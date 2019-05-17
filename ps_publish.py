import time
import json
import datetime
from google.cloud import pubsub

from settings import PUBSUB_TOPIC, GCP_PROJECT, BQ_TABLE, BQ_DATASET

PAUSE = 4  # PAUSE in minutes

topic = f'projects/{GCP_PROJECT}/topics/{PUBSUB_TOPIC}'

publisher = pubsub.PublisherClient()

if __name__ == '__main__':
    c = 0
    limit = 100  # number of messages
    while c < limit:
        now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        msg = {
            'number': c,
            'datetime': now,
            'bq_table': BQ_TABLE,
            'bq_dataset': BQ_DATASET,
            'pause': PAUSE
        }
        r = publisher.publish(topic, json.dumps(msg).encode())
        x = r.result()
        # print(x)
        print(c)
        c += 1
        time.sleep(1)
