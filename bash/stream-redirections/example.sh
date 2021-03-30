#!/bin/bash

# https://linuxize.com/post/bash-redirect-stderr-stdout/

# Redirecting stdout

echo "Redirecting stdout to file" > file.txt
echo "Redirecting stdout to /dev/null" 1> /dev/null

# Redirecting stderr

echo "Redirecting stderr to file" 2> file.txt
echo "Redirecting stderr to /dev/null" 2> /dev/null

# Redirecting stdout and stderr to different files

echo "Redirecting stderr and stdout to different files" 1> output.log 2> error.log

# Redirecting stderr to stdout

echo "Redirecting stderr to stdout and then stdout to a single file" &> output.log
echo "Redirecting stderr to stdout and then stdout to a single file" > output.log 2>&1