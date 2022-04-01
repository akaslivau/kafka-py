# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

fileName = 'payloads/platform-possible-null-reply.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
