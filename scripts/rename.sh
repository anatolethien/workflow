#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: project name was not specified."
  exit 1
fi

title="$1"

sed -i '' "s/industrial/$title/g" README.md
sed -i '' "s/industrial/$title/g" docs/presenation.md
sed -i '' "s/industrial/$title/g" docs/report.md
