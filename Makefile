all: cpp java firm

install:
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/Virtual-Firmware-grSim.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/PyRemote.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonBot.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonSoccerAI.git

uninstall:
	rm -rf TritonBot TritonSoccerAI Virtual-Firmware-grSim PyRemote

pull: 
	cd TritonSoccerAI; git pull
	cd TritonBot; git pull
	cd Virtual-Firmware-grSim; git pull
	cd PyRemote; git pull


init: firm
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install

run:
	python3 RunScripts/run.py 

test:
	python3 TestScripts/test.py

clean: clean-cpp clean-firm clean-java

grSim:
	./../grSim/bin/grSim

cpp:
	cd TritonBot/build && make -j

java:
	cd TritonSoccerAI && mvn clean compile assembly:single 

firm:
	cd Virtual-Firmware-grSim && make

clean-cpp:
	cd TritonBot/build && make clean

clean-firm:
	cd Virtual-Firmware-grSim && make clean

clean-java: 
	cd TritonSoccerAI && mvn clean install

