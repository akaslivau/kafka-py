import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qsftcmdelivery-qis-image-check-response'

fileName = '../payloads/qis-images-response.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('contentType', b'application/json'),
    ('dqCommandName', str.encode('qis-image-check-reply')),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","dqMessageGuid":"java.lang.String","contentType":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('__TypeId__', b'ru.diasoft.micro.model.QISImageCheckDTO'),
    ('mark', b'test-message')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
