import base64
string = "IyEvYmluL2Jhc2gKYmFzaCAtaSA+JiAvZGV2L3RjcC9DVVNUT01fSVAvNDQzIDA+JjE="
test = "blestsploit"
v = base64.b64encode(test.encode('utf-8'))
print(base64.b64decode(string))
print(base64.b64encode(test.encode('utf-8')))
print(v.decode('utf-8'))