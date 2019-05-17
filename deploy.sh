#!/usr/bin/env bash

gcloud beta functions deploy cf-con --runtime python37 --entry-point main --trigger-topic cf-ps-con --timeout 540
