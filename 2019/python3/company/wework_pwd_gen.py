# Problem: implement a password generator, such that the user of the implementation
# can choose the length of the password (min, max), whether the password should include
# numbers, upper case letters, symbols.

# Non-functional req: it should be difficult for an attacker to guess a password given
# full knowledge of the implementation.

# Symbols: "!@#$%^&*"

import random

class Generator():
    def __init__(self):
        self.password = []
        self.all_nums = "0123456789"
        self.all_uchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.all_lchars = "abcdefghijklmnopqrstuvwxyz"
        self.all_syms = "!@#$%^&*"
    
    def pwd_gen(self, min_len, max_len, use_num=False, use_chars=False, use_syms=False):
        
        if max_len <= 0 or min_len > max_len:
            return ''
        
        
        char_list = self.all_lchars
        
        if use_num:
            char_list += self.all_nums
            
        if use_chars:
            char_list += self.all_uchars
        
        if use_syms:
            char_list += self.all_syms
        
        
        self.password = []
        # returns the pasword
        cur_len = random.random() * (max_len - min_len)
        cur_len = int(min_len + cur_len)
        
        ch_sz = len(char_list)
        for i in range(cur_len):
            idx = int(random.random() * ch_sz)
            self.password.append(char_list[idx])
        
        return (''.join(c for c in self.password))

gen = Generator()
print(gen.pwd_gen(20, 40, True, True, True))
print(gen.pwd_gen(20, 40))
print(gen.pwd_gen(20, 40, False, True, True))
print(gen.pwd_gen(0, 0))
print(gen.pwd_gen(0, 1))

