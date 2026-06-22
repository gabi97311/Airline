import enum 

class PaymentStatus(str , enum.Enum): 
    pending = 'pending'
    succeeded = 'succeeded'
    failed = 'failed' 
    
class SeatClass(str, enum.Enum):
    economy = 'Economy'
    business = 'Business'
    comfort = 'Comfort'
    first = 'First'
    
class SeatStatus(str, enum.Enum):
    free = 'Free'
    pending = 'Pending'
    occupied = 'Occupied'
    blocked = 'Blocked'