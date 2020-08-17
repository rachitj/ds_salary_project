# Salary Predictor for Analytics Professionals in Canada

This is an ongoing project....

![](https://github.com/rachitj/ds_salary_project/blob/data_eda/data-science.png)

## Description
Analytics is one of the most exciting roles in current times. Using data to tell stories is a huge plus for companies. There are different kind of roles in analytics field such as Data Analyst, Data Scientist, Machine Learning Engineer, Data Engineer etc. As their job-roles and responsibities vary, their salary also varies. Though all these roles require expertise in technologies like R, Python, SQL, Excel, Machine Learning, Deep Learning, API development, Visualization( Tableau and Power BI), Web Scraping etc. The salaries might also vary based on location and several other factors. In this project, we will explore the analytics world of Canada.

## Objective
* Create an automated tool that helps analytics professional negotiate their salary.
* Collect the salaries data by scraping glassdoor website
* Perform feature engineerig to extract the information if languages like Python, R ,AWS etc are mentioned in Job Description
* Perform Exploratory Data Analysis on the dataset. Check if the data makes sense. Find the relationships and outliers  in our dataset.Check for nulls etc.
* Create and optimize regression models. Use Mean Absolute Error for scoring. :
  * Mutiple Linear Regression
  * Lasso and Ridge Regression
  * Decision Tree Regressor
  * SVM Regressor
  * Random Forest Regressor
* Productionize the model using Flask API

## Data Collection : Web Scraping
We have scraped the data using selenium. We have cleaned the data and have following features:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
* Data has been cleaned. Null Values have been checked. 
* Perform feature engineerig to extract the information if languages like Python, R ,AWS etc are mentioned in Job Description
* Some fetaures have been dropped while some have been genrated. Also datatypes have been defined.
* The final feautures to be used for model building are :
 0   Job Description       438 non-null    object 
 1   Rating                438 non-null    float64
 2   Company Name          438 non-null    object 
 3   Location              438 non-null    object 
 4   Headquarters          438 non-null    object 
 5   Size                  438 non-null    object 
 6   Founded               438 non-null    int64  
 7   Type of ownership     438 non-null    object 
 8   Industry              438 non-null    object 
 9   Sector                438 non-null    object 
 10  Revenue               438 non-null    object 
 11  Competitors           438 non-null    object 
 12  min_salary            438 non-null    int64  
 13  max_salary            438 non-null    int64  
 14  avg_salary            438 non-null    float64
 15  age_of_company        438 non-null    int64  
 16  Job_title_simplified  438 non-null    object 
 17  seniority             438 non-null    object 
 18  R                     438 non-null    int64  
 19  python                438 non-null    int64  
 20  power_bi              438 non-null    int64  
 21  tableau               438 non-null    int64  
 22  ms_excel              438 non-null    int64  
 23  sql                   438 non-null    int64  
 24  spark                 438 non-null    int64  
 25  aws                   438 non-null    int64  
 26  azure                 438 non-null    int64  
 27  google_cloud          438 non-null    int64  
 28  scraping              438 non-null    int64  
 29  api_development       438 non-null    int64  
 30  machine_learning      438 non-null    int64  
 31  deep_learning         438 non-null    int64  
 32  statistics            438 non-null    int64  


## Resources
* Python Version : 3.7
* https://github.com/arapfaik/scraping-glassdoor-selenium
* https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905?gi=2c2d8b16a520
* https://github.com/PlayingNumbers/ds_salary_proj
* https://github.com/PlayingNumbers/ds_salary_proj/commits?author=PlayingNumbers
* Data Science Image : https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bioenergyconsult.com%2Fdata-science%2F&psig=AOvVaw1QknCF094B02tJctd6H3JG&ust=1596814771632000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDFq-70husCFQAAAAAdAAAAABAD
* Flask API deployment : https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Credits 
Thanks Ken Jee for this project and your contribution to the community. The project idea and some of the codes have been cloned  from Ken Jee's github portfolio(as credited in the resurces). I have modified the codes and added my analysis in the project. 
https://github.com/PlayingNumbers/ds_salary_proj/commits?author=PlayingNumbers
