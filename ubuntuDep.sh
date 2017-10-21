#!/bin/sh

echo "Install xboard, mercurial and git"
sudo apt-get install xboard mercurial git

echo "Install Lua"
curl -R -O http://www.lua.org/ftp/lua-5.3.4.tar.gz
tar zxf lua-5.3.4.tar.gz
cd lua-5.3.4

echo "Install torch"
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch
bash install-deps
./install.sh
source ~/.bashrc
