all: cpp java firm

install-dependencies:
	@echo "work in progress, comming soon"

install:
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/Virtual-Firmware-grSim.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/PyRemote.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonBot.git
	git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonSoccerAI.git
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install

uninstall:
	rm -rf TritonBot TritonSoccerAI Virtual-Firmware-grSim PyRemote

pull: 
	cd TritonSoccerAI; git pull
	cd TritonBot; git pull
	cd Virtual-Firmware-grSim; git pull
	cd PyRemote; git pull
	git pull

status:
	cd TritonSoccerAI; git status
	cd TritonBot; git status
	cd Virtual-Firmware-grSim; git status
	cd PyRemote; git status
	git status



#default run registers as blue team
run:
	python3 RunScripts/default_run.py

test:
	python3 TestScripts/test.py

test2:
	python3 TestScripts/test2.py

clean: clean-cpp clean-firm clean-java

grSim:
	./../grSim/bin/grSim

cpp:
	cd TritonBot/build; make proto; make -j

java:
	cd TritonSoccerAI && mvn clean compile assembly:single 

firm:
	cd Virtual-Firmware-grSim && make

clean-cpp:
	cd TritonBot/build; make clean; rm -rf ../proto/ProtoGenerated

clean-firm:
	cd Virtual-Firmware-grSim && make clean

clean-java: 
	cd TritonSoccerAI && mvn clean install

run-blue:
	python3 RunScripts/run_blue.py
	
run-yellow:
	python3 RunScripts/run_yellow.py

run-blue-cpp:
	python3 RunScripts/run_blue_cpp.py

run-yellow-cpp:
	python3 RunScripts/run_yellow_cpp.py

gc:
	python3 OtherScripts/game_control.py