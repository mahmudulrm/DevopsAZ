#Redis check DB size and number of keys
import redis
servers = ["10.0.3.12", "10.0.3.12", "10.0.3.12"]
password = 'z2mdff'
for server in servers:
    try:
        r = redis.StrictRedis(host=server, port=6379, password=password)
        num_keys = r.dbsize()
        print(f"Total number of keys on {server}: {num_keys}")
    except Exception as e:
        print(f"Failed to connect to {server}: {str(e)}")

#-----
#import redis

password = "z2mdff"
servers = [{"host": "10.0.3.12", "port": 6379},
           {"host": "10.0.3.12", "port": 6379},
           {"host": "10.0.3.12", "port": 6379}]

for server in servers:
    try:
        r = redis.StrictRedis(host=server['host'], port=server['port'], password=password)
        role_info = r.info('replication')
        if role_info['role'] == 'master':
            print(f"Master node of {server['host']}:{server['port']} is {server['host']}:{server['port']}")
        else:
            print(f"{server['host']}:{server['port']} is not a master node")
    except redis.exceptions.ConnectionError:
        print(f"Cannot connect to {server['host']}:{server['port']}")
