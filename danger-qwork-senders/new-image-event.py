import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qwork-dq-qis-new-image-event'

fileName = '../payloads/new-image-event.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommand', str.encode('new-image-event')),
]

#  SOURCE CODE
send_message(Brokers.ARE_YOU_SURE_QWORK.value, topic, get_message(fileName, message), headers)
