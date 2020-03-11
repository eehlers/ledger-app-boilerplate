#!/usr/bin/env python

from ledgerblue.comm import getDongle
from binascii import hexlify, unhexlify

account_number = "12345"

account = '{:08x}'.format(int(account_number))

# Create APDU message.
# CLA 0xE0
# INS 0x02  GET_ADDRESS
# P1 0x01   USER CONFIRMATION REQUIRED (0x00 otherwise)
# P2 0x00   UNUSED
# Ask for confirmation
# txt = "E0020100" + '{:02x}'.format(len(donglePath) + 1) + '{:02x}'.format( int(len(donglePath) / 4 / 2)) + donglePath
# No confirmation
#apduMessage = "E0030100" + '{:02x}'.format(len(account) + 1) + account
hash1 = "1ae450e248537de7092a6d295522b5c610bf4412f7bc557c7dcc0cda82550a6f"
apduMessage = "E003" + hash1
apdu = bytearray.fromhex(apduMessage)

print("Request Address")

dongle = getDongle(True)
result = dongle.exchange(apdu)

#print("Address received: " + result.decode("utf-8"))
print("Address received: " + hexlify(result))

