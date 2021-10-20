# DATA PIPELINES - Project 5 
The purpose of the data engineering capstone project is to combine what I've learned throughout the program. 
I have work with three datasets to complete the project. The main dataset will include data on immigration to the United States, and supplementary datasets will include data on airport codes and U.S. city demographics.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Files](#files)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
This project emulates a real case scenario where an automated ETL process is required to explore and analyse data from immigration, airports and demographics in US to have a better understanding on this topic.
The idea behind this project is to generate an individualized social plan for each city to integrate and help the newcomers. The main goal is to generate three types of solutions:
* Plan for students integration
* Plan for families that came for business  
* Plan for Tourists 

For each city it would be studied the type of immigration that exist, and try to adequate the best plan according to the city needs and offer.

The project follows the follow steps:
* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up


## Technologies Used
- Python - version 3.0

## Files 
- Capstone_Project_Report.ipynb : it is the Jupyter Notebook where the Scope of the project is expleined. Then, there is also a Data exploration with Apache Spark. Finally there is a summary report of the project.

- DataDictionary.pdf: It is a pdf document where for each field, I provide a brief description of what the data is and where it came from.

- airflow folder: There is all the Airflow structure and the scripts to run the Data pipeline designed for this project

## Features
List the ready features here:
1. DAGS

A DAG (Directed Acyclic Graph) is the core concept of Airflow, collecting Tasks together, organized with dependencies and relationships to say how they should run. The DAG itself doesn't care about what is happening inside the tasks; it is merely concerned with how to execute them - the order to run them in, how many times to retry them, if they have timeouts, and so on.

2. Plugins

Airflow has a simple plugin manager built-in that can integrate external features to its core by simply dropping files in your $AIRFLOW_HOME/plugins folder.
Airflow offers a generic toolbox for working with data. Different organizations have different stacks and different needs. Using Airflow plugins can be a way for companies to customize their Airflow installation to reflect their ecosystem.
In this project we have 4 different operators:
a)	stage_redshift: to extract data from the s3 to upload it to the Redshift.
b)	load_fact: to generate the fact table songplays.
c)	load_dimension: to generate the 4 dimentional tables arround the fact table. (songs, artists, users and time)
d)	data_quality: a quality test to check if all the ID are not null values. 

3. helpers

Is a script with all the SQL statements that will be used for the operators. 

## Setup
To run this project locally, I wold reccommend to create an environment with "virtual environment" 
Web to create a venv [_here_](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Then, it will be needed to install these packages to make run the project.

4. s3 Amazon Resource
s3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere.

5. Redshift Amazon Resource
Redshift Amazon Resource: It is a fast, fully managed data warehouse that makes it simple and cost-effective to analyze data using standard SQL with existing Business Intelligence (BI) tools. Here we transform the data to obtain our clean data modell prepared to create dasboards and analisys.

6. Apache Airflow
It is an open-source, distributed processing system used for big data workloads. It utilizes in-memory caching, and optimized query execution for fast analytic queries against data of any size. It allow me to explore the data in an easy and fast way.

## Usage

We have applied a ETL pipeline in which there is a connection, using AWS keys, to the public s3 bucket that I have created with the uploaded csv files. This information is extracted and transformed to a snowflake schema organization. Then, the transformed tbales are uploaded to a data warehouse repository in AWS calles Redshift. 


To run the project it is needed to follow this steps:

`create a s3 repository and upload the created csv files
create a Redshift resource and upload the create_tables scripts through the console
Run the Airflow webserver 
Check that the code is the final version
Create the Admin Connections (aws_credentials and redshift_conn
Run the DAG 
Check if the Graph is completed with success)`


## Project Status
Project is: _complete_ 


## Room for Improvement
Both s3 and Redshift can scale-up with more capacity to absorve 100x data increase. However, I would suggest to create an Amazon EMR with a previus ingestion of the data using Apache Spark. 
## Acknowledgements
- Udacity team.
- colleges from the online course


## Contact
Created by [@maullaina] maullaina@gmail.com