#!/bin/bash

# URL of the website
URL="http://localhost:8080"

# Make a request to the website and store the result
response=$(curl -s $URL)

# Check if the response contains the word "Welcome"
if echo "$response" | grep -q "Welcome"; then
    echo "Homepage test passed."
    exit 0
else
    echo "Homepage test failed."
    exit 1
fi
