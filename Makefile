all: cpp java firm

install:
	sudo apt update
	sudo apt install cmake git build-essential cmake pkg-config qt5-default libqt5opengl5-dev libgl1-mesa-dev libglu1-mesa-dev libprotobuf-dev protobuf-compiler libode-dev libboost-all-dev maven openjdk-14-jdk libarmadillo-dev clang 
	if cd Virtual-Firmware-grSim; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/Virtual-Firmware-grSim.git; fi
	if cd PyRemote; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/PyRemote.git; fi
	if cd TritonBot; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonBot.git; fi
	if cd TritonSoccerAI; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonSoccerAI.git; fi
	if cd VisionBroadcastPrinter; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/VisionBroadcastPrinter.git; fi
	if cd VisionBroadcastPrinter/UDP-Multicast-NetCat; then git pull; else cd VisionBroadcastPrinter; git clone https://github.com/IEEE-UCSD-RoboCupSSL/UDP-Multicast-NetCat.git; fi
	if cd grSim; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/grSim.git; fi
	cd VisionBroadcastPrinter/UDP-Multicast-NetCat; make;
	cd VisionBroadcastPrinter; make;
	cd grSim; mkdir -p build; cd build; cmake ..; make; sudo make install
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install

progs = TritonBot TritonSoccerAI Virtual-Firmware-grSim PyRemote UDP-Multicast-NetCat  
simulators = grSim

uninstall:
	rm -rf $(progs) $(simulators)
	

uninstall-except-simulators:
	rm -rf $(progs)



regenerate-proto-src:
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install


open-grsim:
	screen -dmS grSim-session grSim/bin/grSim



pull: 
	cd TritonSoccerAI; git pull
	cd TritonBot; git pull
	cd Virtual-Firmware-grSim; git pull
	cd PyRemote; git pull
	cd grSim; git pull
	git pull

status:
	cd TritonSoccerAI; git status
	cd TritonBot; git status
	cd Virtual-Firmware-grSim; git status
	cd PyRemote; git status
	cd grSim; git status
	git status



#default run registers as blue team
run:
	python3 RunScripts/default_run.py

test:
	python3 TestScripts/test.py

test2:
	python3 TestScripts/test2.py

clean: clean-cpp clean-firm clean-java


cpp:
	cd TritonBot/build && make -j

java:
	cd TritonSoccerAI && mvn clean compile assembly:single 

firm:
	cd Virtual-Firmware-grSim && make

clean-cpp:
	cd TritonBot/build; make clean; rm -rf ../proto/ProtoGenerated; make proto

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


mnc-path = UDP-Multicast-NetCat
vbp-path = OtherScripts/VisionBroadcastPrinter/OldStandard
print-vision-wrapper:
	cd $(vbp-path); ../../../$(mnc-path)/mnc -l 224.5.23.2 10020 | python3 vbp.py