#! /bin/bash
#source /home/devil/django/wsn/bin/activate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -9
