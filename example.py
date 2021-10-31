#!python2.7
import binascii
import hashlib
import struct


def concat(a):
    return "".join(a)


def sort(a, b):
    return sorted([a, b])


def sha3_512(a):
    return hashlib.sha512(a).digest()


def lower_hex(a):
    return binascii.hexlify(a)


# New-Tokimark Request
doc_hash = sha3_512("doc0")
nonce = sha3_512("nonce0")
print "e0/tokimark-new", lower_hex(doc_hash + nonce)

# Tokimark
hash0a = doc_hash
hash0b = nonce
hash1a = sha3_512(concat(sort(hash0a, hash0b)))
hash1b = sha3_512("arbitrary0")
hash2a = sha3_512(concat(sort(hash1a, hash1b)))
hash2b = sha3_512("arbitrary1")
root = sha3_512(concat(sort(hash2a, hash2b)))
timestamp = struct.pack('!Q', 1634944730)
block = sha3_512("previous0") + sha3_512("peer0") + sha3_512("peer1") + root + timestamp
print "e0/tokimark", lower_hex(hash0a + hash0b + hash1b + hash2b), lower_hex(block)

# Daymark
hash0a = sha3_512(block)
hash0b = sha3_512("nonce1")
hash1a = sha3_512(concat(sort(hash0a, hash0b)))
hash1b = sha3_512("arbitrary2")
hash2a = sha3_512(concat(sort(hash1a, hash1b)))
hash2b = sha3_512("arbitrary3")
root = sha3_512(concat(sort(hash2a, hash2b)))
timestamp = struct.pack('!Q', 1634947200)
block = sha3_512("previous1") + sha3_512("peer2") + sha3_512("peer3") + root + timestamp
print lower_hex(hash0a + hash0b + hash1b + hash2b), lower_hex(block)
