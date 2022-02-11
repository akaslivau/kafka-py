import uuid

from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka.future import log

from diasoft_enums import DQEventType, DQCommandStatus

# Brokers-list
# localhost:9092
# 192.168.31.189:9092
# digidemo.diasoft.rut:9092
# qrunkafka.diasoft.ru:9092

# User settings
broker = 'qrunkafka.diasoft.ru:9092'
topic = 'dq-itchosts-request'

readFromFile = False
fileName = ''
message = '"get hosts"'

headers = [
    ('command', b'get-all-hosts'),
    ('spring_json_header_types', b'{"command":"java.lang.String"}'),
    ('b3', b'9269f1d907af57fb-ce013b8022273df9-1'),
    ('__TypeId__', b'java.lang.String')
]

#  SOURCE CODE
if readFromFile:
    with open(fileName, 'r', encoding="utf8") as file:
        message = file.read()

producer = KafkaProducer(bootstrap_servers=[broker])

# Asynchronous by default
future = producer.send(topic=topic, value=str.encode(message), headers=headers)

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print("Sent to topic: {}".format(record_metadata.topic))
print("Partition: {}".format(record_metadata.partition))
print("Offset: {}".format(record_metadata.offset))