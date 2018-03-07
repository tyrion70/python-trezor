# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .TransactionType import TransactionType
from .TxInputType import TxInputType
from .TxOutputType import TxOutputType


class SimpleSignTx(p.MessageType):
    FIELDS = {
        1: ('inputs', TxInputType, p.FLAG_REPEATED),
        2: ('outputs', TxOutputType, p.FLAG_REPEATED),
        3: ('transactions', TransactionType, p.FLAG_REPEATED),
        4: ('coin_name', p.UnicodeType, 0),  # default=u'Bitcoin'
        5: ('version', p.UVarintType, 0),  # default=1
        6: ('lock_time', p.UVarintType, 0),  # default=0
    }
    MESSAGE_WIRE_TYPE = 16
