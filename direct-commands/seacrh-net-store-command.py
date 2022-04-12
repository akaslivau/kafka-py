import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-space-netstore-command'

fileName = ''
message = '{"sender": "test", "spaceNames": ["Space_1", "Space_3"]}'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'not-matter'),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('__TypeId__', b'ru.diasoft.micro.model.KSpaceNetstoreArgs'),
    ('b3', get_uuid())
]



#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)



