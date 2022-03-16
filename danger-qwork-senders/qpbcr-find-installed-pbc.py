# User settings
from _core.brokers import Brokers
from _core.functions import send_message, get_message, get_uuid

# INPUT
topic = 'qwork-dq-dqqpbcr-installed-pbc-find-installedpbc-command'

fileName = ''
message = '{"namespace":"qwork"}'

headers = [
    ('dqMessageGuid', get_uuid()),
    ('dqCommandName', str.encode('findInstalledPbc')),
    ('spring_json_header_types', b'{"dqMessageGuid":"java.lang.String","dqCommandName":"java.lang.String"}'),
    ('b3', get_uuid()),
    ('x-dsft-login', b'echernykh'),
    ('__TypeId__', b'ru.diasoft.micro.integration.qpbcr.dto.PbcInputParamInfo')
]

#  SOURCE CODE
send_message(Brokers.ARE_YOU_SURE_QWORK.value, topic, get_message(fileName, message), headers)
