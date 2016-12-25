#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'othreecodes'

import requests
from bs4 import BeautifulSoup
BASE_URL = 'http://www.lsmvaapvs.org'
import re

def parse_response(response):
    soup = BeautifulSoup(response.text,"html.parser")
    try:
        data = soup.find_all('td')
    except:
        return False;

    '''Cleaning the HTML tags from the string'''
    for i in range(0,len(data)):
        data[i] = clean_html_tags(str(data[i]))

    '''Turning the list into a dict'''
    data_dict = dict(zip(*[iter(data)] * 2))
    return data_dict


'''Clean the HTML tags from response'''
def clean_html_tags(raw_html):
    clean = re.compile('<.*?>')
    clean_text = re.sub(clean, '', raw_html)
    return clean_text

'''MVRD class'''
class Mvrd:
    def __init__(self,plate_number):
        self.plate_number = plate_number

    '''Getting the raw html from www.lsmvaapvs.org'''
    def get_data(self):
        response = requests.get(BASE_URL+'/search.php',{'vpn':self.plate_number})
        data = parse_response(response=response)
        return data
