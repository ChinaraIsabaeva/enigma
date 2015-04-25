#!/usr/local/bin/python

import unittest
from enigma import Enigma, Rotor, shifting_forward, shifting_backward

rotor_one = {"A":"F","B":"U","C":"J","D":"L","E":"N","F":"M","G":"E","H":"S","I":"A","J":"O","K":"I","L":"B","M":"W","N":"Q","O":"P","P":"H","Q":"G","R":"R","S":"Z","T":"D","U":"C","V":"V","W":"Y","X":"K","Y":"X","Z":"T"}

rotor_two = {"A":"X","B":"D","C":"H","D":"T","E":"O","F":"W","G":"R","H":"J","I":"E","J":"P","K":"A","L":"B","M":"I","N":"Y","O":"L","P":"C","Q":"F","R":"U","S":"G","T":"M","U":"V","V":"N","W":"S","X":"Q","Y":"K","Z":"Z"}

rotor_three = {"A":"V","B":"E","C":"D","D":"Z","E":"U","F":"Y","G":"L","H":"P","I":"Q","J":"S","K":"O","L":"K","M":"F","N":"H","O":"R","P":"C","Q":"X","R":"W","S":"J","T":"N","U":"M","V":"I","W":"G","X":"B","Y":"A","Z":"T"}

reflector = {"A":"R","B":"X","C":"Z","D":"S","E":"N","F":"V","G":"U","H":"Y","I":"T","J":"W","K":"Q","L":"P","M":"O","N":"E","O":"M","P":"L","Q":"K","R":"A","S":"D","T":"I","U":"G","V":"F","W":"J","X":"B","Y":"H","Z":"C"}


class TestEnigmaFunctions(unittest.TestCase):
    def setUp(self):
        self.char = 'W'
        self.first_rotor_shift = 6
        self.second_rotor_shift = 0
        self.third_rotor_shift = 0

    def test_replacement(self):
        rotor = Rotor()
        encoded_char = Enigma().replacement(self.char, self.first_rotor_shift, self.second_rotor_shift, self.third_rotor_shift)
        self.assertEqual(encoded_char, 'L')


class TestEncoding(unittest.TestCase):
    def setUp(self):
        self.text = 'PZD'
        self.cipher = 'BEC'

    def test_encoding(self):
        encoded_text = Enigma().encode(self.text)
        self.assertEqual(encoded_text, self.cipher)
        
    def test_decoding(self):
        decoded_text = Enigma().encode(self.cipher)
        self.assertEqual(decoded_text, self.text)


class TestEncodingSecondRotorMove(unittest.TestCase):
    def setUp(self):
        self.text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
        self.cipher = 'CRDJLGDMARVHPJGWREDOHJCYVEIOM'

    def test_encoding(self):
        encoded_text = Enigma().encode(self.text)
        self.assertEqual(encoded_text, self.cipher)
        
    def test_decoding(self):
        decoded_text = Enigma().encode(self.cipher)
        self.assertEqual(decoded_text, self.text)


class TestEncodingThirdRotorMove(unittest.TestCase):
    def setUp(self):
        self.text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABC'
        self.cipher = 'CRDJLGDMARVHPJGWREDOHJCYVEIOMXXEWQGOPPNCXIDAYRNARYJMXGIGODTAXGCJFUVMZLQKQKFJPOMKVRNREYWINVQRUYDZTFFMYPJGZSQRVNIIFZPRIYWEYOZWWDDBSRGLOAUKOSDBXYBZPTDVXNZQVAJMXZSWTULLHGCTADVMJLUKIZLSMLTMKHCOUXSTNHNCINGMNUFLRHQBUOMZXPWVAWZINCYBNHDBPHRMTRGFWCQORVHBDMHFINIMUUZLISZCWTJORVBOKPNNKPFDVILVFBEIKSHNHESLYDHSGHLIEQAYUQDTSSCQOOMYXWWSCDJKDBRKFXKIEWQATBUQFKPWZBMWTSSQAUXFHLYWPRFPJHLOMVSIQHORADLAVSADLBLGOPJPEPWLFEHHIHFUNHENUPQTFSCWRIZIYNXGKAXOZKWEKOLWWDTBUFDUPRGGMAGCXPBZHCATYZOJVJGSHZSLTYLDGSTPHFTVSBYGPXIUWFDMKGCXUMUCZTTMYBNHCBOPMMVTFPEFWOFMAUHQVXINAMDUXLAORLTDBOJVKGMTQTKPCRGJHSYBEIUAPFWCQERFBERAFUYBNHOBQAFCKOMNHTSEYFBIYEYGFDLIOVZAGQURGKVQNYEROBIWPJGWBEIOXXCFXRGKVINEEVVBGNLIYBNHFBPASENSHGI'

    def test_encoding(self):
        encoded_text = Enigma().encode(self.text)
        self.assertEqual(encoded_text, self.cipher)
        
    def test_decoding(self):
        decoded_text = Enigma().encode(self.cipher)
        self.assertEqual(decoded_text, self.text)


class TestSecondRotorRotation(unittest.TestCase):
    def test_second_rotor_zero(self):
        index = 1
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 0)

    def test_second_rotor_zero_another_case(self):
        index = 25
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 0)

    def test_second_rotor_rotate_one_letter(self):
        index = 26
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 1)

    def test_second_rotor_rotate_one_letter_another_case(self):
        index = 51
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 1) 
    
    def test_second_rotor_rotate_two_letter(self):
        index = 52
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 2) 
        
    def test_second_rotor_rotate_two_letter_another_case(self):
        index = 77
        result = Rotor().second_rotor_rotation(index)
        self.assertEqual(result, 2) 

class TestThirdRotorRotation(unittest.TestCase):
    def test_third_rotor_zero(self):
        index = 0
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 0)

    def test_third_rotor_zero_another_case(self):
        index = 675
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 0)

    def test_third_rotor_rotate_one_letter(self):
        index = 676
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 1)

    def test_third_rotor_rotate_one_letter_another_case(self):
        index = 1351
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 1) 
    
    def test_third_rotor_rotate_two_letter(self):
        index = 1352
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 2) 
        
    def test_third_rotor_rotate_two_letter_another_case(self):
        index = 2027
        result = Rotor().third_rotor_rotation(index)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
