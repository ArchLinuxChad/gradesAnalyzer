#!/usr/bin/env python3

import matplotlib.pyplot as plt
import streamlit as st

class Pie:
    def __init__(self, fails, passes, highs, total):
        self.fails = fails
        self.passes = passes
        self.highs = highs
        self.total = total
    def percent(self):
        self.fail = (self.fails / self.total) * 100
        self.pass_ = (self.passes / self.passes) * 100
        self.high = (self.passes / self.passes) * 100
    def plot_chart(self):
        self.sizes = [self.fail, self.pass_, self.high]
        self.labels = ["Fails", "Passes", "Highs"]
        fig1, ax1 = plt.subplots()
        ax1.pie(self.sizes, labels=self.labels,
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
