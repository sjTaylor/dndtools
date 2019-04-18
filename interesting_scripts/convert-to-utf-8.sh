#!/bin/bash

# see https://stackoverflow.com/questions/805418/how-to-find-encoding-of-a-file-in-unix-via-scripts
# and https://stackoverflow.com/questions/64860/best-way-to-convert-text-files-between-character-sets

# I think this is what I did, but the command wasn't left in my ~/.bash_history
recode iso-8859-1..utf8 dumped/*.csv
