#!/bin/bash
#send a request to get content-length
curl -s "$1" | wc -m
