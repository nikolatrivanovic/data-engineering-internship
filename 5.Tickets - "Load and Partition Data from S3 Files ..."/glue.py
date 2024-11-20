import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1732010003039 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bucket-14-11-nt-v2/sensor/Levi9 NineAir Belgrade/"], "recurse": True}, transformation_ctx="AmazonS3_node1732010003039")

# Script generated for node Amazon S3
AmazonS3_node1732010091756 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1732010003039, connection_type="s3", format="csv", connection_options={"path": "s3://processed-data-levi9-nt/sensor/", "compression": "snappy", "partitionKeys": ["time_nano"]}, transformation_ctx="AmazonS3_node1732010091756")

job.commit()