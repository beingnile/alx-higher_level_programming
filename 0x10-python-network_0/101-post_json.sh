#!/bin/bash
# Send a JSON POST request to URL passed as argument
curl -sLH "content-type:application/json" -d @"$2" -X POST "$1"
