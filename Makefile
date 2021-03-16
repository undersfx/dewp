SHELL := /bin/bash
.PHONY: clean nifi


nifi:
	docker-compose -f nifi-compose.yml up -d

airflow:
	docker-compose -f airflow-compose.yml up -d

clean:
	-rm nifi/nifi_files/*