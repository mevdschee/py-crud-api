from wsgiref.simple_server import make_server
from wsgiref.util import shift_path_info
import re
import json
import pymysql

def app(environ, start_response):
    # get the HTTP method, path and body of the request
    method = environ['REQUEST_METHOD']
    size = int('0'+environ.get('CONTENT_LENGTH'))
    if size > 0:
        data = json.loads(environ['wsgi.input'].read(size))
    else:
        data = {}
    # connect to the mysql database
    link = pymysql.connect(host='localhost', user='php-crud-api', password='php-crud-api',
                           db='php-crud-api', charset='utf8', autocommit=True)
    # retrieve the table and key from the path
    table = re.sub(r'[^a-z0-9_]+', '', shift_path_info(environ), flags=re.IGNORECASE)
    try:
        key = int(shift_path_info(environ))
    except (TypeError, ValueError):
        key = 0
    # escape the columns and values from the input object
    columns = list(re.sub(r'[^a-z0-9_]+', '', k, flags=re.IGNORECASE) for k in data.keys())
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
    cursor = link.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        # print results, insert id or affected row count
        start_response('200 OK', [('Content-Type', 'text/html')])
        if method == 'GET':
            if key == 0:
                yield str('[')
            for i in range(0, cursor.rowcount):
                yield str((',' if i > 0 else '')+json.dumps(cursor.fetchone()))
            if key == 0:
                yield str(']')
        elif method == 'POST':
            yield str(cursor.lastrowid)
        else:
            yield str(cursor.rowcount)
    except (pymysql.DatabaseError) as err:
        # die if SQL statement failed
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        yield str(err.args[1])
    # close mysql connection
    link.close()

make_server('127.0.0.1', 8080, app).serve_forever()
