import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-dqqpbcr-installed-pbc-find-installedpbc-command'

fileName = '../payloads/stand-update-conf-command.json'
message = ''

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
