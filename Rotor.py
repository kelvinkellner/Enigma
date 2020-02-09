class Rotor():
    ROTOR_NUMS = {"I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",\
                  "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",\
                  "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",\
                  "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",\
                  "V": "VZBRGITYUPSDNHLXAWMJQOFECK",\
                  "VI": "JPGVOUMFYQBENHZRDKASXLICTW",\
                  "VII": "JPGVOUMFYQBENHZRDKASXLICTW",\
                  "VIII": "FKQHTLXOCBJSPDZRAMEWNIUYGV"}
    
    def __init__(self, initial_position, rotor="I", ring_setting=1):
        assert 0 < ring_setting < 27, "'{}' is not a valid ring setting. Enter a number from 1-26.".format(ring_setting)
        
        self.rotor = rotor
        self.position = initial_position
        self.ring_setting = ring_setting
        
r = Rotor("A")