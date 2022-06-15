# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qworktest-dq-itcdb-command'

fileName = ''
message = '{"deliveryId":859,"installationId":1,"msNames":["qiideamsgbot","qicomposition","qiideaprocessingplan",' \
          '"qiidea","qiideareference"]} '

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', b'schema_create_batch'),
    ('specialMark', b'send-manually-by-didyk')
]

#  SOURCE CODE
send_message(Brokers.QWORKTEST.value, topic, get_message(fileName, message), headers)
