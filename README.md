ProtestHub
==========

## Requirements
```bash
sudo docker run --name=protesthub_dev -e MYSQL_DATABASE=protesthub_dev -e MYSQL_USER=protesthub_dev -e MYSQL_PASSWORD=test -e MYSQL_ROOT_PASSWORD=toor -p 3306:3306 -d mariadb
sudo docker start protesthub_dev
```
