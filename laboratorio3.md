# Laboratory 3

## datasets already exported to s3 and hdfs, I'm going to work with hdfs files.

### Hive

DDL querys
DROP DATABASE mybd;
CREATE DATABASE mybd;
USE mybd;

CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE 
LOCATION '/user/hadoop/datasets/onu/hdi/';

CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE 
LOCATION '/user/hadoop/datasets/onu/export/';

CREATE EXTERNAL TABLE docs (line STRING) 
STORED AS TEXTFILE 
LOCATION '/user/hadoop/datasets/gutenberg-small/';

DQL querys

USE mydb;
SHOW tables;
DESCRIBE hdi;

SELECT country, gni FROM hdi WHERE gni > 2000;    
SELECT * FROM `mydb`.`hdi` LIMIT 100;
SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;
SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
GROUP BY word 
ORDER BY word DESC LIMIT 10;

SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 

!(emr1)[images/hiv1.png]
!(emr2)[images/hiv2.png]
!(emr3)[images/hiv3.png]
!(emr4)[images/hiv4.png]
