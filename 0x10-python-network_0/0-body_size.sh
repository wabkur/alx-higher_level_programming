#!/bin/bash
#send a GET request to the url specified and print the size of respond body to stdout
curl -sI "$1" | grep -i
