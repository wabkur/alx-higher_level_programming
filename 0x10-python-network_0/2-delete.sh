#!/bin/bash
# A script that sends a DELETED request to the URL passed.
curl -s "$1" -X DELETE
