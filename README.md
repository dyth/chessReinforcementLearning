# Deep Reinforcement Learning for Chess
or Combining Function Approximation from Reinforcement Learning with Knowledge Engineering Algorithms in the context of Chess

Investigating searching algorithms with reinforcement learning trained evaluator fuctions.

## Interesting papers

Giraffe: Deep Reinforcement Learning in Chess: https://arxiv.org/abs/1509.01549
Introduction to Reinforcement Learning: https://arxiv.org/pdf/1701.07274v5.pdf 
Python Deep Learning library: http://pytorch.org
Considerations: https://chessprogramming.wikispaces.com/Board+Representation 

Version control and backup for code written for University of Cambridge Computer Science Tripos Part II Dissertation Project.

Based off the amazing Giraffe engine by Matthew Lai.

## Play against Giraffe
```
sudo apt-get install xboard
xboard
```
then on the GUI, under `engine > Edit Engine List ...` add the line `"<path/to/root/giraffe/directory>" -fd "<path/to/root/giraffe/directory>/giraffe"`


## Compiling Giraffe from Source

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
cd ~/torch
bash install-deps
./install.sh
source ~/.bashrc
```
Then make giraffe
```
make
```

## Train Giraffe
1. [Download, extract, rename to `ccrl.fen`](https://bitbucket.org/waterreaction/giraffe/downloads/ccrl4040_shuffled_5M.epd.gz)
2. [Download](https://bitbucket.org/waterreaction/giraffe/downloads/sts.epd)
3. Move all into root of giraffe
3. Run `nproc` to find the number of cores
4. `OMP_NUM_THREADS=<number returned by nproc> ./giraffe tdl ccrl.fen sts.epd`

## Food for thought

* Look at Slonik
* Huber loss rather than L1 loss
* Komodo most powerful chess engine?
* David Silver, Meep. Uses TreeStrap and Linear models
* Universal Chess Interface, GUI: Scid, PC, Chessbase
* Magic numbers
* Investigate / implement MTD(bi)
