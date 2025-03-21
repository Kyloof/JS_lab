import sys
from datetime import datetime

def read_log():
    log = []
    
    
    for line in sys.stdin:
        line = line.split()
        elements = line[:6] + line[7:10]

        ts = datetime.fromtimestamp(float(elements[0]))
        orig_port = int(elements[3])
        resp_port = int(elements[5])
        
        log_entry = (ts, elements[1], elements[2], orig_port, elements[4], resp_port, elements[6], elements[7], elements[8])
        log.append(log_entry)
    
    return log

#print(read_log()[:1])