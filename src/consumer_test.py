from kafka import KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer(
   'test',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
#    group_id='my-group-1',
#    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['localhost:9092']
)

for m in consumer:
    try:
        value = m.value
        timestamp = int(value.decode('utf-8'))
        tm_diff = int(time.time()*1000) - timestamp
        print(f'{tm_diff} ms')
    except ValueError:
        print('ValueError')
    except KeyboardInterrupt:
        print('Bye')
        sys.exit(0)
    except:
        print('SHIT')
        sys.exit(127)
