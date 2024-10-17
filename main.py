#!/usr/bin/env python3

## IMPORTS ##
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import vars
from functions import Calc
from functions import Pie

st.set_page_config(page_title="Grades Data Tracker")

st.title("Grades Data Tracker")

with st.container():
    col_sub, col_grade = st.columns(2)
    with col_sub:
        sub1 = st.selectbox("Subject 1", vars.subjects, index=None, placeholder="Please enter a subject")
        sub2 = st.selectbox("Subject 2", vars.subjects, index=None, placeholder="Please enter a subject")
        sub3 = st.selectbox("Subject 3", vars.subjects, index=None, placeholder="Please enter a subject")
        sub4 = st.selectbox("Subject 4", vars.subjects, index=None, placeholder="Please enter a subject")
        sub5 = st.selectbox("Subject 5", vars.subjects, index=None, placeholder="Please enter a subject")
        sub6 = st.selectbox("Subject 6", vars.subjects, index=None, placeholder="Please enter a subject")
        sub7 = st.selectbox("Subject 7", vars.subjects, index=None, placeholder="Please enter a subject")
        sub8 = st.selectbox("Subject 8", vars.subjects, index=None, placeholder="Please enter a subject")
        sub9 = st.selectbox("Subject 9", vars.subjects, index=None, placeholder="Please enter a subject")
        sub10 = st.selectbox("Subject 10", vars.subjects, index=None, placeholder="Please enter a subject")
    with col_grade:
        grade1 = st.selectbox("Grade 1", vars.grades, index=None, placeholder="Please choose a grade")
        grade2 = st.selectbox("Grade 2", vars.grades, index=None, placeholder="Please choose a grade")
        grade3 = st.selectbox("Grade 3", vars.grades, index=None, placeholder="Please choose a grade")
        grade4 = st.selectbox("Grade 4", vars.grades, index=None, placeholder="Please choose a grade")
        grade5 = st.selectbox("Grade 5", vars.grades, index=None, placeholder="Please choose a grade")
        grade6 = st.selectbox("Grade 6", vars.grades, index=None, placeholder="Please choose a grade")
        grade7 = st.selectbox("Grade 7", vars.grades, index=None, placeholder="Please choose a grade")
        grade8 = st.selectbox("Grade 8", vars.grades, index=None, placeholder="Please choose a grade")
        grade9 = st.selectbox("Grade 9", vars.grades, index=None, placeholder="Please choose a grade")
        grade10 = st.selectbox("Grade 10", vars.grades, index=None, placeholder="Please choose a grade")
    if st.button("Submit"):
        subs = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10]
        double = False
        for i in range(0, 10):
            if i < 4:
                if subs[i] == subs[i+1]:
                    double = True
        if double == True:
            st.error("You can't eneter two of the same subjects")
        else:
            st.success("Data Submitted")
            # Make DataFrame for bar chart to be plotted
            df = pd.DataFrame({
                'Subjects' : [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10],
                'Grades' : [grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10]
            })

            # plot bar chart
            st.bar_chart(df, x='Subjects', y='Grades', height=600)
            # put all grades into an array
            grades = [grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10]
            stats = Calc(grades)
            stats.calc_states()
            # Get numbers for fails, passes, and high grade
            fails = stats.get_fails()
            passes = stats.get_passes()
            highs = stats.get_highs()
            # total amount of grades
            # Show numbers
            total = fails + passes
            st.title("You are on track to")
            st.header(f"You got {fails} fails.")
            st.header(f"You got {passes} passes.")
            st.header(f"You got {highs} High Grades.")
            # plot pie chart
            pie = Pie(fails, passes, highs, total)
            pie.percent()
            pie.plot_chart()
