# TRC-Software

**Note**
* when navigating to a sub-repository, git checkout master (or another desired branch) before making any changes to that sub-repository. This is because git submodule only trace a snapshot of the repository which is detached from the HEAD, to ensure regular usage of git push, checkout a branch HEAD first!
* When switching branch, don't forget to clean the target or build folders
### Install Guide
```bash
# Start at an empty directory ...

# Install all dependencies
sudo apt update
sudo apt install git build-essential cmake pkg-config qt5-default libqt5opengl5-dev libgl1-mesa-dev libglu1-mesa-dev libprotobuf-dev protobuf-compiler libode-dev libboost-all-dev maven openjdk-14-jdk libarmadillo-dev clang 

# Git clone
git clone https://github.com/RoboCup-SSL/grSim.git
git clone https://github.com/IEEE-UCSD-RoboCup-2020/TRC-Software.git
cd TRC-Software
git clone https://github.com/IEEE-UCSD-RoboCup-2020/Virtual-Firmware-grSim.git
git clone https://github.com/IEEE-UCSD-RoboCup-2020/PyRemote.git
git clone https://github.com/IEEE-UCSD-RoboCup-2020/TritonBot.git
git clone https://github.com/IEEE-UCSD-RoboCup-2020/TritonSoccerAI.git

# GrSim setup
cd grSim
mkdir build
cd build 
cmake -DCMAKE_INSTALL_PREFIX=/usr/local ..
make

# TRC setup
cd ../../TRC-Software/TritonBot
mkdir build
cd build 
cmake ..
make clean
make proto
cmake ..
make -j

cd ../../TritonSoccerAI
mvn clean package

cd ../Virtual-Firmware-grSim
make 

cd ../../ 

# Everything is finished
# sudo ./grSim/bin/grSim
# python TRC-Software/run.py
```
