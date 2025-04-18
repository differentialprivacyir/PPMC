def read_dataset(filename):
    print('Reading dataset ...')
    data = []

    file = open(filename,'r')
    file.readline() # just skip headline

    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        line_splited = line.split(",")
        data.append([int(x) for x in line_splited])

    file.close()
    return data

def attributes_domain(filename):
    print('Reading domains ...')
    domains = []
    
    file = open(filename,'r')
    file.readline() # just skip headline

    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        line_splited = line.split(" ")
        domains.append([int(x) for x in line_splited[3:]])

    file.close()
    return domains
