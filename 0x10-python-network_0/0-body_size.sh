#!/bin/bash
# read the size of url in byte(content-length)
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'