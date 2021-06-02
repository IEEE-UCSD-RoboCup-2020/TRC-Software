all: #don't write it as "all: cpp java", which crashes my computer sometimes
	cd TritonBot/build; make -j
	cd TritonSoccerAI; mvn compile assembly:single
cpp:
	cd TritonBot/build; make

java:
	cd TritonSoccerAI; mvn compile assembly:single 


pull: 	
	@git pull
	@if cd Virtual-Firmware-grSim; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/Virtual-Firmware-grSim.git; fi
	@if cd PyRemote; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/PyRemote.git; fi
	@if cd TritonBot; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonBot.git; fi
	@if cd TritonSoccerAI; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonSoccerAI.git; fi
	@if cd VisionBroadcastPrinter; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/VisionBroadcastPrinter.git; fi
	@if cd grSim; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/grSim.git; fi
	@if cd ssl-simulation-protocol; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/ssl-simulation-protocol.git; fi
	@if cd TritonBot/include/Misc/Inih/inih; then git pull; else git clone https://github.com/IEEE-UCSD-RoboCupSSL/inih.git TritonBot/include/Misc/Inih/inih; fi
	
install: pull
	sudo apt update
	sudo apt install cmake git build-essential cmake pkg-config qt5-default libqt5opengl5-dev libgl1-mesa-dev libglu1-mesa-dev libprotobuf-dev protobuf-compiler libode-dev libboost-all-dev maven openjdk-14-jdk libarmadillo-dev clang screen
	cd VisionBroadcastPrinter; make protosrc; make -j;
	cd grSim; mkdir -p build; cd build; cmake ..; make; sudo make install
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI/src/main/java/Triton/Legacy/OldGrSimProto; make
	cd TritonSoccerAI; mvn clean install



progs = TritonBot TritonSoccerAI Virtual-Firmware-grSim PyRemote VisionBroadcastPrinter ssl-simulation-protocol TritonBot/include/Misc/Inih/inih
simulators = grSim

uninstall:
	rm -rf $(progs) $(simulators)
	

uninstall-except-simulators:
	rm -rf $(progs)


import-proto:
	cp CustomProto/*.proto TritonBot/proto/
	cp CustomProto/*.proto TritonSoccerAI/src/main/proto/
	cp ssl-simulation-protocol/proto/*.proto TritonSoccerAI/src/main/proto/
	

regenerate-proto-src:
	cd TritonBot; mkdir -p build; cd build; cmake ..; make clean; make proto; cmake ..; make -j
	cd TritonSoccerAI; mvn clean install


open-grsim:
	screen -dmS grSim-session grSim/bin/grSim


status:
	cd TritonSoccerAI; git status
	cd TritonBot; git status
	cd Virtual-Firmware-grSim; git status
	cd PyRemote; git status
	cd grSim; git status
	git status



#default run registers as blue team
# run:
# 	python3 RunScripts/default_run.py

test: 
	python3 PyScripts/TestScripts/test-AI-virtual.py -b -s mainsetup-grsim-6v6.ini

test-tab: 
	python3 PyScripts/TestScripts/test-AI-virtual.py -db -s mainsetup-grsim-6v6.ini

# test-blue:
# 	python3 TestScripts/test-blue.py

# test-yellow:
# 	python3 TestScripts/test-yellow.py

# test-tritonbot:
# 	python3 TestScripts/test-tritonbot.py


clean: clean-cpp clean-java



# firm:
# 	cd Virtual-Firmware-grSim && make

clean-cpp:
	cd TritonBot/build; make clean; rm -rf ../proto/ProtoGenerated; make proto

# clean-firm:
# 	cd Virtual-Firmware-grSim && make clean

clean-java: 
	cd TritonSoccerAI && mvn clean install


gc:
	python3 OtherScripts/game_control.py


print-vision-detection-old:
	VisionBroadcastPrinter/vbp detection
