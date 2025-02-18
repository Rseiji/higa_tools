#!bin/bash

# Ref: https://medium.com/@gutoinfo.ribeiro/instalando-e-configurando-o-zsh-no-ubuntu-20-04-4ef8a2499ed5
sudo apt update
sudo apt install zsh -y
sudo usermod -s /usr/bin/zsh $(whoami)
sudo apt install zsh-theme-powerlevel9k
echo "source /usr/share/powerlevel9k/powerlevel9k.zsh-theme" >> ~/.zshrc
sudo apt install zsh-syntax-highlighting
echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
sudo apt install git
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
echo "source /usr/share/powerlevel9k/powerlevel9k.zsh-theme" >> ~/.zshrc
echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
# ls .oh-my-zsh/plugins

# zsh autosuggestions
# Ref: https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md
mkdir $HOME/.zsh
cd .zsh
git clone https://github.com/zsh-users/zsh-autosuggestions
echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc

# Include Aliases
echo "source ~/higa_tools/settings/bash_aliases" >> ~/.zshrc
source ~/.zshrc
