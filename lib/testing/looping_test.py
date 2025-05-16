#!/usr/bin/env python3

from looping import happy_new_year, square_integers, fizzbuzz

import io
import sys

class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
        #answer.split(\n) produces a list that ends in ''
        answer_list = answer.split('\n')
        #second to last value should be the HNY string
        
        digit_strings = [str(i) for i in range(1,11)]
        remaining_digits = [i for i in digit_strings if i not in answer_list] 
       

class TestSquareIntegers:
    '''square_integers() in looping.py'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        
        
class TestFizzBuzz:
    '''fizzbuzz() in looping.py'''

    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fizzbuzz()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
       
        
        i = 1
        for line in answer.split('\n'):
            if(line): #answer.split(\n) produces a list that ends in ''
                if i % 15 == 0: assert line == "FizzBuzz", f"Should have printed 'Buzz' when number is {i}, got {line} instead"
                elif i % 3 == 0: assert line == "Fizz", f"Should have printed 'Fizz' when number is {i}, got {line} instead"
                elif i % 5 == 0: assert line == "Buzz", f"Should have printed 'Buzz' when number is {i}, got {line} instead"
                else: assert str(i) == line, f"Should have printed {i}, got {line} instead"
                i += 1
        
        i = i - 1
    
