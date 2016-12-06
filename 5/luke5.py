import hashlib

m = hashlib.md5()

result = []

for i in range(10000000,99999999):
    streng = "wtnhxymk" + str(i)
    m.update(streng)
    h = m.hexdigest()
    if h[0:5] == '00000':
        result.append(h[5])
    if len(result) > 8:
        break
print result

