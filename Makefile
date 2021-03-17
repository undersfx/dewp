SHELL := /bin/bash
.PHONY: clean nifi


setup:
	mkdir logs nifi_files nifi_config pgadmin postgres
	sudo chmod -R 777 logs nifi_files nifi_config pgadmin postgres 

nifi:
	docker-compose -f nifi-compose.yml up -d

airflow: pg-admin
	docker-compose -f airflow-compose.yml up -d

pg-admin:
	docker-compose -f pgadmin-compose.yml up -d

kibana:
	docker-compose -f kibana-compose.yml up -d

elastic:
	docker-compose -f kibana-compose.yml up -d

stop-all:
	docker stop $(docker ps -q)

clean:
	-rm nifi/nifi_files/*