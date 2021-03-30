#!/bin/bash

# More info: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html

# Abort script at first error, when a command exits with non-zero status (except in until or while loops, if-tests, list constructs)
set -e

# Echoes all commands before executing. set -v is equivalent
set -o verbose

ls -l .
du -sh .

# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
# An error message will be written to the standard error, and a non-interactive shell will exit.
set -u

# echo $NON_EXISTENT_VAR
echo "Hola"


# Change back -ue option
set +eu
echo $NON_EXISTENT_VAR
ehco "Hola"
echo "Hola"

# https://unix.stackexchange.com/questions/308260/what-does-set-do-in-this-dockerfile-entrypoint
# https://stackoverflow.com/questions/20088290/whats-set-progname-means-in-shell-script/20088379

# The set command (when not setting options) sets the positional parameters eg
set a b c

echo $1
echo $2
echo $3

# The -- is the standard "don't treat anything following this as an option"
# The "$@" are all the existing position paramters.
# So the sequence: set -- haproxy "$@"
# Will put the word haproxy in front of $1 $2 etc.

echo $1,$2,$3
set -- haproxy "$@"
echo $1,$2,$3,$4

# The -- is a bash built-in as well as something a lot of unix commands use to denote the end of command options. 
# So if you have something like:

grep -- -v file

# the -v won't be interpreted as a grep option, but a parameter (so you can grep for -v)
