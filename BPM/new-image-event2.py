import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qis-new-image-event3'

guid = str(uuid.uuid4())
get_uuid()
fileName = ''
message = '{"param1":5, "correlationId": "' + guid + '"}'

headers = [
    ('dqCommand', str.encode('new-image-event')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
