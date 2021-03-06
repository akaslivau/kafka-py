import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qworktest-dq-qconfigsupply-configsupply-command-reply2'

fileName = 'qiidea-reply.json'
message = ''

headers = [
    ('dqMessageGuid', b'd532310b-ccd5-4e3f-826d-f3621fc3fcb3'),
    ('contentType', b'application/json'),
    ('dqCommandName', b'create'),
    ('dqCommandStatus', b'ok'),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String","x-dsft-login":"java.lang.String"}'),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)