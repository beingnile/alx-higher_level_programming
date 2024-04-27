#!/bin/bash
# Sends a GET request to passed URL argument
curl -o /dev/null -w "%{http_code}" -sLf "$1" | grep -q '200' && curl -sLf "$1"
