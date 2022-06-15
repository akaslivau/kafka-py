# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qworktest-dq-servdsgnpassport-after-dq-servdsgnpassportpbc-command'

fileName = ''
message = '{"dQPBCPlatformCommandList":[{"microServName":"ITCMSA"}]}'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('correlationId', b'75a728ae-da95-4907-85a2-9a8f42623898'),
    ('dqCommandName', str.encode('check-platform')),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
