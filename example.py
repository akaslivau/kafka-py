import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-didyk-test'

fileName = ''
message = 'pidorasina'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('dqCommandName', b'get-all-db')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)