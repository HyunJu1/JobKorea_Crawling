import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('sample_5200.xlsx',header=0)

df['comp_member_number']=(pd.to_numeric(df['comp_member_number'].str.replace(',',''), errors='coerce'))
df['avg_salary']=(pd.to_numeric(df['avg_salary'].str.replace(',',''), errors='coerce'))

#df = df.apply(lambda x: x.str.replace(',', ' '))
if df['comp_year'].any()=="년차)":
	df['comp_year']=df['comp_member_number']
	df['comp_member_number']=''

df['comp_year']=(pd.to_numeric(df['comp_year'].replace(',',''), errors='coerce'))
df['comp_spec']=df['comp_spec'].str.replace(',','-')
df['comp_level']=df['comp_level'].str.replace('\n','').replace('\t','')
#df['회사 영업이익']=(pd.to_numeric(df['회사 영업이익'].replace(',','').replace('억','').replace('천','000').replace('십','0'), errors='coerce'))


print(df.info())
print(df.head())

df.to_excel("result_5200_test.xlsx",encoding="utf-8")
