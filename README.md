# TritonsRCSC-Software-Pack

This is a All-in-One repository containing the necessary sub-repositories, scripts, and misc components to run our software for Team TritonsRCSC in RoboCup Soccer SSL(Small Size League) competition, which is an international robotics tournament featuring autonomous robots playing soccer. More information about RoboCup can be found in the links below:

* [RoboCup](https://www.robocup.org/)
* [RoboCup Soccer Small Size League](https://ssl.robocup.org/)



This repository contains a script to automatically install simulators to run along with our AI software. Our software can run on an entirely virtual settings without any hardware robots. 



## Install

#### System Requirement 

Ubuntu 18.04 or higher (Ubuntu 20.04 is recommended)

(Win10 & MacOS support coming soon)

The install scripts will install many sub-repositories, including two simulator repositories forked from the official repositories maintained by the competition, which have their own system requirements:

* https://github.com/RoboCup-SSL/grSim
* https://github.com/robotics-erlangen/framework#simulator-cli

#### Instruction

Clone this repository, cd into it, then run: 	(root access is required, might take a few minutes)

```shell
make install
```
(many dependency would get installed via apt/apt-get, type "Y" along the way if prompted, if you are using a different Linux distribution, please refer to the Makefile to find out whhich packages to install)


Similarly, to uninstall:

```shell
make uninstall
```



Once make install is done, several repositories would be installed under this repository, and they are already listed in .gitignore so you won't need to worry about git operations on this repository having effect or getting affected by those sub-repositories. These sub-repositories can be considered as git-submodules, but we deliberately chose not to use git submodule feature from git due to personal preferences. 

In addition, there is a handy 

```shell
make pull
```

that automatically pull the latest version for every sub-repositories, but the rest of git operations should be performed in this repository and the sub-repositories separately.



## Compile

```shell
make
```

This make will build sources in the sub-repositories too!

#### Note on protobuf

Our software & competition simulator use google protobuf for data serialization, which involves auto-generating c++/java source code based on proto definitions stored in .proto files. You normally won't need to worry anything about it if you don't make any changes to any of the .proto files. In case you do made modifications to any of the .proto files, make sure to run the following before re-compile:

```shell
make clean
make regenerate-proto-src
```

  

# Run (virtual setting)

To run our AI software commanding virtual robots in the simulator, first open the simulator, there are 2 simulator choices available

* grSim

  * ```shell
    make open-grsim
    ```
  * grSim might display error messgae in the bottom region, just ignore them

* ER-Force Simulator

  * ```shell
    make open-erf
    ```

  * RoboCup SSL 2021 Virtual Tournament decided to use ER-Force Simulator for official games

Then run our AI software:

```shell
make run
```

then follow the instructions in the stdout prompt.



To test components of our AI software, run:

```shell
make test
```

 to perform the interactive manual tests through user typing in the terminal. Automated tests are not ideal for this application because GUI simulator and human judgment is required to evaluate the test performance.



# Run (real robots setting)

coming soon