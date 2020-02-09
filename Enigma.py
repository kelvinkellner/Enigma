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
# Imports
from Rotor import Rotor
from Reflector import Reflector

# USER VARIABLES

# Init switchboard
switchboard = "" # enter swaps in format 'AB,CD,EF..." (the real machine performed 10 swaps)

# Init Rotors
rotors = (Rotor(rotor="I"), Rotor(rotor="II"), Rotor(rotor="III", initial_position="Z"))
reflector = Reflector("B")

"""
--------------------------------------------------
Inner workings below...
--------------------------------------------------
"""

# Receive input message
message = input("Message: ")
encrypted = message.upper()


# Create list of individual switchboard swaps
sb = switchboard.split(",")

# Create tuples for each character swap
switches = []
while len(sb) > 0:
    s = sb.pop(0)
    if len(s)>=2:
        switches.append((s[0],s[1]))
    
# Run first pass through switchboard, swapping letters
for swap in switches:
    for i in range(len(encrypted)):
        if encrypted[i] == swap[0]:
            encrypted = encrypted[:i] + swap[1] + encrypted[i+1:]
        elif encrypted[i] == swap[1]:
            encrypted = encrypted[:i] + swap[0] + encrypted[i+1:]


# Set up rotor chain
for i in range(len(rotors)-1, 0, -1):
    rotors[i].next_rotor = rotors[i-1]
for i in range(len(rotors)-1):
    rotors[i].prev_rotor = rotors[i+1]
    
# Reflector should point to and from the leftmost rotor
reflector.next_rotor = rotors[0]
reflector.prev_rotor = rotors[0]
rotors[0].next_rotor = reflector

for i in range(len(encrypted)):
    encrypted = encrypted[:i] + rotors[-1].encrypt(encrypted[i], True) + encrypted[i+1:]

# Output final encrypted message
print(message.upper(), " -> ", encrypted)