import uuid

# User settings
from _core.brokers import Brokers
from _core.diasoft_enums import DQCommandStatus
from _core.functions import send_message, get_message

# INPUT
topic = 'qvcs-commit-create-command'

fileName = 'payloads/qvcs-commit-create-branch.json'
message = ''

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('dqCommandName', str.encode('create-commit')),
    ('dqCommandStatus', DQCommandStatus.OK.value),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
