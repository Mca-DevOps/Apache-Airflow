# Apache-Airflow get started (version 2.10.5)

Introduction to Apache Airflow

<image src="https://blog.cloudxlab.com/wp-content/uploads/2021/06/image-2.png" width=1000 center>

[<img src="https://img.shields.io/badge/Docker-28.4.0-blue.svg?logo=docker   ">](https://www.docker.com/)     [<img src="https://img.shields.io/badge/Apache/Airflow-2.10.5-yellow.svg?logo=apacheairflow   ">](https://airflow.apache.org/)   [<img src="https://img.shields.io/badge/Postgres-15-9cf.svg?logo=postgresql   ">](https://www.postgresql.org/)   [<img src="https://img.shields.io/badge/MinIO AIStor-latest-red.svg?logo=minio   ">](https://www.min.io/)   


## 1. Overwiew
This repository is a tour of main concepts of Apache Airflow. it contains some DAG examples ready for use in order to practice some concepts like **Operators**, **Sensors**, **XComs**, **Connections** and so on. At the end, of this README, you'll find a link to a mini-project's README, that is an application of the main Airflow concepts.

<br/>


---
## 2. Prerequisites

For running this project locally, you need to have the following tools installed on your device:
- **Docker**: which will be the containerization engine (you can use Podman as well)
- **Git**: for pulling the project's repository

<br/>


---
## 3. Setting up the environment

After satisfying the above requirements, you can proceed with the following steps:

**Step 1**: Clone the project's repository
```bash
$ git clone https://github.com/Mca-DevOps/Apache-Airflow.git
```

**Step 2**: At the root of the repository's directory, execute the following command in order to generate a blueprint of a `.env` file which will contain all necessary credentials for Airflow logging in and variables.

```bash
$ make dotenv
```



**Step 3**: Include MinIO AIStor license to activate its container. Go to [MinIO AIStor website](https://www.min.io/pricing) and click `Free > Get started`. You'll receive your license through e-mail. Download it on your local disk and drop the `minio.license` file into `minio/` directory. It should looks like this at the end :
```bash
$ tree minio
minio
├── certs
├── data
└── minio.license

3 directories, 1 file
```

**Step 4**: Finally set up the containers in this order:
```bash
$ docker compose up airflow-init
````

```bash
$ docker compose up -d
```

```bash
$ make minio-aistor
```
Make sure every containers are running well without error by executing this command:
```bash
$ docker ps
````
To open Airflow webserver UI, go in your navigator and enter this URL:
```
http://localhost:8080
``` 
To open MinIO Aistor console, go in your navigator and enter this URL:
```
http://localhost:9009
```

<br/>

---

## 4. Some files content
It's import to make some files content fathomable for the user.
- **airflow-volumes/**: Airflow is composed of some components as defined in the `docker-compose.yaml file`. Each component that is a container has a volume where data is persisted. To keep this data available even after shutting down all containers, those volumes are binded to local folders. Those folders are contained in `airflow-volumes/` directory.

- **minio/**: Minio being a container, The logic behind `Minio/` directory is the same as the one behind `airflow-volumes/`. Moreover, it contains `minio.license` which is necessary to activate MinIO AIStor container

- **Dockerfile.airflow**: It's an extended docker image configuration file of `apache/airflow` docker image. It contains `requirements.txt` file which will install all needed python packages for the DAGs development

- **.env**: This file contains all variables and credentials needed to run efficiently and correctly the `docker-compose.yaml` file. Refer to [Troubleshooting section](#Troubleshooting) for more details.

- **docker-compose.yaml**: contains containers definitions for Airflow webserver, scheduler, worker, Postgres (Metadata database for Airflow). This definition is a Docker stack because they share the same docker network and can communicate one another.

- **Makefile**: a file where some commands are defined in order to automate some tasks like the `.env` file creation and MinIO AIStor container creation

<br/>

---
## 5. Use cases
Let deep dive into various use cases resolved through DAGs in the airflow-volumes/DAG

- **DAGs and Operators**: Introduction to DAGs and Operators in Airflow. a DAG(Directed Acyclic Graph) is a sequence of tasks and tasks are the logical representation of an Operator and the DAG's nodes. Each task may have a downstream (a descendant node) and/or an upstream (an ascendant node) task. There are a bunch of operators preset delivered by airflow but the user can create his own ones. Check the examples with [BashOperator](./airflow-volumes/dags/first_dag.py) and for [PythonOperator](./airflow-volumes/dags/pythonOpDAG.py)

- **XComs**:

- **Airflow Connections**: It's a feature powered by Airflow which allows the user to connect some data sources to the platform in order to create tasks which will interact with them.

<image src="./doc/connections.gif" width=1000 center>

- **Sensors**:

<br/>


---
## Troubleshooting
> Avoid using `postgres` as value for `POSTGRES_USER` variable in `.env` file. It'll disturb the logging in yo your postgres container. And **Airflow Postgres Connection** may not be able to log in your postgres container.

> If you encounter some writing permissions issues for `airflow-volumes/` directory especially `airflow-volumes/dags/` one, execute the following command in your terminal:
>```bash
>$ id -u
>```
> Then copy the output value and paste it as value of the `AIRFLOW_UID` variable in the `.env` file.

> Airflow UI > Admin > Connections > "+" 
> Extra
>```json
>{
>  "aws_access_key_id": "minioadmin",
>  "aws_secret_access_key": "minioadmin",
>  "endpoint_url": "http://localhost:9008",
>  "addressing_style": "path"
>}
>```

<br/>

<br />

## **CREDITS**

**AUTHOR :** ADOTRI Frimpong

