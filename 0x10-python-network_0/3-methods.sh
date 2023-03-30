#!/bin/bash
#display all HTTP method
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-