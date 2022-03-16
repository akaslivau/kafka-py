# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

fileName = 'payloads/platform-single-reply.json'
message = ''

headers = [
    ('dqMessageGuid', b'9dcede20-bc55-4f85-a353-8c33ea27d0ef'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
