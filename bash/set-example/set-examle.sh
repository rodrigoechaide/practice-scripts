#!/bin/bash

#More info
#https://www.tldp.org/LDP/abs/html/options.html

#Abort script at first error, when a command exits with non-zero status (except in until or while loops, if-tests, list constructs)
set -e

# Echoes all commands before executing.
set -o verbose

ls -l /home/rodrigox
du -sh /home/rodrigo
