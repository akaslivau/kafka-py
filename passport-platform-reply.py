# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message

# INPUT
topic = 'dq-servdsgnpassport-after-dq-servdsgnpassportpbc-reply'

fileName = 'payloads/platform-single-reply.json'
message = ''

headers = [
    ('dqMessageGuid', str.encode('2bbca9ea-62d9-42bd-87e1-5210ff10b3ab')),
    ('dqCommandName', str.encode('not-matter')),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.PUBUNTU.value, topic, get_message(fileName, message), headers)
