#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: project name was not specified."
  exit 1
fi

endpoint="$1"

filename=$(basename "$endpoint")

curl -o "downloads/$filename" "$endpoint"
