from kafka import KafkaProducer
from json import dumps
import time
import sys

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'),
   bootstrap_servers=['localhost:9092']
)

while True:
    try:
        message = int(time.time()*1000)
        producer.send("test", value=message)
        print(f'message sent: {message}')
#        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
