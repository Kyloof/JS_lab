import ipaddress
from read_log import read_log

def get_entries_by_code(log: tuple, code: int):
    def validate_code():
        try:
            int(code)
            return True
        except ValueError:
            return False

    result = []

    if validate_code():  
        for line in log:
            if line[-4] == code:  
                result.append(line)
            
    
    return result

print(get_entries_by_code(read_log(), 80))
