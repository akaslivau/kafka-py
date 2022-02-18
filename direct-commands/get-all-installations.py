import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-qstandcm-installation-request'

readFromFile = False
fileName = ''
message = 'get-all-installations-didyk-hand'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('command', b'')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
