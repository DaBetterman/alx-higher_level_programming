#!/bin/bash
# script to get the allowed methods in an server if availaible through OPTIONS http request
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'

