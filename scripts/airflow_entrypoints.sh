#!/usr/bin/env bash
airflow resetdb
airflow db init
airflow upgradedb
airflow users create -r ngisecoge -u admin -e admin@admin.com -f admin -l admin -p admin
airflow scheduler &
airflow webserver