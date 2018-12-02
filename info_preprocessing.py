import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('info2.xlsx',header=0)



df['comp_revenue']=df['comp_revenue'].str.replace('매출액','').str.replace(' ','')
df['comp_member_number']=df['comp_member_number'].str.replace('사원수','').str.replace(' ','').str.replace('명','')

print(df.info())
print(df.head())

df.to_excel("info_result2.xlsx",encoding="utf-8")
