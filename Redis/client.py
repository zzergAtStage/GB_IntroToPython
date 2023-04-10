import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop("queue")  #instead rpop
print(int(value[1]))