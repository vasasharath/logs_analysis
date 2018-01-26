# logs_analysis
Querying DB through python and generating report

## Pre-Requisites
1. [Virtual box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
1. [Vagrant](https://www.vagrantup.com/downloads.html)
1. [Python3](https://www.python.org/downloads/release/python-364)
1. [git](https://git-scm.com/downloads)
1. [Fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
1. Queries document to create the database and tables inside it. Get it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## setup
* Install virtual box, vagrant
* open git bash command line and cd to vagrant sub directory which is downloaded at step 5
* launch the VM by running following command
```
vagrant up
```
* login to the vm using the command

```
winpty vagrant ssh
```
* cd to /vagrant directory to acces the shared documents
* create the database using the command 
```
psql -d news -f newsdata.sql
```

The database includes three tables

- The ```authors``` table includes information about the authors of articles.
- The ```articles``` table includes the articles themselves.
- The ```log table``` includes one entry for each time a user has accessed the site.

## Creating view

This view is used in the query 

```
CREATE VIEW error_log AS SELECT date(time),
                         ROUND(100.0*sum(case log.status when '200 OK' 
                         THEN 0 ELSE 1 END)/COUNT(log.status),2) AS Error_percentage 
						             FROM log 
						             GROUP BY date(time) 
                         ORDER BY 2 DESC;                     
```

Column | Type
------ | -------
date | date
Error_percentage | float

## Running the program 

Run this command to generate the report
```
python3 loganalysis.py
```



