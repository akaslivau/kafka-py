import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-itcdb-command'

fileName = ''
message = '"get-all-db-schema-command"'

headers = [
    ('dqMessageGuid', str.encode(str(uuid.uuid4()))),
    ('dqCommandName', b'get-all-db-schema-command')

]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
