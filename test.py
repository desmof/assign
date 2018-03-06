# -*- coding: utf-8 -*-
import os
import unittest
import calrender
import tex
import fizzbuzz

class UtilTestCase(unittest.TestCase):
    def setUp(self) :
        self.terry=tex.human(30,1000000,True)
    def test_fizz(self) :
        self.assertEqual(fizzbuzz.fbuzz(3),"fizz")
    def test_tex(self) :
        self.assertEqual(self.terry.tex_cal(),600000)
    def test_cal(self) :
        self.assertEqual(calrender.cal(800),u"윤년")


if __name__=="__main__" :
    unittest.main(verbosity=2)
                                                                                                                                                                                        
