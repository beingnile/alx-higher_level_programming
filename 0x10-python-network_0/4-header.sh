#!/bin/bash
# Sends a GET request with custom header content
curl -s -H "X-School-User-Id: 98" "$1"
