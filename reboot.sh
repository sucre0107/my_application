#!/usr/bin/env bash

echo -e "\033[34m--------------------wsgi process--------------------\033[0m"
ps -ef | grep uwsgi_params.ini | grep -v grep

sleep 0.5

echo -e '\n--------------------going to close--------------------'
pkill -f uwsgi_params.ini
sleep 0.5

echo -e '\n----------check if the kill action is correct----------'
ps -ef | grep uwsgi_params.ini | grep -v grep

echo -e '\n--------------获取静态文件，完全覆盖原来的文件--------------'
python3 manage.py collectstatic --noinput || echo "collectstatic failed"

echo -e '\n\033[42;1m----------------------starting uwsgi...----------------------\033[0m'
/envs/my_application/bin/uwsgi --ini uwsgi_params.ini

echo -e '\n----------------------current uwsgi status----------------------'
ps -ef | grep uwsgi_params.ini | grep -v grep