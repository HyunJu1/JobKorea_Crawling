
users = LOAD '/user/maria_dev/data/jobkorea_data1.csv' USING PigStorage('|')
 AS (index:int, name:chararray, 
 endday:date,title:chararray,dept:chararray,dept2:chararray,dept3:chararray,
 coLevel:chararray,career:chararray,edu:chararray,region:chararray,link:chararray,
 emp_grade_score:float,
emp_toeic_score:int,
emp_ts_score:chararray,
emp_opic_score:chararray,
emp_etcL_score:float,
emp_license_score:float,
emp_otherCountry_score:float,
emp_intern_score:float,
emp_award_score:float,
 comp_industry:chararray,comp_member_number:int,comp_year:int, comp_level:chararray,
 comp_spec:chararray,comp_revenue:int,
 cover_letter_Q:chararray,cover_letter_A:chararray,candidate_num:int, avg_salary:int,
 interview_Q:chararray,interview_review:chararray,
 cover_letter_A_nouns:chararray, cover_letter_Q_nouns:chararray, interview_Q_nouns:chararray, 
 interview_review_nouns:chararray);

STORE users INTO 'hbase://jobkorea'
USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('jobkorea:index, jobkorea:name, 
 jobkorea:endday,jobkorea:title,jobkorea:dept,jobkorea:dept2,jobkorea:dept3,
 jobkorea:coLevel,jobkorea:career,jobkorea:edu,jobkorea:region,jobkorea:link,
 jobkorea:emp_grade_score,
jobkorea:emp_toeic_score,
jobkorea:emp_ts_score,
jobkorea:emp_opic_score,
jobkorea:emp_etcL_score,
jobkorea:emp_license_score,
jobkorea:emp_otherCountry_score,
jobkorea:emp_intern_score,
jobkorea:emp_award_score,
 jobkorea:comp_industry,jobkorea:comp_member_number,jobkorea:comp_year, jobkorea:comp_level,
 jobkorea:comp_spec,jobkorea:comp_revenue,
 jobkorea:cover_letter_Q,jobkorea:cover_letter_A,jobkorea:candidate_num, jobkorea:avg_salary,
 jobkorea:interview_Q,jobkorea:interview_review,
 jobkorea:cover_letter_A_nouns, jobkorea:cover_letter_Q_nouns, jobkorea:interview_Q_nouns, 
 jobkorea:interview_review_nouns');