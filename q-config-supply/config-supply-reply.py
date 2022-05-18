import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qconfigsupply-configsupply-command-reply2'

fileName = 'qcm-reply.json'
message = ''

headers = [
    ('dqMessageGuid', b'bb3e8b4a-91e0-4b4e-97e6-5447c4e91b44'),
    ('contentType', b'application/json'),
    ('dqCommandName', b'create'),
    ('dqCommandStatus', b'ok'),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String","x-dsft-login":"java.lang.String"}'),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)