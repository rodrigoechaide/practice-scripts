#!/bin/bash

# Grep WORD inside TEXT string with -q (quiet) option

WORD="Hello"
TEXT="Hello World"
grep -q "$WORD" <<< "$TEXT"
grep "$WORD" <<< "$TEXT"