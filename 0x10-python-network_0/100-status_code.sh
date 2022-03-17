#!/bin/bash
# Send request to URL passed as argument and return the status code
curl -so /dev/null -w "%{http_code}" "$1"
