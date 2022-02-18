import uuid

from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka.future import log

# Brokers-list
# localhost:9092
# 192.168.31.189:9092
# digidemo.diasoft.ru:9092
# qrunkafka.diasoft.ru:9092

# User settings
# broker = '192.168.31.189:9092'
broker = 'digidemo.diasoft.ru:9092'

#
#
#
topic = 'dq-itsoftware-response'

readFromFile = False
fileName = ''
message = '[{"id":61,"name":"MS SQL Server","component_id":1,"component_name":"СУБД"},{"id":62,"name":"PostgreSQL","component_id":1,"component_name":"СУБД"},{"id":63,"name":"Oracle","component_id":1,"component_name":"СУБД"},{"id":64,"name":"IBM Websphere","component_id":2,"component_name":"Сервер приложений"},{"id":65,"name":"Oracle Weblogic","component_id":2,"component_name":"Сервер приложений"},{"id":66,"name":"JBOSS EAP","component_id":2,"component_name":"Сервер приложений"},{"id":67,"name":"Wildfly","component_id":2,"component_name":"Сервер приложений"},{"id":68,"name":"Kubernetes","component_id":3,"component_name":"Кластер MSA"},{"id":69,"name":"Q.Kubernetes","component_id":3,"component_name":"Кластер MSA"},{"id":70,"name":"Q.Runner","component_id":3,"component_name":"Кластер MSA"},{"id":71,"name":"Openshift","component_id":3,"component_name":"Кластер MSA"},{"id":72,"name":"Kafka","component_id":4,"component_name":"Брокер сообщений"},{"id":73,"name":"Q.Kafka","component_id":4,"component_name":"Брокер сообщений"},{"id":74,"name":"ElasticSearch","component_id":5,"component_name":"Кластер ELK"},{"id":75,"name":"Fluent Bit","component_id":5,"component_name":"Кластер ELK"},{"id":76,"name":"Kibana","component_id":5,"component_name":"Кластер ELK"},{"id":77,"name":"Zipkin","component_id":5,"component_name":"Кластер ELK"},{"id":78,"name":"MS Windows Server","component_id":6,"component_name":"Операционная система"},{"id":79,"name":"RHEL","component_id":6,"component_name":"Операционная система"},{"id":80,"name":"CentOS","component_id":6,"component_name":"Операционная система"},{"id":81,"name":"Ubuntu","component_id":6,"component_name":"Операционная система"},{"id":82,"name":"Harbor","component_id":7,"component_name":"Хранилище образов"}]'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('command', str.encode('get-all-software-name-response')),
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
