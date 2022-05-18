import uuid

# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'dq-qdevops-qsftcmdelivery-command'

fileName = './../payloads/dq-devops-command.json'
message = ''

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommand', str.encode('manual-test')),
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
