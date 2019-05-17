# Cloud Functions triggered by PubSub message

example of process where Google Cloud Function is triggered by PubSub message.   
Cloud Functions writes data into BigQuery and than waits for a few minutes (depending on the value in the message).  
Idea is to explore possibility to use CFs as async background workers for longer duration tasks, that's why artificial 
waiting is done in function.

## setup up
0. `settings.py` - set varibales

1. in `main.py` - file for Cloud Function

2. `deploy.sh` - deploys Cloud function

3. `create_bq_table.py` - creates BigQuery table

4. `ps_publish.py` - use to publish messages to PubSub

## Problem
although it's known that PubSub has at least once delivery rule, for some cases there is high number of duplicates 
not sure why