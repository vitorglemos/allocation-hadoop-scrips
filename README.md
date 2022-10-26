# Processing Data Research

## Introduction 

The generation of massive data tends to grow gradually over the years. For this reason, with the high computational cost, we need to think in ways to reduce processing time in this data, such as intelligent resource allocation, distributed processing, parallel processing, and query optimization. Many Big Data management systems were developed to take advantage of different characteristics of the machines on which they are deployed, using strategies to guarantee efficiency and also the quality of the services offered. As part of this research, we investigated how the addition of processing nodes in different scenarios can influence the processing of highly complex queries.


## Myria Plataform 
For this, we use the Myria system, as it allows us to change the query plan to select which nodes (nuclei) the data operations (here called data nodes) and processing operations (here called worker nodes) will take place. The objective is to test how these operations can be affected by I/O concurrency caused by simultaneous access of processing nodes to a single disk resource.

About Myria: https://myria.cs.washington.edu/

## Hadoop and YARN 

Myria uses Hadoop and YARN to allocate processing resources across a cluster of machines. In addition, cluster management is fully handled by YARN, responsible for allocating system resources to the various applications running on a Hadoop cluster and scheduling tasks to be performed on different cluster nodes.

More about Hadoop: https://hadoop.apache.org/


## Script Allocation

The allocation scripts in this project are used to perform performance tests, in addition to removing any temporary files and residuals on the system. Such scripts ensure that tests are clean, cache-free, and with RAM memory free of residue from previous runs. In addition, the scripts also ensure that Hadoop and YARN are working properly, free of the stored data from queries in the database.
