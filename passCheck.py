def lowerCheck(password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    strength = [x for x in lower if x in password]
    return len(strength)/26

def passCheck(password):
    strength = 0
