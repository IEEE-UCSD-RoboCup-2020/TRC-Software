all: cpp java firm

run:
	python3 run2.py

grSim:
	./../grSim/bin/grSim

cpp:
	cd TritonBot/build && make -j

java:
	cd TritonSoccerAI && mvn package

firm:
	cd Virtual-Firmware-grSim && make

init: firm
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install package
