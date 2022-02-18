import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-itsoftware-request'

fileName = ''
message = '"get software"'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('command', b'get-all-software')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
