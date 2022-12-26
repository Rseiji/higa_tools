#!/bin/bash

## Brave Installation
# Source: https://brave.com/linux/
echo "Installing brave..."

sudo apt install curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser


## Okular Installation
# Source: https://linuxconfig.org/okular-pdf-viewer-installation-on-ubuntu-20-04-focal-fossa
echo "Installing okular..."
sudo apt install okular


## Spotify Installation
# Source: https://www.spotify.com/br/download/linux/
echo "Installing Spotify..."
curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client


## Google Chrome Installation
echo "Installing Google Chrome..."
sudo apt-get update
sudo apt-get install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo rm google-chrome-stable_current_amd64.deb


## Vscode Installation
echo "Installing VsCode..."
sudo apt-get update
sudo apt-get install code
sudo apt-get clean
bash $HOME/coding/higa_tools/settings/vscode/setup.sh


## Zoom Installation
echo "Installing Zoom..."
sudo apt update
wget https://zoom.us/client/latest/zoom_amd64.deb
sudo apt install ./zoom_amd64.deb
rm zoom_amd64.deb


## Postman
echo "Installing Postman..."
wget https://dl.pstmn.io/download/latest/linux64
unzip linux64
sudo apt-get install ./Postman-linux-x64-6.7.2.tar.gz
sudo rm linux64
sudo rm Postman-linux-x64-6.7.2.tar.gz


## VLC Media Player
sudo apt update
sudo apt install vlc

# Check if VLC was successfully installed
if [ -f "/usr/bin/vlc" ]; then
    echo "VLC was successfully installed!"
else
    echo "VLC installation failed!"
fi


## Sublime
# Check for root privileges
if [ "$(whoami)" != "root" ]; then
  echo "You must run this script with root privileges."
  exit 1
fi

# Download Sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | tee /etc/apt/sources.list.d/sublime-text.list

# Update repository
sudo apt-get update

# Install Sublime
sudo apt-get install -y sublime-text

echo "Sublime is now installed!"
