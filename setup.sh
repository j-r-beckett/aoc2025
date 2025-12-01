#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <day>" >&2
    exit 1
fi

day=$1

if [ -z "$AOC_TOKEN" ]; then
    echo "Error: AOC_TOKEN environment variable is not set" >&2
    exit 1
fi

mkdir -p inputs
mkdir -p solutions

curl -s -f -b "session=$AOC_TOKEN" "https://adventofcode.com/2025/day/$day/input" -o "inputs/$day.txt"

sed "s/{{day}}/$day/g" template.py > "solutions/$day.py"

echo "Created inputs/$day.txt and solutions/$day.py"
