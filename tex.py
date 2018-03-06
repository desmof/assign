# -*- coding: utf-8 -*-

class human :
    age = 0
    earn = 0
    baby = False

    def __init__(self,age,earn,baby):
        self.age = age
        self.earn = earn
        self.baby = baby
    def tex_cal(self):
        tex_pay = 0
        if self.age > 16 and self.age < 60 :
            if self.earn < 20000 :
                tex_pay = self.earn/5
            else : 
                tex_pay = self.earn/2
            if self.baby == True :
                return tex_pay + self.earn/10
            else :
                return tex_pay
        else:
            return self.earn




