import numpy as np 
import pandas as pd 
import re
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
# 이 파이썬 코드는 데이터 분석하기에 앞서,
# 분석이 용이하게 하기 위하여 전처리를 수행하는 코드들이다. 

#한글 출력을 위한 한글 폰트 지정 
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#크롤링 완료한 엑셀 파일 LOAD
df=pd.read_excel('jobkorea_data.xlsx',header=0, encoding="utf-8")

df['comp_member_number']=df['comp_member_number'].str.replace(',','')
df['avg_salary']=df['avg_salary'].str.replace(',','')
df['endday']=df['endday'].str.replace('~','').str.replace('.','-').str.replace('(월)','')\
.str.replace('(화)','').str.replace('(수)','').str.replace('(목)','').str.replace('(금)','').str.replace('(토)','').str.replace('(일)','')
df['endday']=df['endday'].str.replace('()','')

if df['comp_year'].any()=="년차)":
	df['comp_year']=df['comp_member_number']
	df['comp_member_number']=''

df['title']=df['title'].str.replace(',','')
df['region']=df['region'].str.replace(',','')
# df['comp_year']=df['comp_year'].str.replace(',','')
df['comp_spec']=df['comp_spec'].str.replace(',','-')
df['comp_level']=df['comp_level'].str.replace('\n','').str.replace(' ','')
df['comp_level']=df['comp_level'].str.replace('(','').str.replace(')','').str.replace('"','')
df['comp_level']=df['comp_level'].str.replace('투자기업','').str.replace('해외상장법인자회사','').str.replace('해외상장','').str.replace('코스피','').str.replace('비상장','').str.replace('코스닥','').str.replace('코넥스 상장','').str.replace('코스닥 상장','').str.replace('주권(유가증권)상장','').str.replace('상장','').str.replace('코넥스','')
#기업 매출액 중 조/억/만 -> 숫자 변환 
df['comp_revenue']=df['comp_revenue'].str.replace(',','').str.replace('원','').str.replace(' ','')
df['comp_revenue']=df['comp_revenue'].str.replace('천','000').str.replace('조','00000000 ').str.replace('억','0000 ').str.replace('만','')

x=df['comp_revenue'].str.split(' ')
x=x.values.tolist()


#앞서 처리한 기업 매출액 숫자들을 합함  (만 단위)
# 예)) o조 o억 o천만 --> 숫자변환  (만 단위)
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

df['cover_letter_Q']=df['cover_letter_Q'].str.replace(',','').str.replace('\n','').str.replace('(','').str.replace(')','')
df['cover_letter_A']=df['cover_letter_A'].str.replace(',','').str.replace('\n','').str.replace('(','').str.replace(')','')
df['interview_Q']=df['interview_Q'].str.replace(',','').str.replace('\n','').str.replace('(','').str.replace(')','')
df['interview_review']=df['interview_review'].str.replace(',','').str.replace('\n','').str.replace('(','').str.replace(')','')


print(df.info())
print(df.head())

#csv형식으로 변환

df.to_excel("aa.xlsx",encoding="utf-8")
