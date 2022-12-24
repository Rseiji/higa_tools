#!/bin/bash

# Setup to enable jupyter notebook extensions.
# https://linuxhint.com/read_file_line_by_line_bash/
# https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html

filename='jupyter_notebook_extensions.txt'

while read line; do
    echo "Validating line " $line
    jupyter nbextension enable $line
done < $filename
