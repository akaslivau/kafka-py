# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qwork-dq-servdsgnpassport-after-dq-servdsgnpassportpbc-command'

fileName = 'payloads/platform-command.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', str.encode('check-platform')),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo')
]

#  SOURCE CODE
send_message(Brokers.ARE_YOU_SURE_QWORK.value, topic, get_message(fileName, message), headers)
