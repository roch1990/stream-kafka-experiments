from kafka import KafkaConsumer
from json import loads
import time
import sys

consumer = KafkaConsumer(
   'test',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group',
#    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['10.5.0.8:9094', '10.5.0.7:9093', '10.5.0.6:9092']
)

for m in consumer:
    try:
        value = m.value
        timestamp = int(value.decode('utf-8'))
        tm_diff = int(time.time()*1000) - timestamp
        print(f'{tm_diff} ms')
    except KeyboardInterrupt:
        print('Bye')
        sys.exit(0)
    except ValueError:
        print('ValueError')

    except:
        print('SHIT')
        sys.exit(127)
