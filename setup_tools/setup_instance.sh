#!/bin/bash

printf "${LGREEN}> Installing with sudo apt-get...${NC}\n"

sudo -E apt-get -y update
sudo -E apt-get -y upgrade
sudo -E apt-get -y install tmux
sudo -E apt-get -y install htop
sudo -E apt-get -y install s3cmd

sudo -E apt-get -y install python3
sudo -E apt-get -y install python3-pip
sudo -E apt-get -y install python3-venv

sudo -E apt-get -y install git

# Installing Docker
sudo snap install docker

# Installing node
curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs
sudo apt install -y npm

# Needed for pyodbc
sudo apt-get -y install unixodbc-dev

printf "${LGREEN}>> Creating Environment...${NC}\n"
python3 -m venv $HOME/.py3env
echo "alias py3env='source $HOME/.py3env/bin/activate'" >> ~/.bashrc
echo "alias tmx='tmux new -s new_session'" >> ~/.bashrc
echo "alias jnb='py3env && jupyter notebook'" >> ~/.bashrc
echo "alias jlb='py3env && jupyter lab'" >> ~/.bashrc

# Setting aliases...
cp $HOME/coding/higa_tools/settings/terminal/bash_aliases $HOME/.bash_aliases
source ~/.bashrc

printf "${LGREEN}>> Installing Requirements...${NC}\n"
source $HOME/.py3env/bin/activate
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
pip install dask[complete]

# https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04-pt
printf "${LGREEN}>> Setting up node & npm...${NC}\n"
sudo apt update
sudo apt install nodejs
sudo apt install npm

printf "${LGREEN}>> Setting up programming environments...${NC}\n"
pip install jupyter
pip install jupyter_contrib_nbextensions

# Jupyterlab
pip install jupyterlab
pip install xeus-python notebook
jupyter contrib nbextension install --user
jupyter labextension install @jupyterlab/toc
jupyter labextension install @jupyterlab/debugger
jupyter labextension install jupyterlab-chart-editor

pip install jupyterlab-topbar       # container extension
pip install jupyterlab-topbar-text  # to install the topbar-text extension

jupyter labextension install jupyterlab-topbar-extension \
                             jupyterlab-system-monitor \
                             jupyterlab-topbar-text \
                             jupyterlab-logout \
                             jupyterlab-theme-toggle

bash $HOME/coding/higa_tools/settings/jupyter_lab/setup.sh
bash $HOME/coding/higa_tools/settings/jupyter_notebook/setup_enable.sh

# Tmux settings
bash $HOME/coding/higa_tools/settings/tmux/setup.sh
