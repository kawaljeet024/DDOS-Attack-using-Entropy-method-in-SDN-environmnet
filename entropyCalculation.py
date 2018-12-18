import math

class ddosDetection:

    pktCnt = 0
    #ddosDetected : 1 indicates ddosDetected is true , 0 : false
    ddosDetected = 0
    # if 10 times consecutively , entropy value is less than 1, then indicate to controller than DDOS Attack is detected
    counter = 0
    ipList_Dict = {}
    sumEntropy = 0
    def calculateEntropy(self,ip):
       #calculate entropy when pkt cont reaches 100
       self.pktCnt +=1
       if ip in self.ipList_Dict:
          self.ipList_Dict[ip] += 1
       else:
          self.ipList_Dict[ip] = 0
 
       if self.pktCnt == 50:
          #print self.ipList_Dict.items()
          #print self.pktCnt
          self.sumEntropy = 0
          self.ddosDetected = 0
          print "Window size of 50 pkts reached, calculate entropy"
          for ip,value in self.ipList_Dict.items():
              prob = abs(value/float(self.pktCnt))
              #print prob
              if (prob > 0.0) : 
                 ent = -prob * math.log(prob,2)
                 #print ent
                 self.sumEntropy =  self.sumEntropy + ent
          print "Entropy Value = ",self.sumEntropy  
          if (self.sumEntropy < 2 and self.sumEntropy != 0) :
             self.counter += 1
          else :
             self.counter = 0 
          if self.counter == 10:
             self.ddosDetected = 1
             print "Counter = ",self.counter
             print "DDOS ATTACK DETECTED"
             self.counter = 0 
          self.cleanUpValues()       
       
    def cleanUpValues(self):
       self.pktCnt = 0
       self.dest_ipList = []
       self.ipList_Dict = {}
       #self.sumEntropy = 0

def __init__(self):
    pass
