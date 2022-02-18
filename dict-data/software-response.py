import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-itsoftware-response'

fileName = ''
message = '[{"id":61,"name":"MS SQL Server","component_id":1,"component_name":"СУБД"},{"id":62,"name":"PostgreSQL","component_id":1,"component_name":"СУБД"},{"id":63,"name":"Oracle","component_id":1,"component_name":"СУБД"},{"id":64,"name":"IBM Websphere","component_id":2,"component_name":"Сервер приложений"},{"id":65,"name":"Oracle Weblogic","component_id":2,"component_name":"Сервер приложений"},{"id":66,"name":"JBOSS EAP","component_id":2,"component_name":"Сервер приложений"},{"id":67,"name":"Wildfly","component_id":2,"component_name":"Сервер приложений"},{"id":68,"name":"Kubernetes","component_id":3,"component_name":"Кластер MSA"},{"id":69,"name":"Q.Kubernetes","component_id":3,"component_name":"Кластер MSA"},{"id":70,"name":"Q.Runner","component_id":3,"component_name":"Кластер MSA"},{"id":71,"name":"Openshift","component_id":3,"component_name":"Кластер MSA"},{"id":72,"name":"Kafka","component_id":4,"component_name":"Брокер сообщений"},{"id":73,"name":"Q.Kafka","component_id":4,"component_name":"Брокер сообщений"},{"id":74,"name":"ElasticSearch","component_id":5,"component_name":"Кластер ELK"},{"id":75,"name":"Fluent Bit","component_id":5,"component_name":"Кластер ELK"},{"id":76,"name":"Kibana","component_id":5,"component_name":"Кластер ELK"},{"id":77,"name":"Zipkin","component_id":5,"component_name":"Кластер ELK"},{"id":78,"name":"MS Windows Server","component_id":6,"component_name":"Операционная система"},{"id":79,"name":"RHEL","component_id":6,"component_name":"Операционная система"},{"id":80,"name":"CentOS","component_id":6,"component_name":"Операционная система"},{"id":81,"name":"Ubuntu","component_id":6,"component_name":"Операционная система"},{"id":82,"name":"Harbor","component_id":7,"component_name":"Хранилище образов"}]'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('command', str.encode('get-all-software-name-response')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
