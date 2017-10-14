# chessReinforcementLearning
Investigating searching algorithms with reinforcement learning trained evaluator fuctions.

Version control and backup for code written for University of Cambridge Computer Science Tripos Part II Dissertation Project.

Based off the amazing Giraffe engine by Matthew Lai.

## How to build Giraffe

```
sudo apt-get install mercurial
hg clone https://bitbucket.org/waterreaction/giraffe
cd giraffe
```
Install Lua
```
curl -R -O http://www.lua.org/ftp/lua-5.3.4.tar.gz
tar zxf lua-5.3.4.tar.gz
cd lua-5.3.4
```
Install Torch
```
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch; bash install-deps;
./install.sh
source ~/.bashrc
```
Then make giraffe
```
make
```

## Food for thought

* Look at Slonik
* Huber loss rather than L1 loss
* Komodo most powerful chess engine?
* David Silver, Meep. Uses TreeStrap and Linear models
* Universal Chess Interface, GUI: Scid, PC, Chessbase
* Magic numbers
