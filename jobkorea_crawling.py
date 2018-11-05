import xlsxwriter
import requests
from bs4 import BeautifulSoup
import time

req = requests.get('http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page=')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
page = soup.select(
    '.tplPagination > ul > li'
    )
name,endday,title=[],[],[]
dept= []
coLevel= []
career= []
edu= []
region= []
link= []
urlpage="http://www.jobkorea.co.kr/starter/?schLocal=&schPart=&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt=&Page="
emp_grade_score=[] #학점 
emp_toeic_score=[]
emp_ts_score=[]
emp_opic_score=[]
emp_etcL_score=[] #외국어(기타)
emp_license_score=[] #자격증개수 
emp_otherCountry_score=[]  #해외경험
emp_intern_score=[]
emp_award_score=[]
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

    emp_grade_score.append(tmp1)
    emp_toeic_score.append(tmp2)
    emp_ts_score.append(tmp3)
    emp_opic_score.append(tmp4)
    emp_etcL_score.append(tmp5)
    emp_license_score.append(tmp6)
    emp_otherCountry_score.append(tmp7)
    emp_intern_score.append(tmp8)
    emp_award_score.append(tmp9)

    print(tmp4)

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
            '.info .sTit span')
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
        career.append(temp7[0].string)
        edu.append(temp8[0].string)
        region.append(temp9[0].string)

     

print(name)

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', '기업명')
worksheet.write('B1', '마감일자')
worksheet.write('C1', '제목')
worksheet.write('D1', '직무')
worksheet.write('E1', 'c1')
worksheet.write('F1', 'c2')
worksheet.write('G1', 'c3')
worksheet.write('H1', 'c4')
number=0
for ind in name:
    # Write some numbers, with row/column notation.
    worksheet.write(number+1, 0, name[number])
    worksheet.write(number+1, 1, endday[number])
    worksheet.write(number+1, 2, title[number])
    worksheet.write(number+1, 3, dept[number])
    worksheet.write(number+1, 4, coLevel[number])
    worksheet.write(number+1, 5, career[number])
    worksheet.write(number+1, 6, edu[number])
    worksheet.write(number+1, 7, region[number])
    #worksheet.write(number+1, 8, num[number])
    get_main_content(link[number])
    #worksheet.write(number+1, 9, emp_toeic_score[number])
    number=number+1

workbook.close()