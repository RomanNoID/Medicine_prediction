import streamlit as st
import joblib
import pandas as pd


st.header('Вероятность сердечно-сосудистых заболеваний')

st.write('Укажите ваш пол')
#gender = st.selectbox('Пол', ['Мужской', 'Женский'], key='gender')
gender = st.selectbox('Пол', [1, 2], key='gender')

st.write('Укажите ваш возраст')
age = st.number_input('Возраст', key=int(), value=int())

st.write('Укажите ваш рост')
height = st.slider('Рост', 80, 250, key='height')

st.write('Укажите Ваш вес')
weight = int(st.number_input('Вес'))

st.write('Укажите верхнее значение артериального давления')
ap_hi = st.slider('Артериальное давление', 80, 200)

st.write('Укажите нижнее значение артериального давления')
ap_lo = st.slider('Артериальное давление', 40, 160)

st.write('Укажите уровень холестирина в крови')

cholesterol = st.selectbox('Категория', [1, 2, 3], key='cholesterol')

st.write('Укажите уровень глюкозы в крови')
gluc = st.selectbox('Категория', [1, 2, 3], key='gluc')

#st.write('Курение')
#smoke = st.radio('Вы курите?', options=('Да', 'Нет'), key='smoking') 
smoke = st.radio('Вы курите?', options=(1, 0), key='smoking') 

#st.write('Алкоголь')
#alco = st.radio('Вы употребляете алкоголь?', options=('Да', 'Нет'), key='alco')
alco = st.radio('Вы употребляете алкоголь?', options=(1, 0), key='alco')

#st.write('Спорт')
#sport = st.radio('Вы занимаетесь спортом?', options=('Да', 'Нет'), key='sport')
active = st.radio('Вы занимаетесь спортом?', options=(1, 0), key='sport')



#if gender == 'Мужской':
#    gender=1
#elif gender == 'Женский':
#    gender=2

age = (age * 365)
#if smoke == 'Да':
#    smoke=1
#elif smoke == 'Нет':
 #   smoke=0
#if alco == 'Да':
 #   smoke=1
#elif alco == 'Нет':
 #   smoke=0
#if sport == 'Да':
 #   active=1
#elif sport == 'Нет':
 #   active=0


user_data = pd.DataFrame(data=[[age, gender, height, weight, ap_hi, ap_lo,
                               cholesterol, gluc, smoke, alco, active]],
                         columns=('age', 'gender', 'height', 'weight', 'ap_hi',
                                  'ap_lo','cholesterol', 'gluc', 'smoke',
                                  'alco', 'active'))

model = joblib.load('/Users/roman/Desktop/Яндекс Практикум/Medicine/model.pkl')

#prediction = model.predict_proba([age, gender, height, weight, ap_hi,
 #                                 ap_lo, cholesterol, gluc, smoke, alco,
  #                                active])[:, 1]

prediction = model.predict_proba(user_data)[:, 1]

if st.button('Предсказать'):
    st.write('Вeроятность ССЗ составляет:')
    st.write(prediction)
    #st.write(f'{prediction:.3%}')
    #st.dataframe(data=user_data)