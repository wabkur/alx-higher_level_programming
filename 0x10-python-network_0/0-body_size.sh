#!/bin/bash
#send request to check for content-length
curl -s "$1" | wc -m
