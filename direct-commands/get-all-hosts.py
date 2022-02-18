# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-itchosts-request'

fileName = ''
message = '"get hosts"'

headers = [
    ('command', b'get-all-hosts'),
    ('spring_json_header_types', b'{"command":"java.lang.String"}'),
    ('b3', b'9269f1d907af57fb-ce013b8022273df9-1'),
    ('__TypeId__', b'java.lang.String')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
