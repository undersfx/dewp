SHELL := /bin/bash
.PHONY: clean nifi setup elastic kibana


setup:
	@echo "Setting directory tree"
	mkdir logs nifi_files nifi_config pgadmin postgres
	sudo chmod -R 777 logs nifi_files nifi_config pgadmin postgres
	@echo "Creating docker network"
	docker network create etl_network

nifi:
	docker-compose -f nifi-compose.yml up -d

airflow:
	docker-compose -f airflow-compose.yml up -d

kibana:
	docker-compose -f kibana-compose.yml up -d

elastic: kibana


compose-all: airflow kibana nifi


sample-data:
	@echo "Generating Sample Data"
	python code_examples/chapter3/inserting_data_into_elasticsearch.py
	python code_examples/chapter3/inserting_data_into_postgres.py

stop-all:
	docker stop $(docker ps -q)

clean:
	-rm nifi_files/*