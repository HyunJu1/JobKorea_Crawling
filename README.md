
# JobKorea사이트 데이터를 활용한 Hadoop 기반 NLP System 개발
####	프로젝트 기간 : 2018년 11월 5일 ~ 2018년 12월 12일


####	데이터 수집:
- 언어  : Python( 3.6 버전 사용)
- Editor : Sublime Text
- 사용 모듈 :
	1.	xlsxwriter ,
	2.	requests,
	3.	BeautifulSoup,
	4.	konlpy.tag,
	5.	konly.utils 	
    소스코드:  joblorea_crawling.py
	결과 파일:  jobkorea_data.xlsx


####	데이터 전처리 :
- 언어: Python(3.6 버전 사용)
- Editor: Sublime Text
- 사용 모듈:
	 1.	Numpy
	 2.	 pandas
	 3.	 matplotlib
	소스코드:  data_preprocessing.py
	결과 파일 :  jobkorea_data1.csv (GitHub에 올리기에는 용량 제한에 걸려 올리지 못하였습니다.)  
 	파일 크기: 207MB,  ROW: 25760개, COLUMN: 38개


####	데이터 분석:
- 시스템 아키텍쳐

![bigdata](https://user-images.githubusercontent.com/17667687/52959851-a83d7d80-33da-11e9-89b3-3f18fb1c4295.png)

- 개발 환경 :

    Hadoop Data Platform Sandbox (HDP Sandbox)
		Hadoop Cluster
		Yarn

- 활용:
	1.	Hadoop,
	2.	HDFS ,
	3.	Hive
	4.	MySQL
	5.	Sqoop,
	6.	Zeppelin


	### > 2019.04 추가 내용

	- AWS Lambda Function & AWS CloudWatch + AWS RDS 를 활용한 Serverless 자동 크롤링 시스템 구축 완료.

![bigdata](https://user-images.githubusercontent.com/17667687/56209605-f09db280-608e-11e9-8e31-d1f169582ffc.PNG)
