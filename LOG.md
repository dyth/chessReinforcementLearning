#### 2017.10.17

* Giraffe has project file in repository: `.sublime_*`.
* Install Sublime Text to match IDEs

#### 2017.10.19

* Install StarUML to assist reverse engineering

```
sudo dpkg -i libgcrypt11_1.5.3-2ubuntu4.2_amd64.deb
sudo dpkg -i StarUML-v2.8.0-64-bit.deb 
```
* StarUML did not generate relational UML, so install BoUML

```
echo "deb http://www.bouml.fr/apt/xenial xenial free" | sudo tee -a /etc/apt/sources.list 
sudo apt-get update
echo "deb http://bouml.free.fr/apt/xenial xenial free" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install bouml
```

#### 2017.10.17

* Install Git-Hg to interface with Giraffe on Mercurial
* convert giraffe from .hg to .git
```
sudo apt install hg-fast-export
git-hg clone --force https://bitbucket.org/waterreaction/giraffe
mv .hgignore .gitignore
```
* then add to repository. Unfortunately, `rm -rf .git` had to be called because it contained large files exceeding github's limit, negating any advantage of using git-hg!

### 2017.10.29

* See architecture

```
th

require 'nn'
require 'SlicedParallel.lua'
require 'optnet'
a = torch.load('evalPyTorch.t7', 'ascii')
net, input = a
generateGraph = require 'optnet.graphgen'

graphOpts = {
displayProps =  {shape='ellipse',fontsize=14, style='solid'},
nodeData = function(oldData, tensor)
  return oldData .. '\n' .. 'Size: '.. tensor:numel()
end
}

g = generateGraph(net, input, graphOpts)
```

### 2017.11.07

* Neural Network Initialise Functions from `main.cpp`
  * `evaluator.Deserialize(EvalNetFilename)`
  * `mevaluator.Deserialize(MoveEvalNetFilename)`
  * `backend.SetEvaluator(&evaluator)`

* An alternate implementation exists within `eigen_ann.cpp` and `eigen_ann.h`, which is faster than the Lua version

* Lua Function Calls
	* `giraffe/ann/ann.h`
		* `class LuaFunctionCall`
	* `giraffe/ann/ann.cpp`
		* calls the class `LuaFunctionCall` twice

### 2017.11.08

* Compile test python + C++ bridge: `g++ -Wall -I/usr/include/python2.7 -std=gnu++0x pythonWrapper.cpp -lpython2.7`
* Compile test python + C++ bridge: `g++ -Wall -I/usr/include/python2.7 -std=gnu++0x wrapperValueNetwork.cpp -lpython2.7`

