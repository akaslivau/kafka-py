# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

fileName = '../payloads/platform-null-reply.json'
message = ''

headers = [
    ('dqMessageGuid', b'72d7cf48-01c7-4155-888e-27b579c9f1b6'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
