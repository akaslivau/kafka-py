import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-itchosts-response'

fileName = ''
message = '[{"id":333,"name":"qrunner-n"}]'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('command', str.encode('get-all-hosts-response')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)