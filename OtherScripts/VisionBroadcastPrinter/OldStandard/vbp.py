# if proto definition is modified, empty "proto-gen" folder 
# and then run "protoc -I=proto --python_out=protogen proto/*.proto" to apply the change
import sys
sys.path.append("./protogen")
import messages_robocup_ssl_wrapper_pb2
import messages_robocup_ssl_detection_pb2
import messages_robocup_ssl_geometry_pb2

packet = input()
ssl_wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
parsedPacket = ssl_wrapper.parseFrom(packet)
print(parsedPacket)