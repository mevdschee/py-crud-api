# py-crud-api

A Python port of the full php-crud-api project (single file REST API)

NB: WORK IN PROGRESS - NOT FINISHED YET!

### Installing / Running

You need to execute the following to install dependencies on Ubuntu 16.04:

    sudo apt-get install python pip libev-dev libprotobuf-dev protobuf-compiler
    export MYSQLXPB_PROTOC=/usr/bin/protoc
    export MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/include/google/protobuf
    export MYSQLXPB_PROTOBUF_LIB_DIR=/usr/lib/x86_64-linux-gnu
    pip install bjoern mysql-connector gunicorn meinheld

To run single core (using Bjoern):

    python api.py

To run multi core (using Gunicorn and Meinheld):

    gunicorn --workers=4 --worker-class="egg:meinheld#gunicorn_worker" api:app
    
NB: workers should match core count.

### Performance improvements

Do you have an idea for a performance improvement? Open an [issue](https://github.com/mevdschee/py-crud-api/issues) or a [pull request](https://github.com/mevdschee/py-crud-api/pulls).
