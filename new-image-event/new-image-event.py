import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qis-new-image-event'

fileName = 'qi-idea-error.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommand', str.encode('new-image-event')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
