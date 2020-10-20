#!/usr/bin/python


import boto3
import logging
from datetime import date, datetime
from time import sleep
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

#REGION = os.environ["AWS_REGION"]

while True:
    #client = boto3.client('meteringmarketplace',  region_name=REGION)
    client = boto3.client('meteringmarketplace')
    utc_now = datetime.utcnow()
    try:
        response = client.meter_usage(
        ProductCode='string',
        Timestamp=utc_now,
        UsageDimension='my-dimension',
        UsageQuantity=5
        )
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        if (status_code == 200):
            logger.info("I reached MP API")
        else:
            logger.error (f"I got an error: {response}")
            break
    except ClientError as e:
        logger.error(f"I got an exception MP exception: {e}")
        break
    except Exception as e:
        logger.error(f"I got an exception: {e}")
        break
    sleep(10)