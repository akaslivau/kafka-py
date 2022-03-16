import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qis-add-image-rule'

fileName = ''
message = '{"repoId":8,"imageStorageId":1,"images":["itcmsa"],"runTypeId":1,"day":null,"hour":null,"minute":null,"grade":"3"}'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('specialMark', b'send-manually-by-didyk'),
    ('dqCommandName', b'create-replication-rule')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
