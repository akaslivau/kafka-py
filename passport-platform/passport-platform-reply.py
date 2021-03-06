# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

fileName = ''
message = ''

headers = [
    ('dqMessageGuid', b'33f39c68-eafb-4de7-baa2-e7854bd55a16'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
