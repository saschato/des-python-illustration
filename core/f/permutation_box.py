class PBox:
    pbox = [
        16,7,20,21,29,12,28,17,
        1,15,23,26,5,18,31,10,
        2,8,24,14,32,27,3,9,
        19,13,30,6,22,11,4,25
    ]

    def permute(self,inp):
        if not len(inp) == 32:
            raise Exception

        return "".join([inp[bit-1] for bit in self.pbox])