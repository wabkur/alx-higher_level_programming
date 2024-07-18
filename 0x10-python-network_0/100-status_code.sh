#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only status code of a response.
curl -so /dev/null -w "%{http_code}" "$1"
