#!/usr/bin/python3
import uuid

#  This function generates a random UUID.
random_uuid = uuid.uuid4()
print(random_uuid)
print("=" * 50)
# ----------------------------------------
# that function will print typical mac address of your device
random_uuid_mac = uuid.getnode()
print(random_uuid_mac)
print("=" * 50)
# -----------------------------------------
# node=None, clock_seq=None): This function generates
# UUID using a host ID, sequence number, and the current time
random_uuid1 = uuid.uuid1()  #
print(random_uuid1)
print("=" * 50)
# ------------------------------------------------
# This function generates a UUID using the MD5 hash of a
# namespace identifier (which is a UUID) and a name (which is a string)
random_uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, "Meow")
print(random_uuid3)
print("=" * 50)
# ------------------------------------------------------
# This function generates a UUID using the SHA-1 hash of a
# namespace identifier (which is a UUID) and a name (which is a string)
random_uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "Meow")
print(random_uuid5)
print("=" * 50)
# --------------------------------------------------------
