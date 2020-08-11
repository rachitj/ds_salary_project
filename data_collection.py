# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:36:42 2020

@author: Rachit J
"""
import glassdoor_scraper as gs
import pandas as pd

path= "C:/Users/kaira/Documents/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 5)
df = pd.DataFrame(df)
df.head()
df.to_csv('glassdoor_jobs_data.csv', index = False)


