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


doc_hash = sha3_512("doc0")
nonce = sha3_512("nonce0")
request_hash = sha3_512(concat(sort(doc_hash, nonce)))
print "New-Tokimark RPC Request:"
print "e0/tokimark-new", lower_hex(request_hash)
print
hash0a = request_hash
hash0b = sha3_512("arbitrary0")
hash1a = sha3_512(concat(sort(hash0a, hash0b)))
hash1b = sha3_512("arbitrary1")
root = sha3_512(concat(sort(hash1a, hash1b)))
timestamp = struct.pack('!Q', 1634944730)
dayblock = sha3_512("previous0") + sha3_512("peer0") + sha3_512("peer1") + root + timestamp
block_hash = sha3_512(dayblock)
print "Response:"
print "e0/tokimark", lower_hex(hash0a + hash0b + hash1b), lower_hex(dayblock)
print
print "Tokimark:"
print "e0/tokimark", lower_hex(doc_hash + nonce + hash0b + hash1b), lower_hex(dayblock)
print

print "Get-Containing-Block Request:"
print "e0/tokimark-get-containing-block", lower_hex(block_hash) + lower_hex(timestamp)
print
c_timestamp = struct.pack('!Q', 1634947201)
c_block = sha3_512("previous1") + block_hash + sha3_512("peer2") + sha3_512("peer3") + sha3_512("root") + c_timestamp
print "Response:"
print "e0/tokimark-block", lower_hex(c_block)
print

print "Get-Daymark Request:"
print "e0/tokimark-get-daymark", lower_hex(timestamp)
print
hash0a = sha3_512(dayblock)
hash0b = sha3_512("arbitrary2")
hash1a = sha3_512(concat(sort(hash0a, hash0b)))
hash1b = sha3_512("arbitrary3")
root = sha3_512(concat(sort(hash1a, hash1b)))
dayblock_timestamp = struct.pack('!Q', 1634947200)
dayblock = sha3_512("previous2") + sha3_512("peer4") + sha3_512("peer5") + root + dayblock_timestamp
print "Response:"
print "e0/tokimark", lower_hex(hash0a + hash0b + hash1b), lower_hex(dayblock)
print

print "Get-Dayblock Request:"
print "e0/tokimark-get-dayblock", lower_hex(timestamp)
print
print "Response:"
print "e0/tokimark-block", lower_hex(dayblock)
print
