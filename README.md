# Apache-Airflow get started (version 2.10.5)

Introduction to Apache Airflow

<image src="https://blog.cloudxlab.com/wp-content/uploads/2021/06/image-2.png" width=1000 center>

[<img src="https://img.shields.io/badge/Docker-28.4.0-blue.svg?logo=docker   ">](https://www.docker.com/)     [<img src="https://img.shields.io/badge/Apache/Airflow-2.10.5-yellow.svg?logo=apacheairflow   ">](https://airflow.apache.org/)   [<img src="https://img.shields.io/badge/Postgres-15-9cf.svg?logo=postgresql   ">](https://www.postgresql.org/)   [<img src="https://img.shields.io/badge/MinIO AIStor-28.4.0-red.svg?logo=minio   ">](https://www.min.io/)   


## 1. Overwiew
This repository is tour of main concepts of Apache Airflow. it contains some DAG examples ready for use in order to practice some concepts like **Operators**, **Sensors**, **XComs**, **Connections** and so on. At the end, of this README, you'll find a link to a mini-project README, that is an application of the learned Airflow concepts.

<br/>


---
## 2. Prerequisites

For running this project locally, you need to have the following tools installed on your device:
- **Docker**: which will be the containerization engine (you can use Podman as well)
- **Git**: for the project's repository pulling

<br/>


---
## 3. Setting up the environment

After satisfying the above requirements, you can proceed with the following steps:

**Step 1**: Clone the project's repository

**Step 2**: At the root of the repository directory, execute the following command to create a `.env` file which will contain all necessary credentials for Airflow logging in and variables.

```bash
$ make dotenv
```



**Step 3**: Include MinIO license to activate the container. Go to [MinIO AIStor website](https://www.min.io/pricing) and click `Free > Get started`. You'll receive your license through e-mail. Download it on your local disk and drop the `minio.license` file into `minio/` directory. It should looks like this at the end :
```bash
$ tree minio
minio
├── certs
├── data
└── minio.license

3 directories, 1 file
```

<br/>

---

## 4. Some files content
It's import to make some files content fathomable for the user.
- **airflow-volumes/**:
- **minio/**:
- **Dockerfile.airflow**:
- **.env**:
- **docker-compose.yaml**:
- **Makefile**:

<br/>

---
## 5. Use cases
Let deep dive into various use cases resolved through DAGs in the airflow-volumes/DAG

- **DAGs and Operators**
- **XComs**
- **Airflow Connections**
- **Sensors**

<br/>


---
## 6. Troubleshooting
> Avoid using `postgres` as value for `POSTGRES_USER` variable in `.env` file. It'll disturb the logging in yo your postgres container. And **Airflow Postgres Connection** may not be able to log in your postgres container.


<br/>

<br />

## **CREDITS**

**AUTHOR :** ADOTRI Frimpong

