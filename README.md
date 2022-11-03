![image](https://user-images.githubusercontent.com/85397546/199650294-04e16b50-6998-4687-b514-653aa5a7c1ab.png)

  # Web Phishing Detection
 
 
 IBM_Project: IBM-Project-9002-1658942080
 Batch-Name:B8-2A4E

  

         
              *Vishal Guna
              *Vembu Karthick T
              *Hemapriya R
              *Sabarissan GK
             
Introduction :
               *Phishing  attack  is  a  simplest  way  to  obtain  sensitive information  from innocent  users. Aim  of the  phishers  is to acquire critical information like username, password and bank account details.  Cyber security  persons are now looking for trustworthy  and  steady  detection  techniques  for  phishing websites  detection. This  paper  deals with  machine learning technology for detection of phishing URLs by extracting and analyzing various features of legitimate and phishing URLs. Decision  Tree,  random  forest  and  Support  vector  machine algorithms are used to detect phishing  websites. Aim of the paper is to detect phishing URLs as  well as narrow down to best machine learning algorithm by comparing accuracy rate, false positive and false negative rate of each algorithm.
               
               
  ABSTRACT

   In this paper, we propose a feature-free method for detecting phishing websites using the Normalized Compression Distance (NCD), a parameter-free similarity measure which computes the similarity of two websites by compressing them, thus eliminating the need to perform any feature extraction. It also removes any dependence on a specific set of website features. This method examines the HTML of webpages and computes their similarity with known phishing websites, in order to classify them. We use the Furthest Point First algorithm to perform phishing prototype extractions, in order to select instances that are representative of a cluster of phishing webpages. We also introduce the use of an incremental learning algorithm as a framework for continuous and adaptive detection without extracting new features when concept drift occurs. On a large dataset, our proposed method significantly outperforms previous methods in detecting phishing websites, with an AUC score of 98.68%, a high true positive rate (TPR) of around 90%, while maintaining a low false positive rate (FPR) of 0.58%. Our approach uses prototypes, eliminating the need to retain long term data in the future, and is feasible to deploy in real systems with a processing time of roughly 0.3 seconds.

Overview :
            *There are a number of users who purchase products online and make payments through e-banking. There are e-banking websites that ask users to provide sensitive data such as username, password & credit card details, etc., often for malicious reasons. This type of e-banking website is known as a phishing website. Web service is one of the key communications software services for the Internet. Web phishing is one of many security threats to web services on the Internet. 
          
          
          
Common threats of web phishing:

•	Web phishing aims to steal private information, such as usernames, passwords, and credit card details, by way of impersonating a legitimate entity.

•	It will lead to information disclosure and property damage.

•	Large organizations may get trapped in different kinds of scams.

This Guided Project mainly focuses on applying a machine-learning algorithm to detect Phishing websites.

Solution:
In order to detect and predict e-banking phishing websites, we proposed an intelligent, flexible and effective system that is based on using classification algorithms.  We implemented classification algorithms and techniques to extract the phishing datasets criteria to classify their legitimacy. The e-banking phishing website can be detected based on some important characteristics like URL and domain identity, and security and encryption criteria in the final phishing detection rate. Once a user makes a transaction online when he makes payment through an e-banking website our system will use a data mining algorithm to detect whether the e-banking website is a phishing website or not.



Project Objectives :
               * we’ll be able to understand the problem to classify if it is a regression or a classification kind of problem.
              
               •	we will be able to know how to pre-process/clean the data using different data pre-processing techniques.
               
               •	Applying different algorithms according to the dataset.
               
               •	You will be able to know how to find the accuracy of the model.
               
               •	You will be able to build web applications using the Flask framework.


Knowledge we need to finish up the project:

     *Flask
     *Machine Algorithm(Regression,Classification,Supervised and Unsupervised )
     *Anaconda Navigator


Conclusion:
               *This  project aims  to  enhance  detection  method  to  detect phishing  websites  using  machine  learning  technology.  We achieved  97.14%  detection  accuracy  using  random  forest algorithm  with  lowest false positive rate.  Also result shows that  classifiers give better  performance when we used more data as training data. In  future  hybrid  technology  will  be  implemented  to  detect phishing websites more accurately,  for  which random  forest algorithm  of  machine  learning  technology  and  blacklist method will be used.
         
         
         
         Technical Architecture:

![191585875-9db35871-72b5-476e-ac9b-3795cf3778de](https://user-images.githubusercontent.com/85397546/199651037-95eb9a2a-ce7d-4ebc-b486-03519627d2c2.png)

