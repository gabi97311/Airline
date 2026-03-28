from enum import Enum
import enum


class PaymentStatus(str , Enum): 
    pending = 'pending'
    succeeded = 'succeeded'
    failed = 'failed'

    