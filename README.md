# py-crud-api

A Python port of the full php-crud-api project (single file REST API)

NB: WORK IN PROGRESS - NOT FINISHED YET!

### Installing / Running

You need to execute the following to install on Ubuntu 16.04:

    sudo apt-get install python pip libev-dev libprotobuf-dev protobuf-compiler
    export MYSQLXPB_PROTOC=/usr/bin/protoc
    export MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/include/google/protobuf
    export MYSQLXPB_PROTOBUF_LIB_DIR=/usr/lib/x86_64-linux-gnu
    pip install bjoern mysql-connector
    python api.py
    
This uses Bjoern and MySQL connection pooling for high performance.

### Performance improvements

Do you have an idea for a performance improvement? Open an [issue](https://github.com/mevdschee/py-crud-api/issues) or a [pull request](https://github.com/mevdschee/py-crud-api/pulls).
