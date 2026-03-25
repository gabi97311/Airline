from sqlalchemy import Enum
import enum


class PaymentStatus(str ,Enum.enum): 
    pending = 'pending'
    succeeded = 'succeeded'
    failed = 'failed'
    