import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('final_sample_16000_1.xlsx',header=0)

df['name']=df['name'].str.replace('㈜','')

if df['comp_year'].any()=="0":
	df['comp_year']=''
if df['comp_year'].any()=="0":
	df['comp_year']=''
if df['comp_year'].any()=="0":
	df['comp_year']=''
if df['comp_year'].any()=="0":
	df['comp_year']=''
if df['comp_year'].any()=="0":
	df['comp_year']=''
if df['comp_year'].any()=="0":
	df['comp_year']=''	
print(df.info())
print(df.head())

df.to_excel("sampling_16000_1.xlsx",encoding="utf-8")
