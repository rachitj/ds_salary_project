# Salary Predictor for Analytics Professionals in Canada

This is an ongoing project....

![](https://github.com/rachitj/ds_salary_project/blob/data_eda/data-science.png)

## Description
Analytics is one of the most exciting roles in current times. Using data to tell stories is a huge plus for companies. There are different kind of roles in analytics field such as Data Analyst, Data Scientist, Machine Learning Engineer, Data Engineer etc. As their job-roles and responsibilities vary, their salary also varies. Though all these roles require expertise in technologies like R, Python, SQL, Excel, Machine Learning, Deep Learning, API development, Visualization( Tableau and Power BI), Web Scraping etc. The salaries might also vary based on location and several other factors. In this project, we will explore the analytics world of Canada.

## Objective
* Create an automated tool that helps analytics professional negotiate their salary.
* Collect the salaries data by scraping glassdoor website
* Perform feature engineering to extract the information if languages like Python, R, AWS etc. are mentioned in Job Description
* Perform Exploratory Data Analysis on the dataset. Check if the data makes sense. Find the relationships and outliers in our dataset. Check for nulls etc.
* Create and optimize regression models. Use Mean Absolute Error for scoring.
  * Multiple Linear Regression
  * Lasso and Ridge Regression
  * Decision Tree Regressor
  * SVM Regressor
  * Random Forest Regressor
* Productionize the model using Flask API

## Data Collection: Web Scraping
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
* Perform feature engineering to extract the information if languages like Python, R, AWS etc. are mentioned in Job Description
* Some features have been dropped while some have been generated. Also, datatypes have been defined.
* The final features to be used for model building are:
  * Job Description
  * Rating
  * Company Name
  * Location
  * Headquarters
  * Size
  * Founded
  * Type of ownership
  * Industry
  * Sector
  * Revenue
  * Competitors
  * min_salary
  * max_salary
  * avg_salary
  * age_of_company
  * Job_title_simplified
  * seniority
  * R
  * python
  * power_bi
  * tableau
  * ms_excel
  * sql
  * spark
  * aws
  * azure
  * google_cloud
  * scraping
  * api_development
  * machine_learning
  * deep_learning
  * statistics
  * job_description_len	: Length of job description. This feature helps in understanding if salary has an impact on roles that have been defined well.
  * num_comp : Number of competitors


## Resources
* Python Version: 3.7
* https://github.com/arapfaik/scraping-glassdoor-selenium
* https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905?gi=2c2d8b16a520
* https://github.com/PlayingNumbers/ds_salary_proj
* https://github.com/PlayingNumbers/ds_salary_proj/commits?author=PlayingNumbers
* Data Science Image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bioenergyconsult.com%2Fdata-science%2F&psig=AOvVaw1QknCF094B02tJctd6H3JG&ust=1596814771632000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDFq-70husCFQAAAAAdAAAAABAD
* Flask API deployment: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Credits
Thanks, Ken Jee, for this project and your contribution to the community. The project idea and some of the codes have been cloned from Ken Jee's GitHub portfolio (as credited in the resources). I have modified the codes and added my analysis in the project.
https://github.com/PlayingNumbers/ds_salary_proj/commits?author=PlayingNumbers
