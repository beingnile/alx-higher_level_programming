#!/bin/bash
# Sends a POST request with a file passed as arg
curl -s -X POST -d @"$2" "$1"
