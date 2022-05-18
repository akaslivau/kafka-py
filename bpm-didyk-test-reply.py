# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-didyk-topic-reply'

fileName = ''
message = '{"param1":"test", "param2":"123457"}'

headers = [
    ('correlationId', b'58945d7a-9f2f-49d0-94dc-6298ec3325b3'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
