.PHONY: help init dotenv
.DEFAULT_GOAL = help


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

init: ## Automatically initialize the project
	@echo "Creation of airflow volumes directories"
	@mkdir airflow-volumes
	@mkdir -p airflow-volumes/dags airflow-volumes/logs airflow-volumes/config airflow-volumes/plugins
	@echo "Successfully done"
	@echo "Creation of PostgreSQL volume directory"
	@mkdir postgresql-volume
	@echo "Successfully done"
	@echo "Creation of MongoDB volume directory"
	@mkdir mongodb-volume
	@echo "Successfully done"
	@echo "Creation data/ directory"
	@mkdir data
	@echo "Successfully done"
	@echo "Creation of MinIO data and certs directories"
	@mkdir -p minio/data minio/certs
	@echo "Successfully done"



dotenv: ## Generate the project .env file blueprint
	@echo "Creation of .env file blueprint"
	@echo "AIRFLOW_UID=501\nAIRFLOW_PROJ_DIR=./airflow-volumes\n# AIRFLOW WEBSERVER CREDENTIALS\n_AIRFLOW_WWW_USER_USERNAME=\n_AIRFLOW_WWW_USER_PASSWORD=\n# POSTGRES DATABASE CREDENTIALS\nPOSTGRES_USER=\nPOSTGRES_PASSWORD=" > .env
	@echo "Successfully done"