#!/bin/bash

# https://en.wikipedia.org/wiki/Here_document#Unix_shells
# https://stackoverflow.com/questions/2500436/how-does-cat-eof-work-in-bash

LANG=C tr a-z A-Z << END_TEXT
one two three
four five six
END_TEXT
