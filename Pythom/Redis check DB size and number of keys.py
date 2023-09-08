#Redis check DB size and number of keys
import redis
servers = ["10.0.3.121", "10.0.3.122", "10.0.3.123"]
password = 'tz2m9uqdelgh7*4'
for server in servers:
    try:
        r = redis.StrictRedis(host=server, port=6379, password=password)
        num_keys = r.dbsize()
        print(f"Total number of keys on {server}: {num_keys}")
    except Exception as e:
        print(f"Failed to connect to {server}: {str(e)}")
