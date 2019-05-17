from google.cloud import bigquery

from settings import BQ_DATASET, BQ_TABLE

bq = bigquery.Client()

schema_fields = [
    bigquery.SchemaField('message_number', 'INTEGER'),
    bigquery.SchemaField('message_created', 'DATETIME'),
    bigquery.SchemaField('message_upload', 'DATETIME')
]


def create_table(table_name):
    dataset_ref = bq.dataset(BQ_DATASET)
    bq.create_dataset(dataset_ref, exists_ok=True)
    table_ref = dataset_ref.table(table_name)
    table = bigquery.Table(table_ref, schema=schema_fields)
    bq.create_table(table, exists_ok=True)


def delete_table(table_name):
    dataset_ref = bq.dataset(BQ_DATASET)
    table_ref = dataset_ref.table(table_name)
    bq.delete_table(table_ref, not_found_ok=True)


if __name__ == '__main__':
    table_name = BQ_TABLE
    create_table(table_name)
