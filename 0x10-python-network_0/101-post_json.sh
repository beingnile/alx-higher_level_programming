#!/bin/bash
# Sends a POST request with a file passed as arg
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
