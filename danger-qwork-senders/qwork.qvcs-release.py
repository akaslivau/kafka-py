import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qwork-qcm-releasedconfelementcomposition-add-event'

fileName = '../payloads/qvcs-release-real-qwork.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('contentType', b'application/json'),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","b3":"java.lang.String","nativeHeaders":"org.springframework.util.LinkedMultiValueMap","contentType":"java.lang.String"}')
]

#  SOURCE CODE
send_message(Brokers.ARE_YOU_SURE_QWORK.value, topic, get_message(fileName, message), headers)
