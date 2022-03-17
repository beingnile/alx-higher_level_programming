#!/bin/bash
# Send POST request to URL passed as argument
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
