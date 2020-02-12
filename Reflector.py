ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

REFLECTOR_NUMS = {"A":"EJMZALYXVBWFCRQUONTSPIKHGD",\
                  "B":"YRUHQSLDPXNGOKMIEBFZCWVJAT",\
                  "C":"FVPJIAOYEDRZXWGCTKUQSBNMHL"}

class Reflector():
    def __init__(self, reflector="B", next_rotor=None):
        assert reflector in REFLECTOR_NUMS.keys(), "Please enter a valid reflector type. Your choices are: {}".format(REFLECTOR_NUMS.keys())
        
        self.reflector = reflector
        self.next_rotor = next_rotor
        self.position = "A"
        self.ring_setting = "A"
        
        self.wiring = REFLECTOR_NUMS[self.reflector]
        
    def encrypt(self, letter, _):
        new_letter = self.wiring[ALPHA.index(letter)]
        encrypted = new_letter
        print("REFLECTOR", encrypted)
        if self.next_rotor is not None:
            encrypted = self.next_rotor.back(encrypted)
        return encrypted
    
    def _turn(self):
        return