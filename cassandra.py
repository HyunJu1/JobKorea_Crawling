from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def parseInput(line):
  fields=line.split('\\|')
  return Row(indexs =fields[0], title =fields[1], endday =fields[2], dept =fields[3], dept2 =fields[4], dept3 =fields[5],colevel =fields[6],career =fields[7],edu  =fields[8],region =fields[9],comp_location =fields[10],link =fields[11],emp_grade_score =fields[12] ,emp_toeic_score =fields[13],emp_ts_score =fields[14],emp_opic_score =fields[15],emp_etcl_score =fields[16], emp_license_score =fields[17] ,emp_othercountry_score =fields[18],emp_intern_score =fields[19] ,emp_award_score =fields[20],comp_industry =fields[21],comp_member_number =fields[22] ,comp_year =fields[23] ,comp_level =fields[24],comp_spec =fields[25],comp_revenue =fields[26] ,cover_letter_q =fields[27],  cover_letter_a =fields[28],candidate_num =fields[29],avg_salary =fields[30],interview_q =fields[31],interview_review =fields[32],interview_q_nouns =fields[33],interview_review_nouns =fields[34],cover_letter_q_nouns =fields[35],cover_letter_a_nouns =fields[36] )

if __name__ == "__main__" :
  spark=SparkSession.builder.appName("CassandraIntegration").config("spark.cassandra.connection.host","127.0.0.1").getOrCreate()
  lines=spark.sparkContext.textFile("hdfs:///user/maria_dev/jobkorea_data.csv")
  jj=lines.map(parseInput)
  jobsDataset=spark.createDataFrame(jj)

  jobsDataset.write\
    .format("org.apache.spark.sql.cassandra")\
    .mode('append')\
    .options(table="jobs_table",keyspace="jobkorea")\
    .save()

  readUsers =spark.read\
    .format("org.apache.spark.sql.cassandra")\
    .options(table="jobs_table",keyspace="jobkorea")\
    .load()
  readUsers.createOrReplaceTempView("jobs_table")

  sqlDF= spark.sql("SELECT * FROM jobs_table")
  sqlDF.show()
  spark.stop()
