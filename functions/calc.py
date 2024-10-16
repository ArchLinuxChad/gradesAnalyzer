#!/usr/bin/env python3

class Calc:
    def __init__(self, grades):
        self.grades = grades
        self.fails = 0
        self.passes = 0
        self.highs = 0
    def calc_states(self):
        for i in self.grades:
            if i < 3:
                self.fails += 1
            elif i >= 3 and i < 8:
                self.passes += 1
            elif i >= 8:
                self.highs += 1
    def get_fails(self):
        return self.fails
    def get_passes(self):
        return self.passes
    def get_highs(self):
        return self.highs
