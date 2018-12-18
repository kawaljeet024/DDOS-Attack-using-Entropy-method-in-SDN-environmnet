import socket
import time
import random
import os
#destination Ip can be passed in argv later

src_ip = "10.0.0.1"

portNum = 80
#portNum = 6555
#flood the packets for 60secs
interval  = 5

def generateUdpPackets():
   #startT = time.time()
   #currT = time.time()
   destIpL = { '10.0.0.2', '10.0.0.3' , '10.0.0.4'}   
      
   #print startT
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   startT = time.time()
   #s.connect((ip,portNum))
   print "Generating random packets to host on mininet simulation"
   while(time.time() - startT < interval):
      #create bytes of data
         i = random.randint(2,16)
       #for i in range(2,17):
         ip = "10.0.0." + str(i)
         print ip
         data = os.urandom(3)
         s.sendto(data,(ip,portNum))
   s.close()

if __name__ == "__main__":
   generateUdpPackets()


