"""
3 wheels, 5 options each, different sizes
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Receive input message
message = input("Message: ")
message = message.upper()

# Convert message into integers based on position in the alphabet
encrypted = []
for char in message:
    if char in alpha:
        encrypted.append(alpha.index(char))
    else:
        encrypted.append(char)

# Open switchboard file for character swaps
txt = open("Switchboard.txt", "r")
txt = txt.read().split()

# Create tuples for each character swap
switches = []
while len(txt) > 0:
    s = txt.pop(0).split("-")
    switches.append((alpha.index(s[0]), alpha.index(s[1])))

# Perform first character swap
for swap in switches:
    for i in range(len(encrypted)):
        if encrypted[i] == swap[0]:
            encrypted[i] = swap[1]
        elif encrypted[i] == swap[1]:
            encrypted[i] = swap[0]



# Output final encrypted message    
out = ""
for i in range(len(encrypted)):
    out += alpha[encrypted[i]]
print(message, " -> ", out)