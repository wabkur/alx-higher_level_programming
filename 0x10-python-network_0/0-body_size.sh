#!/bin/bash

# Get the URL from the command line argument
url=$1

curl -s "$1" | wc -c
