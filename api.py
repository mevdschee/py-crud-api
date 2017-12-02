# Run with (workers should match core count):
#   gunicorn --workers=4 --worker-class="egg:meinheld#gunicorn_worker" api:app

import bjoern, os
import re
import json
import mysql.connector

# connect to the mysql database
link = mysql.connector.connect(host='localhost', user='php-crud-api',
                               password='php-crud-api', db='php-crud-api',
                               charset='utf8', autocommit=True)
cursor = link.cursor(dictionary=True)

def app(environ, start_response):
    # get the HTTP method, path and body of the request
    method = environ['REQUEST_METHOD']
    path = environ.get('PATH_INFO', '').split('/')
    size = int(environ.get('CONTENT_LENGTH', '0'))
    if size > 0:
        data = json.loads(environ['wsgi.input'].read(size))
    else:
        data = {}
    # retrieve the table and key from the path
    table = re.sub(r'[^a-zA-Z0-9_]+', '', path[1] if len(path) > 1 else '')
    key = int(path[2] if len(path) > 2 else '0')
    # escape the columns and values from the input object
    columns = list(re.sub(r'[^a-zA-Z0-9_]+', '', k) for k in data.keys())
    values = list(link.escape_string(str(v)) for v in data.values())
    # build the SET part of the SQL command
    sql = ''
    for i in range(0, len(columns)):
        sql += (',' if i > 0 else '')+'`'+columns[i]+'`="'+values[i]+'"'
    # create SQL based on HTTP method
    if method == 'GET':
        sql = 'select * from `'+table+'`'
        if key > 0:
            sql += ' WHERE id='+str(key)
    elif method == 'PUT':
        sql = 'update `'+table+'` set '+sql+' where id='+str(key)
    elif method == 'POST':
        sql = 'insert into `'+table+'` set '+sql
    elif method == 'DELETE':
        sql = 'delete from `'+table+'` where id='+str(key)
    # execute SQL statement
    try:
        cursor.execute(sql)
        # print results, insert id or affected row count
        start_response('200 OK', [('Content-Type', 'text/html')])
        if method == 'GET':
            if key == 0:
                yield str('[')
            i = 0
            for row in cursor:
                yield str((',' if i > 0 else '')+json.dumps(row))
                i += 1
            if key == 0:
                yield str(']')
        elif method == 'POST':
            yield str(cursor.lastrowid)
        else:
            yield str(cursor.rowcount)
    except (mysql.connector.errors.DatabaseError) as err:
        # die if SQL statement failed
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        yield str(err.args[1])

if __name__ == "__main__":
    bjoern.listen(app, '127.0.0.1', 8000)
    bjoern.run()
