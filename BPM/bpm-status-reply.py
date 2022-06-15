# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-didyk-topic-reply'

fileName = ''
message = '{"statusId": 2}'

headers = [
    ('dqMessageGuid', b'a094af6d-8ec7-4157-96db-d5974a1775b4'),
    ('dqCommandName', b'qworkbpm'),
    ('replyChannel', b'nullChannel'),
    ('spring_json_header_types', b'{"replyChannel":"java.lang.String","dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('__TypeId__', b'u.diasoft.micro.model.DQPBCPlatformReplyInfo')
]

#  SOURCE CODE
send_message(Brokers.QCMDB.value, topic, get_message(fileName, message), headers)
