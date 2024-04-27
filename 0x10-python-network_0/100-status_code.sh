#!/bin/bash
# Prints the status code of a URL request
curl -s -o /dev/null -w '%{http_code}' "$1"
