import os
import re
import pandas as pd
import datetime
from dateutil.parser import parse
import logging
import numpy as np
import sys
import traceback
import nltk
from nltk.tokenize import RegexpTokenizer
from operator import lt, le, eq, ne, ge, gt

subcat_cols={

        'SV001_DR_S002_6_1003' : {
        'SV' : ['visit_nm', 'svsdtc_001_dts'],
        'QS':['qsdtc_011_dts', 'visit_nm', 'qscat_011']},
        'SV001_DR_S002_7_1003' :{
        'SV' : ['visit_nm', 'svsdtc_001_dts'],
        'QS':['qsdtc_033_dts', 'visit_nm', 'qscat_033']},
        'SV001_DR_S002_8_1003' : {
        'SV' : ['visit_nm', 'svsdtc_001_dts'],
        'QS':['qsdtc_109_dts', 'visit_nm', 'qscat_109']},
        'SV001_DR_S002_9_1003' : {
        'SV' : ['visit_nm', 'svsdtc_001_dts'],
        'QS':['qsdtc_011_dts', 'visit_nm', 'qscat_011']},
}

subcat_rename_cols ={        
    'SV001_DR_S002_6_1003':
    {'SV' : 
        {
        'visit_nm' : 'CRF - Visit',
        'svsdtc_001_dts' : 'CRF - Date'},
     'QS' : 
         {'qsdtc_011_dts': 'ePRO - Date',
          'visit_nm': 'ePRO - Visit',
          'qscat_011' : 'ePRO - Category'},
         
        },
     'SV001_DR_S002_9_1003':
    {'SV' : 
        {
        'visit_nm' : 'CRF - Visit',
        'svsdtc_001_dts' : 'CRF - Date'},
     'QS' : 
         {'qsdtc_011_dts': 'ePRO - Date',
          'visit_nm': 'ePRO - Visit',
          'qscat_011' : 'ePRO - Category'},
         
        },
     'SV001_DR_S002_8_1003':
    {'SV' : 
        {
        'visit_nm' : 'CRF - Visit',
        'svsdtc_001_dts' : 'CRF - Date'},
     'QS' : 
         {'qsdtc_109_dts': 'ePRO - Date',
          'visit_nm': 'ePRO - Visit',
          'qscat_109' : 'ePRO - Category'},
         
        },
     'SV001_DR_S002_7_1003':
    {'SV' : 
        {
        'visit_nm' : 'CRF - Visit',
        'svsdtc_001_dts' : 'CRF - Date'},
     'QS' : 
         {'qsdtc_033_dts': 'ePRO - Date',
          'visit_nm': 'ePRO - Visit',
          'qscat_033' : 'ePRO - Category'},
         
        },
    
}




