# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-didyk-topic-command'

fileName = ''
message = '{"param1":"test", "param2":"123457", "eventCorrelationId":"f5b44ccb-656f-4495-b482-a3f489e9de99"}'

headers = [
    # ('correlationId', b'75a728ae-da95-4907-85a2-9a8f42623898'),
    ('dqCommandName', b'not-matter'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
