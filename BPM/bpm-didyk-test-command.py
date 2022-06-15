# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qwork-delivery-event'

fileName = ''
message = '{"statusId":1, "correlationId": "1dad9c25-d5da-4c6d-9db5-6f25dda0441e"}'

headers = [
    ('correlationId', b'1dad9c25-d5da-4c6d-9db5-6f25dda0441e'),
    ('dqMessageGuid', b'1dad9c25-d5da-4c6d-9db5-6f25dda0441e'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
