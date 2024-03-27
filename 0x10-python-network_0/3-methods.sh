#!/bin/bash
# script to get the allowed methods in an server if availaible through OPTIONS http request
curl -s -i -X OPTIONS "$1" | grep "Allow:" | awk '{ print $2 }'
