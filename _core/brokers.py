from enum import Enum


class Brokers(Enum):
    LOCALHOST = 'localhost:9092'
    PUBUNTU = '192.168.31.189:9092'
    QCMDB = 'digidemo.diasoft.ru:9092'
    QWORKTEST = 'qrunkafka.diasoft.ru:9092'
    ARE_YOU_SURE_QWORK = 'qk3.diasoft.ru:9092'