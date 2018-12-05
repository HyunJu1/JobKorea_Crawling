import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('이게진짜다.xlsx',header=0)

df['name']=df['name'].str.replace('㈜','')

# a= 0
# if df['emp_grade_score'].any()==0:
# 	df['emp_grade_score']=''
# if df['emp_toeic_score'].any()==0:
# 	df['emp_toeic_score']=''
# if df['emp_ts_score'].any()==0:
# 	df['emp_ts_score']=''
# if df['emp_opic_score'].any()==0:
# 	df['emp_opic_score']=''
# if df['emp_etcL_score'].any()==0:
# 	df['emp_etcL_score']=''
# if df['emp_license_score'].any()==0:
# 	df['emp_license_score']=''	
# if df['emp_otherCountry_score'].any()==0:
# 	df['emp_otherCountry_score']=''
# if df['emp_intern_score'].any()==0:
# 	df['emp_intern_score']=''
# if df['emp_award_score'].any()==0:
# 	df['emp_award_score']=''
# if df['comp_industry'].any()==0:
# 	df['comp_industry']=''
# if df['interview_Q'].any()==a:
# 	df['interview_Q']=''

# if df['comp_year'].any()==a :
# 	df['comp_year']=''	
# if df['emp_grade_score'].any()==a:
# 	df['emp_grade_score']=''
# if df['emp_toeic_score'].any()==a:
# 	df['emp_toeic_score']=''
# if df['emp_ts_score'].any()==a:
# 	df['emp_ts_score']=''

# if df['emp_opic_score'].any()==a:
# 	df['emp_opic_score']=''
# if df['emp_etcL_score'].any()==a:
# 	df['emp_etcL_score']=''
# if df['comp_level'].any()==a:
# 	df['comp_level']=''	
# if df['emp_otherCountry_score'].any()==a:
# 	df['emp_otherCountry_score']=''
# if df['comp_spec'].any()==a:
# 	df['comp_spec']=''
# if df['comp_revenue'].any()==a:
# 	df['comp_revenue']=''
# if df['comp_year'].any()==a:


# 	df['comp_year']=''
# if df['cover_letter_Q'].any()=="0":
# 	df['cover_letter_Q']=''
# if df['cover_letter_A'].any()=="0":
# 	df['cover_letter_A']=''	
# if df['avg_salary'].any()=="0":
# 	df['avg_salary']=''
# if df['candidate_num'].any()=="0":
# 	df['candidate_num']=''	

print(df.info())
print(df.head())

df.to_excel("이게진짜다_2.xlsx",encoding="utf-8")
