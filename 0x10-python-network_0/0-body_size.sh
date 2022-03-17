#!/bin/bash
# Send request to URL and return size of body in bytes
curl -sD - "$1" | grep "Content-Length" | cut -d " " -f 2-
