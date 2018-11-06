import xlsxwriter
import requests
from bs4 import BeautifulSoup
import time
import re
urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=4&schWork=2&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="
#urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="
#urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=6&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="
req = requests.get(urlpage)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
page = soup.select(
    '.tplPagination > ul > li'
    )
name,endday,title,dept,dept2,dept3,coLevel,career,edu,region,link,comp_location=[],[],[],[],[],[],[],[],[],[],[],[]


emp_grade_score=[] #학점 
emp_toeic_score=[]
emp_ts_score=[]
emp_opic_score=[]
emp_etcL_score=[] #외국어(기타)
emp_license_score=[] #자격증개수 
emp_otherCountry_score=[]  #해외경험
emp_intern_score=[]
emp_award_score=[]

comp_industry,comp_member_number,comp_year, comp_level, comp_spec,comp_revenue=[],[],[],[],[],[]

cover_letter_Q,cover_letter_A=[],[]

def get_cover_letter_Q(url):
    time.sleep(2)
    print('여기까지 옴'+url)
    req=requests.get('http://www.jobkorea.co.kr'+url)
    time.sleep(2)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')

    realdata = soup.select(
    '.cont .bx ul '
    )
    for r in realdata:
        tt1= r.select('li')
        tt1=make_context(tt1)
        return tt1

def get_cover_letter_A(url):
    time.sleep(2)
    print('여기까지 옴22'+url)
    req=requests.get('http://www.jobkorea.co.kr'+url)
    time.sleep(2)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')

    realdata=soup.find_all('div',class_='tx')
    str1=make_context(realdata)
    return str1
    # realdata = soup.select(
    # '.show .tx'
    # )
    # s=''
    # for r in realdata:
    #     s=s+r.text
    # return s

def make_context(arr):
    str1=''
    for t in arr:
        str1=str1+t.text
    return str1


def get_main_content(url):
    print(url)
    time.sleep(2)
    reqq= requests.get('http://www.jobkorea.co.kr'+url)
    time.sleep(2)
    htmll = reqq.text
    soupp = BeautifulSoup(htmll, 'html.parser')
    result = soupp.find_all('span',class_="score")
    if result:
        final = result[0].get_text(strip=True, separator='-') 
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

    result1=soupp.find_all('a', title="새창")[3]
    f=result1.get_text(strip=True, separator='-') 
    comp_location.append(f)

    tmp_ar=''
    tmp_arr=''
    tmp11= soupp.select('.devStartlist.listArea.pAssayList ul li')
    temp2=''
    for t in tmp11:
        temp11 =t.select('.tx a')

        tmp_ar=get_cover_letter_Q(temp11[0].get('href'))
        for y in temp11:
            print(y)
            tmp_arr=tmp_arr+'/'+get_cover_letter_A(y.get('href'))
    print('tmp_ar:'+tmp_ar)
    print('tmp_arr:'+tmp_arr)
    cover_letter_Q.append(tmp_ar)
    cover_letter_A.append(tmp_arr)
    result2=soupp.find_all('dl',class_="tbList")[3]
    ff=result2.get_text(strip=True, separator='-') 



    comp_industry.append(ff.split('-')[1])
    comp_member_number.append(ff.split('-')[3])
    comp_year.append(ff.split('-')[6])
    comp_level.append(ff.split('-')[11]) 
    



    split_list =ff.split('-')
    if len(split_list)<=12:
        comp_spec.append('')
        comp_revenue.append('')
    elif ff.split('-')[12] =="매출액": #인증 대신 영업 이익만 있다면 
        comp_spec.append('')
        comp_revenue.append(ff.split('-')[13])
    else:
        if len(split_list)<=14: #매출액 대신 인증만 있다면 
            comp_spec.append(ff.split('-')[13])
            comp_revenue.append('')
        else: #매츨액, 인증 둘 다 있다면 
            comp_spec.append(ff.split('-')[13])
            comp_revenue.append(ff.split('-')[15])

 



    emp_grade_score.append(tmp1)
    emp_toeic_score.append(tmp2)
    emp_ts_score.append(tmp3)
    emp_opic_score.append(tmp4)
    emp_etcL_score.append(tmp5)
    emp_license_score.append(tmp6)
    emp_otherCountry_score.append(tmp7)
    emp_intern_score.append(tmp8)
    emp_award_score.append(tmp9)

for pa in page:
    sendpage=urlpage+str(pa.text)
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
        dept.append(temp4[0].string)
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
worksheet.write('A1', '회사 이름')
worksheet.write('B1', '지원서 마감일자')
worksheet.write('C1', '제목')
worksheet.write('D1', '직무')
worksheet.write('E1', '직무2')
worksheet.write('F1', '직무3')
worksheet.write('G1', '기업스펙')
worksheet.write('H1', '요구 경력')
worksheet.write('I1', '요구 학력')
worksheet.write('J1', '지역')
worksheet.write('K1', '상세 지역')
worksheet.write('L1', '상세페이지 링크')

worksheet.write('M1', '합격자 학점')
worksheet.write('N1', '합격자 토익')
worksheet.write('O1', '합격자 토익스피킹')
worksheet.write('P1', '합격자 오픽')
worksheet.write('Q1', '합격자 외국어(기타)')
worksheet.write('R1', '합격자 자격증개수')
worksheet.write('S1', '합격자 해외경험')
worksheet.write('T1', '합격자 인턴')
worksheet.write('U1', '합격자 수상횟수')

worksheet.write('V1', '회사 산업분야')
worksheet.write('W1', '회사 직원 수')
worksheet.write('X1', '회사 설립년도')
worksheet.write('Y1', '회사 규모')
worksheet.write('Z1', '회사 스펙')
worksheet.write('AA1', '회사 영업이익')

worksheet.write('AB1', '자소서 질문')
worksheet.write('AC1', '합격 자소서 답안')
number=0
for ind in name:
    # Write some numbers, with row/column notation.
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
    get_main_content(link[number])
    worksheet.write(number+1, 10, comp_location[number])
    worksheet.write(number+1, 11, link[number])

    worksheet.write(number+1, 12, emp_grade_score[number])
    worksheet.write(number+1, 13, emp_toeic_score[number])
    worksheet.write(number+1, 14, emp_ts_score[number])
    worksheet.write(number+1, 15, emp_opic_score[number])
    worksheet.write(number+1, 16, emp_etcL_score[number])
    worksheet.write(number+1, 17, emp_license_score[number])
    worksheet.write(number+1, 18, emp_otherCountry_score[number])
    worksheet.write(number+1, 19, emp_intern_score[number])
    worksheet.write(number+1, 20, emp_award_score[number])

    worksheet.write(number+1, 21, comp_industry[number])
    worksheet.write(number+1, 22, comp_member_number[number])
    worksheet.write(number+1, 23, comp_year[number])
    worksheet.write(number+1, 24, comp_level[number])
    worksheet.write(number+1, 25, comp_spec[number])
    worksheet.write(number+1, 26, comp_revenue[number])
    worksheet.write(number+1, 27, cover_letter_Q[number])
    worksheet.write(number+1, 28, cover_letter_A[number])
    number=number+1

workbook.close()