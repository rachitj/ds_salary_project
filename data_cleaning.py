# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:34:45 2020

@author: Rachit J
"""

import pandas as pd


df = pd.read_csv("glassdoor_jobs_data.csv")

# Step[ 1: Salary parsing

# Removing rows where salary data is not present
df = df[df['Salary Estimate'] != '-1']

# Removing Duplicates if any
df = df.drop_duplicates()

# Remove the text string from salary estimates
salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])

# Replace CA$ and K('000') with spaces to use these salary estimates as integers
minus_k_dollar = salary.apply(lambda x:x.replace('K',"").replace('CA$',""))

''' Check if salary estimates has Per hour dollars. In case yes, 
we will remove them as we will focus only on Full time Data Scientist Jobs.
Here'-1' indicates it is not an hourly salary
'''
df['hourly_estimates_index'] = salary.apply(lambda x :x.find('per hour'))

# Get minimum and maximum salary
df['min_salary'] = minus_k_dollar.apply(lambda x : int(x.split('-')[0]))
df['max_salary'] = minus_k_dollar.apply(lambda x : int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+ df['max_salary'])/2

# Remove per hour salary estimates  and drop the unncessary column
df = df[df['hourly_estimates_index'] == -1]
df.drop(['Salary Estimate' ,'hourly_estimates_index'], axis= 1, inplace = True)

# STEP 2: Company Name parsing, text only
df['Company Name'] = df['Company Name'].str[:-3]

# STEP 3 : CHECKING LOCATIONS
location_check = df['Location'].unique()
df['Location'] = df['Location'].apply(lambda x : x.replace("Montréal-Est","Montreal").replace("Montréal-Nord","Montreal"))
df['Location'] = df['Location'].apply(lambda x : x.replace("Toronto,Ontario","Toronto"))



# STE 4 : Age of Company
df['age_of_company'] = df['Founded'].apply(lambda x : x if x <1 else 2020-x)

# STEP 5: Job Title
df['Job Title'] = df['Job Title'].apply(lambda x : 'data analyst' if 'data analyst' in x.lower()
                                               else 'data engineer' if 'data engineer' in x.lower()
                                               else 'data scientist' if 'data scientist' in x.lower() or 'machine learning' in x.lower()
                                               else 'other')
# Remove other roles that were not relevant to data scientist role
df = df[df['Job Title'] != 'other']


# STEP 6: Job Descripton Parsing : Language(Python, R et.) and Years of Experience Required



# PROGRAMMING LANGUAGES, DATABASES AND TOOLS/TECHNOLOGIES
# Python
df['R'] = df['Job Description'].apply(lambda x : 1 if 'r-studio' in x.lower() or 'r studio' in x.lower() or 'rstudio' in x.lower() or ' r ' in x.lower() else 0)

# Python
df['python'] = df['Job Description'].apply(lambda x : 1 if 'python' in x.lower() else 0)

# Power BI
df['power_bi'] = df['Job Description'].apply(lambda x : 1 if 'power-bi' in x.lower() or 'power bi' in x.lower() or 'powerbi' in x.lower() else 0)

# Tableau
df['tableau'] = df['Job Description'].apply(lambda x : 1 if 'tableau' in x.lower() else 0)

# Microsoft Excel
df['ms_excel'] = df['Job Description'].apply(lambda x : 1 if 'microsoft excel' in x.lower() or 'ms excel' in x.lower() else 0)

# SQL
df['sql'] = df['Job Description'].apply(lambda x : 1 if 'sql' in x.lower() else 0)

# Apache Spark
df['spark'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0)

# AWS
df['aws'] = df['Job Description'].apply(lambda x : 1 if ' aws ' in x.lower() or 'amazon web services' in x.lower() else 0)

# Azure
df['azure'] = df['Job Description'].apply(lambda x : 1 if 'azure' in x.lower() else 0)

# Google Cloud
df['google_cloud'] = df['Job Description'].apply(lambda x : 1 if 'google cloud' in x.lower() else 0)

# Web Scraping
df['scraping'] = df['Job Description'].apply(lambda x : 1 if 'scraping' in x.lower() else 0)

# API Development
df['api_development'] = df['Job Description'].apply(lambda x : 1 if ' api ' in x.lower() else 0)

# Machine Learning
df['machine_learning'] = df['Job Description'].apply(lambda x : 1 if 'machine learning' in x.lower() else 0)

# Deep Learning
df['deep_learning'] = df['Job Description'].apply(lambda x : 1 if 'deep learning' in x.lower() else 0)


# Statistics
df['statistics'] = df['Job Description'].apply(lambda x : 1 if 'statistics' in x.lower() else 0)


# STEP 6 : Double Check the data rows where we couldn't find any skill
df['check_skills'] = (df['R']+ df['python']+df['tableau']+df['ms_excel']
                    +df['sql']+df['spark']+df['aws']+df['google_cloud']+
                    df['scraping']+df['api_development'] + df['machine_learning']
                    + df['deep_learning'] + df['statistics'])

# Remove the rows where skills are not mentioned 
df = df[df['check_skills'] !=0]

# STEP 7 : Keep only analytics job roles
df = df[df['Job Title'] != 'other']

# STEP 8 : Drop unnecessay columns
df.drop(columns = [], inplace = True)

# STEP 9 : Save the data
df.to_csv('glassdoor_salary_data_cleaned.csv', index = False)