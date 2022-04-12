import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qcm-releasedconfelementcomposition-add-event'

fileName = 'payloads/qvcs-release-wrong.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('contentType', b'application/json'),
    ('dqCommandName', str.encode('any command')),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String","x-dsft-login":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('__TypeId__', b'ru.diasoft.micro.dto.qarcher.DQPBCPlatformCommandInfo'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
