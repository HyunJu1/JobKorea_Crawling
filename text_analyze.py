import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('sample1.xlsx',header=0)
df[['합격자 토익','합격자 수상횟수','지원자 수']] = df[['합격자 토익','합격자 수상횟수','지원자 수']].apply(pd.to_numeric) 
print(df.info())
print(df.head())


#plt.plot(df['합격자 수상횟수'],df['지원자 수'])

#plt.show()
df.to_excel("sample3.xlsx")
