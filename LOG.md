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
