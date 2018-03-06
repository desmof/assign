# -*- coding: utf-8 -*-

def cal(year) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return u"윤년"
            return u"평년"
        return u"윤년"

