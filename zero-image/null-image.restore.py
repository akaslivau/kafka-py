# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qsftcmdelivery-qis-delivery-create-command'

fileName = '../payloads/zero-image-dto.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', str.encode('qis-create-delivery-command')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
