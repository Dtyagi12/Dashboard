import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

vehicle=pd.read_csv("vehicle_list.csv")
al = pd.read_csv("AL.csv")
tata = pd.read_csv("Tata.csv")

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title("WELCOME TO HIPER AUTOMOTIVE")
with col2:
    st.image('hiper.jfif', width=150)

col1,col2,col3 = st.columns([0.3,0.4,0.3])
with col1:
    manu = st.selectbox('Manufacturer',vehicle.Manufacturer.unique())
with col2:
    model = st.selectbox('Model',vehicle.Model.unique())
with col3:
    vn = st.selectbox('Select to View Dashboards',['Fuel Injector','Common Rail','Metering Unit','Water Fuel Seperator','Protect Filter','Fuel Tank'])

if manu == 'AL':
     st.image("bg_AL.png")
     st.image("Component Layout.png")
     st.write('## DASHBOARD REQUESTED')
     if vn == 'Fuel Injector':
         fig = px.scatter(al, x=al['master_row_id'], y=al['error_iq'], color=al['master_row_id'])
         st.plotly_chart(fig)
         st.image('Injector.png', width=150, caption='Injector')
         col1, col2 = st.columns([0.25, 0.25])
         with col1:
             al_avg1 = np.mean(al['error_iq'])
             val = float('{:.2f}'.format(al_avg1))
             col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
         with col2:
             col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')

     elif vn == 'Common Rail':
         fig = px.scatter(al, x=al['master_row_id'], y=al['error_rp'], color=al['master_row_id'])
         st.plotly_chart(fig)
         st.image('Common Rail.png')
         col1, col2 = st.columns([0.25, 0.25])
         with col1:
             al_avg1 = np.mean(al['error_iq'])
             val = float('{:.2f}'.format(al_avg1))
             col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
         with col2:
             col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')

     elif vn == 'Metering Unit':
        fig = px.scatter(al, x=al['master_row_id'], y=al['error_mu'], color=al['master_row_id'])
        st.plotly_chart(fig)
        st.image('Metering Unit.png')
        col1, col2 = st.columns([0.25, 0.25])
        with col1:
            al_avg1 = np.mean(al['error_iq'])
            val = float('{:.2f}'.format(al_avg1))
            col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
        with col2:
            col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')
     elif vn == 'Water Fuel Seperator':
         st.subheader('No data given for this Subsytem hence just displaying the Image')

         st.image('Water Fuel Seperator.png', use_column_width='auto', caption='Water Fuel Seperator')
     elif vn == 'Protect Filter':
         st.subheader('No data given for this Subsytem hence just displaying the Image')
         st.image('Fuel Filter.png', use_column_width='auto', caption='Protect Filter')
     elif vn == 'Fuel Tank':
         st.subheader('No data given for this Subsytem hence just displaying the Image')
         st.image('Fuel Tank.png', use_column_width='auto', caption='Fuel tank')

if manu == 'TATA':
     st.image("bg_TATA.png")
     st.image("Component Layout.png")
     st.write('## DASHBOARD REQUESTED')
     if vn == 'Fuel Injector':
         fig = px.scatter(tata, x=tata['master_row_id'], y=tata['error_iq'], color=tata['master_row_id'])
         st.plotly_chart(fig)
         st.image('Injector.png', width=150, caption='Injector')
         col1, col2 = st.columns([0.25, 0.25])
         with col1:
             al_avg1 = np.mean(tata['error_iq'])
             val = float('{:.2f}'.format(al_avg1))
             col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
         with col2:
             col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')

     elif vn == 'Common Rail':
        fig = px.scatter(tata, x=tata['master_row_id'], y=tata['error_rp'], color=tata['master_row_id'])
        st.plotly_chart(fig)
        st.image('Common Rail.png')
        col1, col2 = st.columns([0.25, 0.25])
        with col1:
            al_avg1 = np.mean(tata['error_iq'])
            val = float('{:.2f}'.format(al_avg1))
            col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
        with col2:
            col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')

     elif vn == 'Metering Unit':
        fig = px.scatter(tata, x=tata['master_row_id'], y=tata['error_mu'], color=tata['master_row_id'])
        st.plotly_chart(fig)
        st.image('Metering Unit.png')
        col1, col2 = st.columns([0.25, 0.25])
        with col1:
            al_avg1 = np.mean(tata['error_iq'])
            val = float('{:.2f}'.format(al_avg1))
            col1.metric(label='Error Percentage', value=str(val) + '%', delta='-100%')
        with col2:
            col2.metric(label='Efficiency', value=str(100 - val) + '%', delta='100%')
     elif vn == 'Water Fuel Seperator':
        st.subheader('No data given for this Subsytem hence just displaying the Image')

        st.image('Water Fuel Seperator.png', use_column_width='auto', caption='Water Fuel Seperator')
     elif vn == 'Protect Filter':
        st.subheader('No data given for this Subsytem hence just displaying the Image')
        st.image('Fuel Filter.png', use_column_width='auto', caption='Protect Filter')
     elif vn == 'Fuel Tank':
        st.subheader('No data given for this Subsytem hence just displaying the Image')
        st.image('Fuel Tank.png', use_column_width='auto', caption='Fuel tank')


