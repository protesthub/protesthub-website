ProtestHub
==========
[![pipeline status](https://travis-ci.org/protesthub/protesthub-website.svg?branch=master)](https://travis-ci.org/protesthub/protesthub-website.svg?branch=master)

## Requirements
```bash
# Start MariaDB
$ sudo docker run --name=protesthub_dev -e MYSQL_DATABASE=protesthub_dev -e MYSQL_USER=protesthub_dev -e MYSQL_PASSWORD=test -e MYSQL_ROOT_PASSWORD=toor -p 3306:3306 -d mariadb
$ sudo docker start protesthub_dev
# Run migrations
$ python manage.py migrate
```

## Tests
```bash
$ python manage.py test
```
