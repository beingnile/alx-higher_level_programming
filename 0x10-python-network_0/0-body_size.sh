#!/bin/bash
# Prints a response body size for passed in URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
