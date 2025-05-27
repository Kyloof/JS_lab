def entry_to_dict(entry: tuple):
    return {
            "ts": entry[0],
            "uid": entry[1],
            "id.orig_h": entry[2],
            "id.orig_p": entry[3],
            "id.resp_h": entry[4],
            "id.resp_p": entry[5],
            "method": entry[6],
            "host": entry[7],
            "uri": entry[8],
            "status_code": entry[9]
        }

#print(entry_to_dict(((2012, 3, 16, 13, 30), 'CHEt7z3AzG4gyCNgci', '192.168.202.79', 50465, '192.168.229.251', 80, 'HEAD', '192.168.229.251', '/DEASLog02.nsf')))