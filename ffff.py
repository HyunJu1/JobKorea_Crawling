import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
import re
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('sample_16000.xlsx',header=0)

df['name']=df['name'].str.replace('㈜','')



print(df.info())
print(df.head())

df.to_excel("sampling_16000.xlsx",encoding="utf-8")
