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


hash0a = sha3_512("doc0")
hash0b = sha3_512("doc_nonce")
hash1a = sha3_512(concat(sort(hash0a, hash0b)))
hash1b = sha3_512("arbitrary0")
hash2a = sha3_512(concat(sort(hash1a, hash1b)))
hash2b = sha3_512("arbitrary1")
root = sha3_512(concat(sort(hash2a, hash2b)))

previous = sha3_512("previous")
peer0 = sha3_512("peer0")
peer1 = sha3_512("peer1")
block_nonce = sha3_512("block_nonce")
timestamp = struct.pack('!Q', 1634944730)

print "e0/tokimark",
print lower_hex(hash0a) + lower_hex(hash0b) + lower_hex(hash1b) + lower_hex(hash2b) + lower_hex(root),
print lower_hex(previous) + lower_hex(peer0) + lower_hex(peer1) + lower_hex(block_nonce) + lower_hex(timestamp)
