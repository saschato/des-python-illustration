from core.initial_permutation import IP
from core.f.expansion_box import EBox
from core.f.substitution_boxes import SBoxes
from core.f.permutation_box import PBox
from core.key_schedule import SubKeys
from core.final_permutation import FP

from copy import deepcopy

class DES:
    def __init__(self,key):
        # loading required classes
        self.IP = IP()
        self.EBox = EBox()
        self.SBoxes = SBoxes()
        self.PBox = PBox()
        self.SubKeys = SubKeys(key)
        self.FP = FP()

    def length(self,inp,n):
        if len(inp) <= n:
            while len(inp) < n:
                inp = "0" + inp
        else:
            raise Exception
        return inp

    def f_function(self,right_site,key):
        # expansion box
        temp = self.EBox.expand(right_site)

        # xor of key and right site
        right_site = self.length(bin(int(temp,2)^int(key,2))[2:],48)

        temp,box = "",0
        # sboxes
        for i in range(0,48,6):
            temp += self.length(self.SBoxes.sbox(right_site[i:i+6],box),4)
            box += 1

        # permutation
        return self.PBox.permute(temp)

    def split_plaintext(self,plaintext):
        return plaintext[0:32],plaintext[32:64]

    def main(self,inp):
        # raising exception if length or key or plaintext != 64
        if not len(inp) == 64:
            raise Exception

        # initial permutation
        inp = self.IP.permute(inp)

        # splitting plaintext into two 32bit parts
        left_site,right_site = self.split_plaintext(inp)

        for i in range(0,16):
            temp_right_site = self.f_function(right_site,self.SubKeys.generate())

            # xor of current leftside and rightside after f function
            temp_left_site = self.length(bin(int(left_site,2)^int(temp_right_site,2))[2:],32)

            # changing sites
            left_site = deepcopy(right_site)
            right_site = deepcopy(temp_left_site)

        print(hex(int(self.FP.permute(right_site+left_site),2)))

if __name__ == "__main__":
    DES = DES("0111000001100001011100110111001101110111011011110111001001100100")
    DES.main("0"+bin(int(b"password".hex(),16))[2:])
