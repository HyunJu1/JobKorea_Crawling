import xlsxwriter
import requests
from bs4 import BeautifulSoup
import time
import re
from konlpy.tag import Twitter
from konlpy.utils import pprint
twitter = Twitter()

#결과물 800개
urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="

#마감된 공고
urlpage2="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=1&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="

name,endday,title,dept,dept2,dept3,coLevel,career,edu,region,link,comp_location=[],[],[],[],[],[],[],[],[],[],[],[]

emp_grade_score=[] #학점 
emp_toeic_score=[] #토익점수
emp_ts_score=[] #토익스피킹 점수
emp_opic_score=[] # 오픽 점수 
emp_etcL_score=[] #외국어(기타)
emp_license_score=[] #자격증개수 
emp_otherCountry_score=[]  #해외경험
emp_intern_score=[] #인턴경험횟수
emp_award_score=[] #수상횟수

comp_industry,comp_member_number,comp_year, comp_level, comp_spec,comp_revenue=[],[],[],[],[],[]

cover_letter_Q,cover_letter_A,interview_Q,interview_review=[],[],[],[]
candidate_num, avg_salary=[],[]

cover_letter_A_nouns, cover_letter_Q_nouns, interview_Q_nouns, interview_review_nouns=[],[],[],[]

#자소서 질문 받아오기
def get_cover_letter_Q(url):
    try:
        req=requests.get('http://www.jobkorea.co.kr'+url)
        html=req.text
        soup=BeautifulSoup(html,'html.parser')

        realdata = soup.select(
        '.cont .bx ul '
        )
        for r in realdata:
            tt1= r.select('li')
            tt1=make_context(tt1)
            return tt1
    except Exception as e:
        pass
#합격 자소서 답안 받아오기
def get_cover_letter_A(url):
    try:
        req=requests.get('http://www.jobkorea.co.kr'+url)
        html=req.text
        soup=BeautifulSoup(html,'html.parser')

        realdata=soup.find_all('div',class_='tx')
        str1=make_context(realdata)
        return str1
    except Exception as e:
        pass


def make_context(arr):
    str1=''
    for t in arr:
        str1=str1+t.text
    return str1

def make_arr_to_str(arr):
    str1=''
    for t in arr:
        str1=str1+" "+t
    return str1

#직원 평균 연봉 수집하기
def get_avg_salary(url):
    req=requests.get('http://www.jobkorea.co.kr'+url)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')

    realdata = soup.find_all('div',class_="salary")
    if(realdata):
        final = realdata[0].get_text(strip=True, separator='-') 
        avg_salary.append(final.split('-')[0])
    else:
        avg_salary.append('')

#면접 질문 수집하기
def get_interview_Q(url):
    try:
        x=url.find("review")
        if x!=-1:
            req=requests.get('http://www.jobkorea.co.kr'+url)
            html=req.text
            soup=BeautifulSoup(html,'html.parser')
            ss=soup.select('.reviewQnaWrap ul li')
            temp_s=''
            temp_ss=''
            for s in ss:
                realdata = s.find_all('span',class_="tx")
        
                for i in realdata:

                    final = i.get_text(strip=True, separator='-') 

                    tmp=make_arr_to_str(twitter.nouns(final))
                    temp_ss=temp_ss+tmp
                    temp_s=temp_s+final
            interview_Q_nouns.append(temp_ss)
            interview_Q.append(temp_s)
        else:
            interview_Q.append('')
            interview_Q_nouns.append('')
    except Exception as e:
        interview_Q.append('')
        interview_Q_nouns.append('')
        pass

#면접 후기 수집하기
def get_interview_review(url):
    try:
        x=url.find("review")
        if x!=-1:
            req=requests.get('http://www.jobkorea.co.kr'+url)
            html=req.text
            soup=BeautifulSoup(html,'html.parser')
            ss=soup.select('.reviewQnaWrap ul ')
            temp_s=''
            temp_ss=''
            for s in ss:
                realdata = s.find_all('p')
                for i in realdata:
                    final = i.get_text(strip=True, separator='-') 

                    tmp=make_arr_to_str(twitter.nouns(final)) 
                    
             
                    temp_s=temp_s+final
                    temp_ss=temp_ss+tmp
            interview_review.append(temp_s)
            interview_review_nouns.append(temp_ss)
        else:
            interview_review.append('')
            interview_review_nouns.append('')
    except Exception as e:
        interview_review.append('')
        interview_review_nouns.append('')
        pass

#리스트에서 상세페이지로 들어가기
def get_main_content(url):
    time.sleep(2)
    reqq= requests.get('http://www.jobkorea.co.kr'+url)
    htmll = reqq.text
    soupp = BeautifulSoup(htmll, 'html.parser')
    result = soupp.find_all('span',class_="score")
    if result:
        final =  result[0].get_text(strip=True, separator='-') 
        final1 = result[1].get_text(strip=True, separator='-')
        final2 = result[2].get_text(strip=True, separator='-')
        final3 = result[3].get_text(strip=True, separator='-') 
        final4 = result[4].get_text(strip=True, separator='-') 
        final5 = result[5].get_text(strip=True, separator='-')
        final6 = result[6].get_text(strip=True, separator='-')
        final7 = result[7].get_text(strip=True, separator='-')
        final8 = result[8].get_text(strip=True, separator='-')
        final9 = result[9].get_text(strip=True, separator='-')         
        tmp1= final.split('-')[0]
        tmp2= final1.split('-')[0]
        tmp3= final2.split('-')[0]
        tmp4= final3.split('-')[0]
        tmp5= final4.split('-')[0]
        tmp6= final5.split('-')[0]
        tmp7= final6.split('-')[0]
        tmp8= final7.split('-')[0]
        tmp9= final8.split('-')[0]
    else:
        tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8,tmp9='','','','','','','','',''

    #회사 위치 가져오기
    try:
        result1=soupp.find_all('a', title="새창")[3]
        f=result1.get_text(strip=True, separator='-') 
        comp_location.append(f)
    except IndexError as e:
        comp_location.append('')
    

    #지원자 수 가져오기
    result4=soupp.find_all('div', class_="metrics metricsCount")
    if result4 :
        f=result4[0].get_text(strip=True, separator='-')
        candidate_num.append(f.split('-')[1])
    else:
        candidate_num.append('')

    #연봉 정보가 있는 링크 받아오기
    try:
        result5=soupp.find_all('a', class_="girBtn girBtn_3")
        link=result5[len(result5)-1].get('href')
        get_avg_salary(link)
    except IndexError as e:
        print(e)
        avg_salary.append('')

    #면접후기/질문 링크 가져오기
    result6=soupp.find_all('a', class_="linkList")

    if(result6):
        cnt=0
        for r in result6:
            link1=r.get('href')
            if link1[-1]=="5":
                cnt+=1
                get_interview_Q(link1)
                

            if link1[-1]=="3":
                cnt+=2
                get_interview_review(link1)
                
        if(cnt==1):
            interview_review.append('')
            interview_review_nouns.append('')


        elif(cnt==2):
            interview_Q.append('')
            interview_Q_nouns.append('')
   
    else:
        interview_Q.append('')
        interview_Q_nouns.append('')
        interview_review.append('')
        interview_review_nouns.append('')

    tmp_ar=''
    tmp_arr=''
    tmp11= soupp.select('.devStartlist.listArea.pAssayList ul li')
    temp2=''
    try:
        for t in tmp11:
            temp11 =t.select('.tx a')

            tmp_ar=get_cover_letter_Q(temp11[0].get('href'))
            for y in temp11:
                tmp_arr=tmp_arr+' '+get_cover_letter_A(y.get('href'))

        cover_letter_Q_nouns.append(make_arr_to_str(twitter.nouns(tmp_ar)))
        cover_letter_A_nouns.append(make_arr_to_str(twitter.nouns(tmp_arr)))
        cover_letter_Q.append(tmp_ar)
        cover_letter_A.append(tmp_arr)
    except Exception as e:
        cover_letter_Q_nouns.append('')
        cover_letter_Q.append('')
        cover_letter_A_nouns.append('')
        cover_letter_A.append('')
        pass

    try: 
        result2=soupp.find_all('dl',class_="tbList")[3]
        ff=result2.get_text(strip=True, separator='-') 
        comp_industry.append(ff.split('-')[1])
        split_list =ff.split('-')
        if len(split_list)<=12:
            if len(split_list)<=10:
                comp_member_number.append('')
                comp_spec.append('')
                comp_revenue.append('')
                comp_year.append(ff.split('-')[3])
                comp_level.append(ff.split('-')[8])
            else:
                comp_spec.append('')
                comp_revenue.append('')
                comp_member_number.append(ff.split('-')[3])
                comp_year.append(ff.split('-')[6])
                comp_level.append('') 
        
        elif ff.split('-')[12] =="매출액": #인증 대신 영업 이익만 있다면 
            comp_spec.append('')
            comp_revenue.append(ff.split('-')[13])
            comp_member_number.append(ff.split('-')[3])
            comp_year.append(ff.split('-')[6])
            comp_level.append(ff.split('-')[11]) 
        
        else:
            if len(split_list)<=14: #매출액 대신 인증만 있다면 
                comp_spec.append(ff.split('-')[13])
                comp_revenue.append('')
                comp_member_number.append(ff.split('-')[3])
                comp_year.append(ff.split('-')[6])
                comp_level.append(ff.split('-')[11]) 
        
            else: #매츨액, 인증 둘 다 있다면 
                comp_spec.append(ff.split('-')[13])
                comp_revenue.append(ff.split('-')[15])
                comp_member_number.append(ff.split('-')[3])
                comp_year.append(ff.split('-')[6])
                comp_level.append(ff.split('-')[11]) 
    except IndexError as e:
        comp_industry.append('')
        comp_member_number.append('')
        comp_spec.append('')
        comp_revenue.append('')
        comp_year.append('')
        comp_level.append('')
    

    
    
    emp_grade_score.append(tmp1)
    emp_toeic_score.append(tmp2)
    emp_ts_score.append(tmp3)
    emp_opic_score.append(tmp4)
    emp_etcL_score.append(tmp5)
    emp_license_score.append(tmp6)
    emp_otherCountry_score.append(tmp7)
    emp_intern_score.append(tmp8)
    emp_award_score.append(tmp9)

####################################################################################

try:
    for i in range(2):
        if i==0 :
            req = requests.get(urlpage)
        elif i ==1 :
            req= requests.get(urlpage2)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        aa=''
        if i==0:
            a=soup.find("span",id="TabIngCount")
            aa=a.get_text(strip=True, separator='-')
            aa=str(aa).replace("(","").replace(")","").replace(",","")

        if i==1:
            a=soup.find("span",id="TabEndCount")
            aa=a.get_text(strip=True, separator='-')
            aa=str(aa).replace("(","").replace(")","").replace(",","")

        page= int(int(aa)/40)+1
        
        for pa in range(page):

            if i==0 :

                sendpage=urlpage+str(pa)
            if i ==1 :

                sendpage=urlpage2+str(pa+1)
            data = requests.get(sendpage)
            rawdata = data.text
            parser = BeautifulSoup(rawdata, 'html.parser')

            realdata = parser.select(
            '.filterList li'
            )

            for q in realdata:

                temp1=q.select(
                    '.co .coTit .coLink'  )

                temp2=q.select(
                    '.side .day'      )
                temp3=q.select(
                    '.info .tit .link span'  )

                temp4=q.select(
                    '.info .sTit span') #dept
     
                temp5=q.select(
                    '.co .coDesc .coLyArea .btnItem .devType1000 span')
                temp6=q.select(
                    '.co .coDesc .coLyArea .btnItem .devTypeExcellent span')
                temp7=q.select(
                    '.sDesc strong')
                temp8=q.select(
                    '.sDesc span')
                temp9=q.select(
                    '.sDesc span:nth-of-type(2)')
                temp10=q.select(
                    '.info .tit .link')
                temp11=q.select( #dept2
                    '.info .sTit span:nth-of-type(2)'
                    )
                temp12=q.select( #dept3
                     '.info .sTit span:nth-of-type(3)'
                    )
                for temp in temp10:
                    link.append(temp.get('href'))
                
                name.append(temp1[0].string)
                endday.append(temp2[0].string)
                title.append(temp3[0].string)
                
                if temp4:
                    dept.append(temp4[0].string)
                else:
                    dept.append('')

                if temp5:
                    coLevel.append(temp5[0].string)
                elif temp6:
                    coLevel.append(temp6[0].string)
                else :
                    coLevel.append('')
                if temp12 :
                    dept3.append(temp12[0].string)
                    dept2.append(temp11[0].string)
                elif temp11:
                    dept2.append(temp11[0].string)
                    dept3.append('')
                else :
                    dept3.append('')
                    dept2.append('')
                career.append(temp7[0].string)
                edu.append(temp8[0].string)
                region.append(temp9[0].string)

         

        print(name)



    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('sample.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'title')
    worksheet.write('B1', 'endday')
    worksheet.write('C1', 'title')
    worksheet.write('D1', 'dept')
    worksheet.write('E1', 'dept2')
    worksheet.write('F1', 'dept3')
    worksheet.write('G1', 'coLevel')
    worksheet.write('H1', 'career')
    worksheet.write('I1', 'edu')
    worksheet.write('J1', 'region')
    worksheet.write('K1', 'comp_location')
    worksheet.write('K1', 'link')

    worksheet.write('L1', 'emp_grade_score')
    worksheet.write('M1', 'emp_toeic_score')
    worksheet.write('N1', 'emp_ts_score')
    worksheet.write('O1', 'emp_opic_score')
    worksheet.write('P1', 'emp_etcL_score')
    worksheet.write('Q1', 'emp_license_score')
    worksheet.write('R1', 'emp_otherCountry_score')
    worksheet.write('S1', 'emp_intern_score')
    worksheet.write('T1', 'emp_award_score')

    worksheet.write('U1', 'comp_industry')
    worksheet.write('V1', 'comp_member_number')
    worksheet.write('W1', 'comp_year')
    worksheet.write('X1', 'comp_level')
    worksheet.write('Y1', 'comp_spec')
    worksheet.write('Z1', 'comp_revenue')

    worksheet.write('AA1', 'cover_letter_Q')
    worksheet.write('AB1', 'cover_letter_A')

    worksheet.write('AC1', 'candidate_num')
    worksheet.write('AD1', 'avg_salary')

    worksheet.write('AE1', 'interview_Q')
    worksheet.write('AF1', 'interview_review')
    worksheet.write('AG1', 'interview_Q_nouns')
    worksheet.write('AH1', 'interview_review_nouns')
    worksheet.write('AI1', 'cover_letter_Q_nouns')
    worksheet.write('AJ1', 'cover_letter_A_nouns')



    number=0
    for ind in name:
        print(number)
        get_main_content(link[number])

        worksheet.write(number+1, 0, name[number])
        worksheet.write(number+1, 1, endday[number])
        worksheet.write(number+1, 2, title[number])
        worksheet.write(number+1, 3, dept[number])
        worksheet.write(number+1, 4, dept2[number])
        worksheet.write(number+1, 5, dept3[number])
        worksheet.write(number+1, 6, coLevel[number])
        worksheet.write(number+1, 7, career[number])
        worksheet.write(number+1, 8, edu[number])
        worksheet.write(number+1, 9, region[number])

        worksheet.write(number+1, 10, link[number])

        worksheet.write(number+1, 11, emp_grade_score[number])
        worksheet.write(number+1, 12, emp_toeic_score[number])
        worksheet.write(number+1, 13, emp_ts_score[number])
        worksheet.write(number+1, 14, emp_opic_score[number])
        worksheet.write(number+1, 15, emp_etcL_score[number])
        worksheet.write(number+1, 16, emp_license_score[number])
        worksheet.write(number+1, 17, emp_otherCountry_score[number])
        worksheet.write(number+1, 18, emp_intern_score[number])
        worksheet.write(number+1, 19, emp_award_score[number])

        worksheet.write(number+1, 20, comp_industry[number])
        worksheet.write(number+1, 21, comp_member_number[number])
        worksheet.write(number+1, 22, comp_year[number])
        worksheet.write(number+1, 23, comp_level[number])
        worksheet.write(number+1, 24, comp_spec[number])
        worksheet.write(number+1, 25, comp_revenue[number])
        worksheet.write(number+1, 26, cover_letter_Q[number])
        worksheet.write(number+1, 27, cover_letter_A[number])
        worksheet.write(number+1, 28, candidate_num[number])
        worksheet.write(number+1, 29, avg_salary[number])
        try:
            worksheet.write(number+1, 30, interview_Q[number])
        except IndexError as e:
            interview_Q.append('')
            interview_Q_nouns.append('')
            worksheet.write(number+1, 30, interview_Q[number])
        try:
            worksheet.write(number+1, 31, interview_review[number])
        except IndexError as e:
            interview_review.append('')
            interview_review_nouns.append('')
            worksheet.write(number+1, 31, interview_review[number])

        worksheet.write(number+1, 32, interview_Q_nouns[number])
        worksheet.write(number+1, 33, interview_review_nouns[number])
        worksheet.write(number+1, 34, cover_letter_Q_nouns[number])
        worksheet.write(number+1, 35, cover_letter_A_nouns[number])
        number=number+1
    workbook.close()
    
except Exception as e:
    print(e)
    workbook.close()