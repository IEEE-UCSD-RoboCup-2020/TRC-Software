all: cpp java firm

install:
	git clone https://github.com/IEEE-UCSD-RoboCup-2020/Virtual-Firmware-grSim.git
	git clone https://github.com/IEEE-UCSD-RoboCup-2020/PyRemote.git
	git clone https://github.com/IEEE-UCSD-RoboCup-2020/TritonBot.git
	git clone https://github.com/IEEE-UCSD-RoboCup-2020/TritonSoccerAI.git

uninstall:
	rm -rf TritonBot TritonSoccerAI Virtual-Firmware-grSim PyRemote

run:
	python3 run3.py -jcv


grSim:
	./../grSim/bin/grSim

cpp:
	cd TritonBot/build && make -j

java:
	cd TritonSoccerAI && mvn clean compile assembly:single 

firm:
	cd Virtual-Firmware-grSim && make

init: firm
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install

