import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-netstore-command'

fileName = ''
message = '{"sender": "test", "name": null, "exactName": null}'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'get-all-net-stores'),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('b3', get_uuid())
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)



