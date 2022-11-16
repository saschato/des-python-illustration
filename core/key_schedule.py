class SubKeys:
    permuted_choice_1 = [
        57,49,41,33,25,17,9,1,
        58,50,42,34,26,18,10,2,
        59,51,43,35,27,19,11,3,
        60,52,44,36,63,55,47,39,
        31,23,15,7,62,54,46,38,
        30,22,14,6,61,53,45,37,
        29,21,13,5,28,20,12,4
    ]

    permuted_choice_2 = [
        14,17,11,24,1,5,3,28,
        15,6,21,10,23,19,12,4,
        26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,
        51,45,33,48,44,49,39,56,
        34,53,46,42,50,36,29,32
    ]

    def __init__(self,key):
        self.base_key = key
        self.main_key = self.permute_1()
        self.left = None
        self.right = None
        self.round = 1
        self.shift_one = [1,2,9,16]

    def permute_1(self):
        return "".join([self.base_key[bit-1] for bit in self.permuted_choice_1])

    def permute_2(self,out):
        return "".join([out[bit-1] for bit in self.permuted_choice_2])
    
    def split_into_halfes(self):
        return self.main_key[0:28],self.main_key[28:56]

    def length(self,inp,n):
        if not len(inp) == n:
            while len(inp) < n:
                inp = "0" + inp
        return inp

    def transformation(self):
        if self.round in self.shift_one:
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]
        else:
            self.left = self.left[2:] + self.left[0:2]
            self.right = self.right[2:] + self.right[0:2]

        self.round += 1

    def generate(self):
        if self.left is None or self.right is None:
            self.left,self.right = self.split_into_halfes()
    
        self.transformation()

        return self.permute_2(self.left+self.right)

if __name__ == "__main__":
    sb = SubKeys("0000110001110011010000100010000001000011000110000111000111011101")
    for i in range(16):
        print(sb.generate())
