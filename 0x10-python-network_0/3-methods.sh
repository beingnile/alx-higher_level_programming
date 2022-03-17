#!/bin/bash
# Display the HTTP methods the server will accept
curl -sD - "$1" | grep "Allow" | cut -d " " -f 2
