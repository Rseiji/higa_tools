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

