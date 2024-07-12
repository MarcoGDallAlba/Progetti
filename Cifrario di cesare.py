#!/usr/bin/python
key = int(raw_input('inserire valore della chiave:'))
def cryc(s):
    s = s.lower()
    s = s.replace('è','e').replace('é','e').replace('à','a').replace('ì','i').replace('ù','u').replace('ò','o')
    z = [s[i] for i in range(0,len(s))]
    for i in range(0,len(z)):
        if ord(z[i]) in range(97,123):
            z[i] = chr((ord(z[i][0])-97+key)%26+97)
    code = ''.join(z)
    print code

def decryc(s):
    s = s.lower()
    z = [s[i] for i in range(0,len(s))]
    for i in range(0,len(z)):
        if ord(z[i]) in range(97,123):
            z[i] = chr((ord(z[i][0])-97-key)%26+97)
    sentence = ''.join(z)
    print sentence
