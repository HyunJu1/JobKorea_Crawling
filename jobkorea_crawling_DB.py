"""
60151196 문현주

local DB :

PYMSQL 활용

create table jobkorea (

id bigint(11) AUTO_INCREMENT PRIMARY KEY,
name varchar(50),
endday varchar(50),
title varchar(100),
dept varchar(50),
career varchar(50),
edu varchar(50),
region varchar(50)

)


"""
import os
import zipfile

import requests
from bs4 import BeautifulSoup
import time
import re
import pymysql

# 잡코리아 현재 신입 공채 올라온것

urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="

name,endday,title,dept,dept2,dept3,coLevel,career,edu,region='','','','','','','','','',''


# Local DB 사용할 때
# db=  pymysql.connect("localhost","root","0000","jobkorea", charset='utf8')


# AWS RDS 사용할 때

rds_host= "jobkorea-db-rds.curo8latovej.ap-northeast-2.rds.amazonaws.com"
name=""
password=""
db_name="jobkorea"
db=pymysql.connect(rds_host,user=name,passwd=password,db=db_name)

cursor = db.cursor()

try:

    # BeautifulSoup을 활용한 Jobkorea Website data parsing
    req = requests.get(urlpage)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')


    a=soup.find("span",id="TabIngCount")

    # 여기에서 aa 값은 리스트의 총 개수를 구한 것이다.
    aa=a.get_text(strip=True, separator='-')
    aa=str(aa).replace("(","").replace(")","").replace(",","")

    # 한 페이지당 리스트가 40개 들어있으므로 40으로 나눠준 것을 page 변수에 넣어준다.
    page= int(int(aa)/40)+1

    # 각 List 별로 반복
    for pa in range(page):

        # 한번에 갖고오게 되면 jobkorea 사이트 측에서 IP제한을 걸게 된다.
        # 이를 방지하기 위해 1초에 한 페이지씩만 갖고오게 해야한다.

        time.sleep(1)
        sendpage=urlpage+str(pa)
        data = requests.get(sendpage)
        rawdata = data.text
        parser = BeautifulSoup(rawdata, 'html.parser')
        realdata = parser.select(
        '.filterList li'
        )
        # 각각의 배열들에 값을 하나씩 담는 방법 사용
        data = []
        for q in realdata:
            name=q.select(
                '.co .coTit .coLink')[0].string
            #print(name)
            endday=q.select(
                '.side .day'      )[0].string
            #print(endday)
            title=q.select(
                '.info .tit .link span'  )[0].string

            #print(title)
            dept=q.select(
                '.info .sTit span')[0].string

            career=q.select(
                '.sDesc strong')[0].string

            edu=q.select(
                '.sDesc span')[0].string

            region=q.select(
                '.sDesc span:nth-of-type(2)')[0].string


            endday=str(endday).replace('~','').replace('.','-').replace('(월)','')\
            .replace('(화)','').replace('(수)','').replace('(목)','').replace('(금)','').replace('(토)','').replace('(일)','')

            print(name, endday , title)

            data.append((name,endday,title,dept,career,edu,region))

        query = """insert into jobkorea(name,endday,title,dept,career,edu,region) values (%s, %s, %s, %s,%s,%s,%s)"""
        cursor.executemany(query, tuple(data))
        db.commit()

except Exception as e:
    print(e)
