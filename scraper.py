from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#This code extracts data from a single beer review page.

def extract_info(url, fields, state):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    else:
        soup = BeautifulSoup(resp.text, "lxml")
        ret_data = []
        for field in fields:
            ret_data.append(get_value(soup, field, state))
        return ret_data

def get_value(soup, field_name, state):
    if field_name == 'Title':
        obj = soup.find(class_= 'row beer-header').find(class_='user-header')
        return obj.text.strip('\n')
    elif field_name == 'Descr':
        obj = soup.find(class_='commercial-description-container')
        if obj:
            return obj.text.replace('\n','').replace('\r', '')
        else:
            return None
    elif field_name == 'Place':
        return state
    else:
        obj = soup.find(text=re.compile(field_name))
        if not obj:
            return None
        # this works for most of the values
        next_sibling = obj.findNext()
        if next_sibling:
            return next_sibling.text
        else:
            return None
