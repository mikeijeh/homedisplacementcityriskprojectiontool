import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="City Low-Income Displacement Risk Projection Tool")

st.title("City Low-Income Displacement Risk Projection Tool")

st.header("**Location**")
st.subheader("City and State")
colrisk1, colrisk2 = st.columns(2)

with colrisk1:
    city = st.text_input("Enter your City: ", "City name")
with colrisk2:
    state = st.text_input("Enter your State Initials: ", "State initials")

st.header("**Population and Poverty**")

link1 = '[Look up census data](https://www.census.gov/quickfacts/fact/table/US/PST045219)'
st.markdown(link1, unsafe_allow_html=True)

colrisk1, colrisk2 = st.columns(2)

with colrisk1:
    st.subheader("Population Change")
    pop_change = st.number_input("Enter Population Change %: ", min_value=-100.0,format='%f' )
    
    st.subheader("Poverty Rate")
    percent_poverty = st.number_input("Enter Poverty Rate %: ", min_value=0.0,format='%f' )
    
    st.subheader("Population Per Square Mile")
    pop_per_sq_mile = st.number_input("Enter your Population Per Square Mile: ", min_value=0.0,format='%f' ) 
     

st.markdown("---")

st.header("**Zillow Data**")

link2 = '[Look up Zillow Data](https://www.zillow.com/home-values/)'
st.markdown(link2, unsafe_allow_html=True)

colrisk1, colrisk2 = st.columns(2)
with colrisk1:
    st.subheader("Zillow Home Value Today")
    home_value_today = st.number_input("Enter Today's Home Value: ", min_value=0.0,format='%f') 
    
    st.subheader("Zillow Home Value 5 Years Ago")
    home_value_5_yrs_ago = st.number_input("Enter Home Value 5 Years Ago: ", min_value=1.0,format='%f')
    
home_value_change = home_value_today/home_value_5_yrs_ago - 1
x1 = home_value_change * 0.5908
pop_change = pop_change/100
x2 = pop_change * 2.6275
percent_poverty = percent_poverty/100
x3 = percent_poverty * 3.5809
x4 = pop_per_sq_mile * 0.00003345
pred_score = -0.174 + x1 + x2 + x3 + x4

st.header("Risk Rating for " + str(city) + ", " + str(state))
colrisk1, colrisk2 = st.columns(2)
with colrisk1:
    if pred_score > 1.25:
        pred_rank = '<p style="font-family:sans serif; color:Red; font-size: 48px;">Overall risk is High</p>'
        st.markdown(pred_rank, unsafe_allow_html=True)
    elif pred_score > 0.95:
        pred_rank = '<p style="font-family:sans serif; color:Black; font-size: 48px;">Overall risk is Medium</p>'
        st.markdown(pred_rank, unsafe_allow_html=True)
    else:
        pred_rank = '<p style="font-family:sans serif; color:Green; font-size: 48px;">Overall risk is Low</p>'
        st.markdown(pred_rank, unsafe_allow_html=True)


with colrisk2:
    st.subheader("Risk Subcategories")
    if home_value_change > 0.4:
        hv_rank = '<p style="font-family:sans serif; color:Red; font-size: 24px;">Home value change: High</p>'
        st.markdown(hv_rank, unsafe_allow_html=True)
    elif home_value_change > 0.2:
        hv_rank = '<p style="font-family:sans serif; color:Black; font-size: 24px;">Home value change: Medium</p>'
        st.markdown(hv_rank, unsafe_allow_html=True)
    else:
        hv_rank = '<p style="font-family:sans serif; color:Green; font-size: 24px;">Home value change: Low</p>'
        st.markdown(hv_rank, unsafe_allow_html=True)
    if pop_change > 0.11:
        pc_rank = '<p style="font-family:sans serif; color:Red; font-size: 24px;">Population change: High</p>'
        st.markdown(pc_rank, unsafe_allow_html=True)
    elif pop_change > 0.05:
        pc_rank = '<p style="font-family:sans serif; color:Black; font-size: 24px;">Population change: Medium</p>'
        st.markdown(pc_rank, unsafe_allow_html=True)
    else:
        pc_rank = '<p style="font-family:sans serif; color:Green; font-size: 24px;">Population change: Low</p>'
        st.markdown(pc_rank, unsafe_allow_html=True)
    if percent_poverty > 0.18:
        pr_rank = '<p style="font-family:sans serif; color:Red; font-size: 24px;">Poverty Rate: High</p>'
        st.markdown(pr_rank, unsafe_allow_html=True)
    elif percent_poverty > 0.12:
        pr_rank = '<p style="font-family:sans serif; color:Black; font-size: 24px;">Poverty Rate: Medium</p>'
        st.markdown(pr_rank, unsafe_allow_html=True)
    else:
        pr_rank = '<p style="font-family:sans serif; color:Green; font-size: 24px;">Poverty Rate: Low</p>'
        st.markdown(pr_rank, unsafe_allow_html=True)
    if pop_per_sq_mile > 5000:
        pd_rank = '<p style="font-family:sans serif; color:Red; font-size: 24px;">Population Density: High</p>'
        st.markdown(pd_rank, unsafe_allow_html=True)
    elif pop_per_sq_mile > 2500:
        pd_rank = '<p style="font-family:sans serif; color:Black; font-size: 24px;">Population Density: Medium</p>'
        st.markdown(pd_rank, unsafe_allow_html=True)
    else:
        pd_rank = '<p style="font-family:sans serif; color:Green; font-size: 24px;">Population Density: Low</p>'
        st.markdown(pd_rank, unsafe_allow_html=True)
  
    
