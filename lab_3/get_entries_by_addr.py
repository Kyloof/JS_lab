import ipaddress
from read_log import read_log

def get_entries_by_addr(log: tuple, addr: str):
    def validate_addr():
        try:
            ipaddress.ip_address(addr)
            return True
        except ValueError:
            return False

    result = []

    if validate_addr():  
        for line in log:
            if line[-2] == addr or line[2] == addr:  
                result.append(line)
            
    
    return result

print(get_entries_by_addr(read_log(), '192.168.202.79'))
