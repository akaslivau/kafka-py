import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qstandcm-installation-command'

fileName = ''
message = 'nothing here'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'get-all-installations'),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('__TypeId__', b'ru.diasoft.micro.dto.InstallationCommandArgs'),
    ('b3', get_uuid())
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
