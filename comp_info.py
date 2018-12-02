import xlsxwriter
import requests
from bs4 import BeautifulSoup
import time
import re


urlpage2="http://www.jobkorea.co.kr/Salary/?act=s&el=salarySearchCompany&coPage="

name=[]
a,b,c,d=[],[],[],[]

try:
    req= requests.get(urlpage2)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # a=soup.find("div",_class="total")
    # aa=a.get_text(strip=True, separator='-')
    # aa=str(aa).replace("총","").replace("건","").replace(",","")

    # page= int(int(aa)/40)+1
    
    for pa in range(800 ,1500):
#14769
        sendpage=urlpage2+str(pa+1)
        data = requests.get(sendpage)
        rawdata = data.text
        parser = BeautifulSoup(rawdata, 'html.parser')



        realdata = parser.select(
        '#listCompany li'
        )
        #print(realdata)
        for q in realdata:

            temp1=q.select(
                '.headers .text'  )

            temp2=q.select(
                '.summary div:nth-of-type(1)'      )
            temp3=q.select(
                '.summary div:nth-of-type(2)')

            temp4=q.select(
                '.summary div:nth-of-type(3)') #dept
 
            temp5=q.select(
                '.salary .inner strong' )


            name.append(temp1[0].string)

            if(temp2):
                a.append(temp2[0].string)
            else:
                a.append('')
            if(temp3):
                b.append(temp3[0].string)
            else:
                b.append('')
            if(temp4):

                c.append(temp4[0].string)
            else:
                c.append('')
            d.append(temp5[0].string)
 




    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('info.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})


    number=0
    for ind in name:
        #print(number)

        worksheet.write(number+1, 0, name[number])
        worksheet.write(number+1, 1, a[number])
        worksheet.write(number+1, 2, b[number])
        worksheet.write(number+1, 3, c[number])
        worksheet.write(number+1, 4, d[number])

        number=number+1

    workbook.close()
except Exception as e:
    print(e)
    workbook.close()