from enum import Enum


class DQCommandStatus(Enum):
    EMPTY = b''
    OK = b'ok'
    ERROR = b'error'


class DQEventType(Enum):
    EMPTY = b''
    BEFORE_CREATE = b'beforeCreate'
    AFTER_CREATE = b'afterCreate'
    BEFORE_UPDATE = b'beforeUpdate'
    AFTER_UPDATE = b'afterUpdate'
    BEFORE_DELETE = b'beforeDelete'
    AFTER_DELETE = b'afterDelete'
