# geodjango tests

    $ sudo apt-get install wget

    $ vim /etc/apt/sources.list.d/pgdg.list
    deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main 

    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    $ sudo apt-get update
    $ sudo apt-get upgrade

    $ sudo apt-get install postgresql-9.3 postgresql-9.3-postgis-2.1 python-psycopg2
    $ sudo vim /etc/postgresql/9.1/main/pg_hba.conf 
    # replace peer by trust

    $ sudo apt-get install python-pip python-gdal
    $ pip install django geopy

    $ psql -U postgres
    postgres=# create database geodjango;
    postgres=# \c geodjango 
    postgres=# CREATE EXTENSION postgis;
    postgres=# CREATE EXTENSION postgis_topology;    
    postgres=# CREATE EXTENSION fuzzystrmatch;
    postgres=# CREATE EXTENSION postgis_tiger_geocoder;

    $ git clone https://github.com/geelweb/geodjango-tests.git geodjango
    $ cd geodjango
    $ python manage.py syncdb
    $ python manage.py runserver

