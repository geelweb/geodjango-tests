# geodjango tests

Install basic tools

    $ sudo apt-get install -y wget git

Install postgres and postgis

    $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    $ sudo apt-get update
    $ sudo apt-get upgrade

    $ sudo apt-get install -y postgresql-9.3 postgresql-9.3-postgis-2.1 python-psycopg2
    $ sudo sed -i.bak -e 's/\(^local.*\)\(peer\)$/\1trust/g' /etc/postgresql/9.3/main/pg_hba.conf
    $ sudo /etc/init.d/postgresql restart

Install python tools

    $ sudo apt-get install -y python-pip python-gdal

Install django and geopy

    $ pip install django geopy

Create the db and add the postgis extensions

    $ createdb -U postgres geodjango

    $ psql -U postgres geodjango -c "create extension postgis"
    $ psql -U postgres geodjango -c "create extension postgis_topology"
    $ psql -U postgres geodjango -c "create extension fuzzystrmatch"
    $ psql -U postgres geodjango -c "create extension postgis_tiger_geocoder"

Clone the repository

    $ git clone https://github.com/geelweb/geodjango-tests.git geodjango
    $ cd geodjango
    $ python manage.py syncdb
    $ python manage.py runserver


