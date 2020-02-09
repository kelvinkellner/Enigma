"""
--------------------------------------------------
Enigma Machine
--------------------------------------------------
Built by Kelvin Kellner
--------------------------------------------------
Github Project Repo:
https://github.com/kelvinkellner/Enigma
--------------------------------------------------
"""

# USER VARIABLES
switchboard = "AK,BD,EF,GL,PR,CX,WM,QO,IU,YH" # enter swaps in format 'AB,CD,EF..." (the real machine performed 10 swaps)

"""
--------------------------------------------------
Inner workings below...
--------------------------------------------------
"""

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Receive input message
message = input("Message: ")
encrypted = message.upper()

# Create list of individual switchboard swaps
sb = switchboard.split(",")

# Create tuples for each character swap
switches = []
while len(sb) > 0:
    s = sb.pop(0)
    switches.append((s[0],s[1]))
    
# Run first pass through switchboard, swapping letters
for swap in switches:
    for i in range(len(encrypted)):
        if encrypted[i] == swap[0]:
            encrypted = encrypted[:i] + swap[1] + encrypted[i+1:]
        elif encrypted[i] == swap[1]:
            encrypted = encrypted[:i] + swap[0] + encrypted[i+1:]

# Output final encrypted message
print(message.upper(), " -> ", encrypted)