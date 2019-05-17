import json
import time
import logging
import datetime
import base64

from google.cloud import bigquery

bq = bigquery.Client()


def main(data, context):
    logging.info(data)
    logging.info(context)
    data_str = base64.b64decode(data['data']).decode()
    logging.info('received data: {}'.format(data_str))
    data_json = json.loads(data_str)

    dt_str = data_json['datetime']
    pause = int(data_json['pause'])
    bq_table_name = data_json['bq_table']
    bq_dataset_name = data_json['bq_dataset']
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')
    number = data_json['number']

    bq_data = [{
        'message_number': number,
        'message_created': dt,  # as string
        'message_upload': datetime.datetime.utcnow()  # as datetime instance,
    }]

    res = bq_insert(bq_data, bq_dataset_name, bq_table_name)
    if res:
        logging.error(res)
    time.sleep(60 * pause)


def bq_insert(data, bq_dataset_name, bq_table_name):
    bq_dataset = bq.dataset(bq_dataset_name)
    bq_table_ref = bq_dataset.table(bq_table_name)
    bq_table = bq.get_table(bq_table_ref)
    res = bq.insert_rows(bq_table, data)
    return res
