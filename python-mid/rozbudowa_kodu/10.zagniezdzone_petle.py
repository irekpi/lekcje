ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
all_connections_with_repeats = [(a,b) for a in ports for b in ports]

all_connections = [(a,b) for a in ports for b in ports if a!=b]


all_connections_set = [(a,b) for a in ports for b in ports if a <b ]



#Generatory

gen_all_connections_with_repeats = ((a,b) for a in ports for b in ports)

gen_all_connections = ((a,b) for a in ports for b in ports if a!=b)

gen_all_connections_set = ((a,b) for a in ports for b in ports if a <b)

last_gen_len = 0
while True:
    try:
        print(next(gen_all_connections_set))
        last_gen_len += 1
    except StopIteration:
        print('All items were counted')
        print(last_gen_len)
        break
