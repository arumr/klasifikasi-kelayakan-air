import pickle
import streamlit as st

model = pickle.load(open('kualitas_air.sav','rb'))

st.title('KLASIFIKASI KELAYAKAN AIR MINUM')

col1, col2, col3 = st.columns(3)

with col1:
    aluminium = st.number_input('Kadar Aluminium(mg/l)')
    barium = st.number_input('Kadar Barium(mg/l)')
    chromium = st.number_input('Kadar Chromium(mg/l)')
    bacteria = st.number_input('Kadar Bakteri(mg/l)')
    nitrates = st.number_input('Kadar Nitrates(mg/l)')
    perchlorate = st.number_input('Kadar Perchlorate(mg/l)')
    silver = st.number_input('Kadar Silver(mg/l)')
with col2:
    ammonia = st.number_input('Kadar Ammonia(mg/l)')
    cadmium = st.number_input('Kadar Cadmium(mg/l)')
    copper = st.number_input('Kadar Copper(mg/l)')
    viruses = st.number_input('Kadar Virus(mg/l)')
    nitrites = st.number_input('Kadar Nitrites(mg/l)')
    radium = st.number_input('Kadar Radium(mg/l)')
    uranium = st.number_input('Kadar Uranium(mg/l)')
with col3:
    arsenic = st.number_input('Kadar arsenic(mg/l)')
    chloramine = st.number_input('Kadar Chloramine(mg/l)')
    flouride = st.number_input('Kadar Flouride(mg/l)')
    lead = st.number_input('Kadar Lead(mg/l)')
    mercury = st.number_input('Kadar Mercury(mg/l)')
    selenium = st.number_input('Kadar Selenium(mg/l)')

result = ''

if st.button('Prediksi kualitas air'):
    predict = model.predict([[aluminium,ammonia,arsenic,
                              barium,cadmium,chloramine,
                              chromium,copper,flouride,
                              bacteria,viruses,lead,
                              nitrates,nitrites,mercury,
                              perchlorate,radium,selenium,
                              silver,uranium]]) 
    if predict == 2 :
        result = 'Air layak dan aman diminum'
    else:
        result = 'Air tidak layak dan tidak aman diminum'
    st.success(result)
