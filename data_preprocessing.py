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
df['comp_level']=df['comp_level'].str.replace('\n','').str.replace(' ','')
#df['회사 영업이익']=(pd.to_numeric(df['회사 영업이익'].replace(',','').replace('억','').replace('천','000').replace('십','0'), errors='coerce'))
df['comp_location']=''
df['comp_revenue']=df['comp_revenue'].str.replace(',','')
df['cover_letter_Q']=df['cover_letter_Q'].str.replace(',','').str.replace('\n','')
df['cover_letter_A']=df['cover_letter_A'].str.replace(',','').str.replace('\n','')

df['interview_Q']=df['interview_Q'].str.replace(',','').str.replace('\n','')
df['interview_review']=df['interview_review'].str.replace(',','').str.replace('\n','')

df['endday']=df['endday'].str.replace('~','').str[0:10]



print(df.info())
print(df.head())

df.to_excel("result_5200_test1.xlsx",encoding="utf-8")
