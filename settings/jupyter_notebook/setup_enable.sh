#!/bin/bash

# Setup to enable jupyter notebook extensions.
# https://linuxhint.com/read_file_line_by_line_bash/
# https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html

filename='jupyter_notebook_extensions.txt'

while read line; do
    echo "Validating line " $line
    jupyter nbextension enable $line
done < $filename

# Manually installing snippets extension, due to some conflicts
# https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/snippets_menu/readme.html#:%7E:text=Sometimes%2C%20the%20menu,the%20real%20problem.
git clone https://github.com/moble/jupyter_boilerplate
jupyter nbextension install jupyter_boilerplate --user
jupyter nbextension enable jupyter_boilerplate/main
sudo rm -r jupyter_boilerplate
