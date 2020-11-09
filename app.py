# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:00:31 2020

@author: markl
"""
import streamlit as st
import numpy as np
import pandas as pd
import io
import requests

st.title("Welcome to my website")
st.subheader("Mark Lu (marklu@gmail.com)")
st.text("Some text here")

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

url_campus_stu_enr_count_1999_2018="https://raw.githubusercontent.com/marklu729/streamlit_web_heroku/main/data/annual_count_percent_district_1999_2018.csv"
s_campus_stu_enr_count_1999_2018=requests.get(url_campus_stu_enr_count_1999_2018).content
campus_stu_enr_count_1999_2018=pd.read_csv(io.StringIO(s_campus_stu_enr_count_1999_2018.decode('utf-8')))
st.dataframe(campus_stu_enr_count_1999_2018.head())

import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Introduction
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Mark Lu
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Projects
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            1. Data automation
            2. P-12 Student Enrollment Distribution
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)

