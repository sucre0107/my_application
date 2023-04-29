#!/usr/bin/env bash

echo -e "\033[34m--------------------wsgi process--------------------\033[0m"

ps -ef|grep uwsgi_my_application.ini | grep -v grep

sleep 0.5

echo -e '\n--------------------going to close--------------------'

ps -ef |grep uwsgi_my_application.ini | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

echo -e '\n----------check if the kill action is correct----------'

/envs/my_application/bin/uwsgi  --ini uwsgi_my_application.ini &  >/dev/null

echo -e '\n--------------获取静态文件，完全覆盖原来的文件--------------'
sleep 1

python3 manage.py collectstatic --noinput

echo -e '\n\033[42;1m----------------------started...----------------------\033[0m'
sleep 1

ps -ef |grep uwsgi_my_application.ini | grep -v grep
