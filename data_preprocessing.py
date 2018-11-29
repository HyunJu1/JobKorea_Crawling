import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('sample_6400.xlsx',header=0)

df['comp_member_number']=(pd.to_numeric(df['comp_member_number'].str.replace(',',''), errors='coerce'))
df['avg_salary']=(pd.to_numeric(df['avg_salary'].str.replace(',',''), errors='coerce'))


if df['comp_year'].any()=="년차)":
	df['comp_year']=df['comp_member_number']
	df['comp_member_number']=''

df['comp_year']=(pd.to_numeric(df['comp_year'].replace(',',''), errors='coerce'))
df['comp_spec']=df['comp_spec'].str.replace(',','-')
df['comp_level']=df['comp_level'].str.replace('\n','').str.replace(' ','')



df['comp_revenue']=df['comp_revenue'].str.replace(',','').str.replace('원','').str.replace(' ','')
df['comp_revenue']=df['comp_revenue'].str.replace('천','000')
df['comp_revenue']=df['comp_revenue'].str.replace('조','0000000 ')
df['comp_revenue']=df['comp_revenue'].str.replace('억','000 ')
df['comp_revenue']=df['comp_revenue'].str.replace('만','')

x=df['comp_revenue'].str.split(' ')
x=x.values.tolist()
print(x[0][0])
print(x[0][1])
print(x[1][0])
i=0

while i<len(x):
	if x[i]:
		try:

			if len(x[i])==3:
				if(x[i][0]==''):
					x[i][0]=0
				if(x[i][1]==''):
					x[i][1]=0
				if(x[i][2]==''):
					x[i][2]=0				
				df['comp_revenue'][i]=int(x[i][0])+int(x[i][1])+int(x[i][2])
			elif len(x[i])==2:
				if(x[i][0]==''):
					x[i][0]=0
				if(x[i][1]==''):
					x[i][1]=0
				df['comp_revenue'][i]=int(x[i][0])+int(x[i][1])
			i+=1
		except Exception as e:
			i+=1
			pass


df['cover_letter_Q']=df['cover_letter_Q'].str.replace(',','').str.replace('\n','')
df['cover_letter_A']=df['cover_letter_A'].str.replace(',','').str.replace('\n','')

df['interview_Q']=df['interview_Q'].str.replace(',','').str.replace('\n','')
df['interview_review']=df['interview_review'].str.replace(',','').str.replace('\n','')

df['endday']=df['endday'].str.replace('~','').str[0:10].str.replace('.','-')



print(df.info())
print(df.head())

df.to_excel("result_6400.xlsx",encoding="utf-8")
