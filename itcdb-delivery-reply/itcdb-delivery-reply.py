# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qworktest-dq-itcdb-delivery-reply'

fileName = 'schemas.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
