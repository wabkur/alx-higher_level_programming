#!/bin/bash

# Get the URL from the command line argument
url=$1

# Send a request to the URL and get the size of the response body
size=$(curl -s $url | wc -c)

# Display the size of the response body
echo "The size of the response body is: $size bytes"

