import pandas as pd
import streamlit as st
import joblib


x_numerics = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0,
              'extra_people': 0,
              'minimum_nights': 0, 'year': 0, 'month': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_truefalse = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {
    'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House',
                      'Loft', 'Others', 'Serviced apartment'],
    'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
    'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
    }

dicionario = {}
for item in x_lists:
    for valor in x_lists[item]:
        dicionario[f'{item}_{valor}'] = 0

for item in x_numerics:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numerics[item] = valor

for item in x_truefalse:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == "Sim":
        x_truefalse[item] = 1
    else:
        x_truefalse[item] = 0

for item in x_lists:
    valor = st.selectbox(f'{item}', x_lists[item])
    dicionario[f'{item}_{valor}'] = 1

botao = st.button('Prever Valor do Imóvel')

if botao:
    dicionario.update(x_numerics)
    dicionario.update(x_truefalse)
    valores_x = pd.DataFrame(dicionario, index=[0])

    data = pd.read_csv('data.csv')
    columns_df = list(data.columns)[1:-1]
    valores_x = valores_x[columns_df]
    modelo = joblib.load('model.joblib')
    preco = modelo.predict(valores_x)
    st.write(f'Valor sugerido: R${preco[0]}')
