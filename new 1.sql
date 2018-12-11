CREATE TABLE `jobkorea`(
  `index` int, 
  `name` string, 
  `endday` date, 
  `title` string, 
  `dept` string, 
  `dept2` string, 
  `dept3` string, 
  `colevel` string, 
  `career` string, 
  `edu` string, 
  `region` string, 
  `link` string, 
  `emp_grade_score` float, 
  `emp_toeic_score` int, 
  `emp_ts_score` string, 
  `emp_opic_score` string, 
  `emp_etcl_score` float, 
  `emp_license_score` float, 
  `emp_othercountry_score` float, 
  `emp_intern_score` float, 
  `emp_award_score` float, 
  `comp_industry` string, 
  `comp_member_number` int, 
  `comp_year` int, 
  `comp_level` string, 
  `comp_spec` string, 
  `comp_revenue` int, 
  `cover_letter_q` string, 
  `cover_letter_a` string, 
  `candidate_num` int, 
  `avg_salary` int, 
  `interview_q` string, 
  `interview_review` string, 
  `interview_q_nouns` string, 
  `interview_review_nouns` string, 
  `cover_letter_q_nouns` string, 
  `cover_letter_a_nouns` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.orc.OrcSerde' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
  'hdfs://sandbox-hdp.hortonworks.com:8020/apps/hive/warehouse/jobkorea'
TBLPROPERTIES (
  'last_modified_by'='admin', 
  'last_modified_time'='1544523049', 
  'numFiles'='13', 
  'numRows'='268979', 
  'rawDataSize'='195957885', 
  'totalSize'='19689344', 
  'transient_lastDdlTime'='1544523049')
