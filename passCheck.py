alpha = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
nalphanum = ".,/?><';:-_+!@#$%^&*"

def lowerCheck(password):
    lower = alpha
    strength = 1 in [1 for x in lower if x in password]
    return strength

def upperCheck(password):
    upper = alpha.upper()
    strength = 1 in [1 for x in upper if x in password]
    return strength

def numCheck(password):
    strength = 1 in [1 for x in num if x in password]
    return strength

def nalphanumCheck(password):
    strength = 1 in [1 for x in nalphanum if x in password]
    return strength

def passCheck(password):
    strength = 0
    strengthL = [lowerCheck(password),upperCheck(password),numCheck(password),nalphanumCheck(password)]
    for x in strengthL:
        if x:
            strength += 2
    if strengthL[0] and strengthL[1]:
        strength += 2
    return strength

print "justlower:"
print passCheck("justlower")
print "justBOTHALPHA:"
print passCheck("justBOTHALPHA")
print "justl0w3randnum:"
print passCheck("justl0w3randnum")
print "justlowerand!@#$:"
print passCheck("justlowerand!@#$")
print "All0fThem!:"
print passCheck("All0fThem!")
