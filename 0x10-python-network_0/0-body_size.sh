#!/bin/bash
# Send request to URL and return size of body in bytes
curl -s "$1" | wc -c
