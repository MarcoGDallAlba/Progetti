#!/usr/bin/python

def cry(s):
    k = 'luna'
    s = s.lower()
    s = s.replace('è','e').replace('é','e').replace('à','a').replace('ì','i').replace('ù','u').replace('ò','o')
    t = 0
    z = [s[i] for i in range(0,len(s))]
    for i in range(0,len(z)):
        if ord(z[i]) in range(97,123):
            z[i] =chr((ord(z[i][0])-194+ord(k[t%4]))%26+97)
            t += 1
        else:
            t += 0
    code = ''.join(z)
    print code

def decry(s):
    k = 'luna'
    s = s.lower()
    t = 0
    z = [s[i] for i in range(0,len(s))]
    for i in range(0,len(z)):
        if ord(z[i]) in range(97,123):
            z[i] =chr((ord(z[i][0])-ord(k[t%4]))%26+97)
            t += 1
        else:
            t += 0
    sentence = ''.join(z)
    print sentence
    

