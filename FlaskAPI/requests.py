# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:49:54 2020

@author: Rachit J
"""

import requests
from data_input import data_in

URL = "http://127.0.0.1:5000/predict"

# defining a params dict for the parameters to be sent to the API 
headers = {"Content-Type": "application/json"} 

data = {"input":data_in}


r = requests.get(URL, headers = headers, json = data)

r.json()