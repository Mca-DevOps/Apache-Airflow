.PHONY: help init
.DEFAULT_GOAL = help


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

init: ## Automatically initialize the project
	@echo "Creation of airflow volumes directories"
	@mkdir airflow-volumes
	@mkdir -p airflow-volumes/dags airflow-volumes/logs airflow-volumes/config
	@echo "Successfully done"