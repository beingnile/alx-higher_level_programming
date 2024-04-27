#!/bin/bash
# Prints allowed methods for a URL
curl -si "$1" | grep -i Allow: | awk -F": " '{print $2}'
