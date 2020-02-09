ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_NUMS = {"I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ",("Q")),\
             "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE",("E")),\
            "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO",("V")),\
             "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB",("J")),\
              "V": ("VZBRGITYUPSDNHLXAWMJQOFECK",("Z")),\
             "VI": ("JPGVOUMFYQBENHZRDKASXLICTW",("Z","M")),\
            "VII": ("NZJHGRCXMYSWBOUFAIVLPEKQDT",("Z","M")),\
           "VIII": ("FKQHTLXOCBJSPDZRAMEWNIUYGV",("Z","M"))}
    
class Rotor():
    def __init__(self, rotor="I", initial_position="A", ring_setting="A", next_rotor=None, prev_rotor=None):
        assert initial_position in ALPHA, "'{}' is not a valid rotor starting position. Please enter any capital letter."
        assert ring_setting in ALPHA, "'{}' is not a valid ring setting. Please enter any capital letter.".format(ring_setting)
        assert rotor in ROTOR_NUMS.keys(), "Please enter a valid rotor type. Your choices are: {}".format(ROTOR_NUMS.keys())
        
        self.position = initial_position
        self.ring_setting = ring_setting
        self.next_rotor = next_rotor
        self.prev_rotor = prev_rotor
        
        self._change_rotor(rotor)
        
    def encrypt(self, letter, first):
        if first:
            self._turn()
            first = False
        new_letter = self.wiring[(ALPHA.index(letter)+ALPHA.index(self.position))%len(ALPHA)]
        encrypted = new_letter
        if self.next_rotor is not None:
            encrypted = self.next_rotor.encrypt(encrypted, first)
        return encrypted
    
    def back(self, letter):
        new_letter = ALPHA[self.wiring.index(letter)]
        encrypted = new_letter
        if self.prev_rotor is not None:
            encrypted = self.prev_rotor.back(encrypted)
        return encrypted
        
    def _change_rotor(self, rotor):
        self.rotor = rotor
        self.wiring = ROTOR_NUMS[self.rotor][0]
        self.turnovers = ROTOR_NUMS[self.rotor][1]
        
    def _turn(self):
        if self.next_rotor is not None and self.position in self.turnovers:
            self.next_rotor._turn()
            print("TURNING NEXT ROTOR")
        self.position = ALPHA[(ALPHA.index(self.position)+1)%len(ALPHA)]