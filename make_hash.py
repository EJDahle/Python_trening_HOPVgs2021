import hashlib
h = hashlib.sha1(b'Svenskene bruker IKEA til aa infiltrere Norge. Vi maa forberede oss!').hexdigest()
print(h)
