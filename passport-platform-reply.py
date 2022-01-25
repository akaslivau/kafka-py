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
broker = '192.168.31.189:9092'

#
#
#
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

readFromFile = True
fileName = 'payloads/platform-single-reply.json'
message = ''

headers = [
    ('dqMessageGuid', str.encode('0b08a59b-5feb-48d7-b949-f076b568de49')),
    ('specialMark', b'send-manually-by-didyk')
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
