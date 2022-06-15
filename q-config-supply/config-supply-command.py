import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qwork-dq-qconfigsupply-configsupply-command2'

fileName = 'config-supply-command-single-pbc.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('contentType', b'application/json'),
    ('dqCommandName', b'create'),
    ('dqCommandStatus', b'ok'),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String","x-dsft-login":"java.lang.String"}'),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.ARE_YOU_SURE_QWORK.value, topic, get_message(fileName, message), headers)