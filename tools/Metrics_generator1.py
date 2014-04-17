import telnetlib
import datetime
import time

"""
Setup env and Connect to OpenTSDB via telnet client
"""
host = "localhost"
user = "ec2-user"
tn= telnetlib.Telnet(host, 4242) #Connect to OpenTsdb via telnet

curent_date = int(time.time()) #Current date in milliseconds 


"""
Start adding metrics into OpenTSDB each minute.
"""  
for i in range(60):
    print "nr.4444445.app.art", curent_date, 0, "app=2612623", "KnM=1"
    tn.write("put")
    tn.write ("'nr.4444445.app.art', curent_date, 0, 'app=2612623', 'KnM=1\n'")
    tn.write("exit\n")
    print tn.read_all()
    time.sleep(60)
    
if __name__ == '__main__':
    pass
