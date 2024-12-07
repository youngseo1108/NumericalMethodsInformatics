# Method 1. without any module
# Method 1-1
print(0.3 == 0.3)
# METHOD 1-2
print(0.1 + 0.2 == 0.30000000000000004)


# METHOD 2. Using the module 
from decimal import *

getcontext().prec = 1 # Set a precision of the decimal number

# Method 2-1
print(Decimal(0.1) + Decimal(0.2) == Decimal('0.3'))
# Method 2-2
print(Decimal(0.1) + Decimal(0.2) == Decimal((0, (0, 3), -1)))



# getcontext()
#Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
#        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
#        InvalidOperation])



#print(Decimal(0.1) + Decimal(0.2) == Decimal(0, (0, 3), -1))
#print(Decimal((0, (0, 3), -1)))
#print(0.1+0.2)
#print(0.1)
#print(0.2)
#print(0.3)
#print(round(0.1,1) + round(0.2, 1) == round(0.3, 1))