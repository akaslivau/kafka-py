import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qstandcm-installation-event'

fileName = ''
message = '{"statusId":1,"name":"test_inst_05_05_2022","standId":46,"standName":"test_12_04_22","installationId":58,' \
          '"statusName":"Доступно"} '

headers = [
    ('dqMessageGuid', get_uuid()),
    ('contentType', b'application/json'),
    ('dqCommandName', str.encode('any command')),
    ('dqEventType', str.encode('afterCreate')),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String","x-dsft-login":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('__TypeId__', b'ru.diasoft.micro.model.KInstallationDto'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)