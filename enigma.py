#!/usr/local/bin/python

import string

alphabit = string.ascii_uppercase

rotor_one = {'A':'F','B':'U','C':'J','D':'L','E':'N','F':'M','G':'E','H':'S','I':'A','J':'O','K':'I','L':'B','M':'W','N':'Q','O':'P','P':'H','Q':'G','R':'R','S':'Z','T':'D','U':'C','V':'V','W':'Y','X':'K','Y':'X','Z':'T'}

rotor_two = {'A':'X','B':'D','C':'H','D':'T','E':'O','F':'W','G':'R','H':'J','I':'E','J':'P','K':'A','L':'B','M':'I','N':'Y','O':'L','P':'C','Q':'F','R':'U','S':'G','T':'M','U':'V','V':'N','W':'S','X':'Q','Y':'K','Z':'Z'}

rotor_three = {'A':'V','B':'E','C':'D','D':'Z','E':'U','F':'Y','G':'L','H':'P','I':'Q','J':'S','K':'O','L':'K','M':'F','N':'H','O':'R','P':'C','Q':'X','R':'W','S':'J','T':'N','U':'M','V':'I','W':'G','X':'B','Y':'A','Z':'T'}

reflector = {'A':'R','B':'X','C':'Z','D':'S','E':'N','F':'V','G':'U','H':'Y','I':'T','J':'W','K':'Q','L':'P','M':'O','N':'E','O':'M','P':'L','Q':'K','R':'A','S':'D','T':'I','U':'G','V':'F','W':'J','X':'B','Y':'H','Z':'C'}

    
class Enigma(object):

    def shifting_forward(self, char, shift):
        index = alphabit.find(char)
        return alphabit[(index+shift)%26]
        
    def shifting_backward(self, char, shift):
        index = alphabit.find(char)
        return alphabit[(index-shift)%26]
        
    def rotor_reversed(self, rotor):
        return dict(zip(rotor.values(), rotor.keys()))

    def first_rotor_rotation(self, shift):
        return shift % 26
    
    def second_rotor_rotation(self, index):
        return index / 26

    def third_rotor_rotation(self, index):
        return index / 676

    def replacement(self, char, first_rotor_shift, second_rotor_shift, third_rotor_shift):
        step_one = self.shifting_forward(char, first_rotor_shift)
        step_two = rotor_one[step_one]
        step_three = self.shifting_backward(step_two, first_rotor_shift-second_rotor_shift)
        step_four = rotor_two[step_three]
        step_five = self.shifting_backward(step_four, second_rotor_shift-third_rotor_shift)
        step_six = rotor_three[step_five]
        step_seven = self.shifting_backward(step_six, third_rotor_shift) 
        step_eight = reflector[step_seven]
        step_nine = self.shifting_forward(step_eight, third_rotor_shift)
        step_ten =self. rotor_reversed(rotor_three)[step_nine]
        step_eleven = self.shifting_forward(step_ten, second_rotor_shift-third_rotor_shift)
        step_twelve = self.rotor_reversed(rotor_two)[step_eleven]
        step_thirteen = self.shifting_forward(step_twelve, first_rotor_shift-second_rotor_shift)
        step_forteen = self.rotor_reversed(rotor_one)[step_thirteen]
        step_fifteen = self.shifting_backward(step_forteen, first_rotor_shift)
        return step_fifteen

    def encode(self, text):
        result = ''
        for i in range(len(text)):
            first_rotor_shift = self.first_rotor_rotation(i+1)
            second_rotor_shift = self.second_rotor_rotation(i+1)
            third_rotor_shift = self.third_rotor_rotation(i+1)
            shift = first_rotor_shift
            result += self.replacement(text[i], first_rotor_shift, second_rotor_shift, third_rotor_shift)                
        return result

            
            
