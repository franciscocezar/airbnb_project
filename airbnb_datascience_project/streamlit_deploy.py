import pandas as pd
import streamlit as st
import joblib


x_numerics = {'latitude': 0, 'longitude': 0, 'accommodates': 0,
              'bathrooms': 0, 'bedrooms': 0, 'beds': 0,
              'extra_people': 0, 'minimum_nights': 0, 'year': 0,
              'month': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_truefalse = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {
    'property_type': ['Apartment', 'Bed and breakfast', 'Condominium',
                      'Guest suite', 'Guesthouse', 'Hostel', 'House',
                      'Loft', 'Others', 'Serviced apartment'
                      ],                     
    'room_type': [
        'Entire home/apt', 'Hotel room', 
        'Private room', 'Shared room'
        ],
    'cancellation_policy': [
        'flexible', 'moderate', 'strict', 
        'strict_14_with_grace_period']
}

features = {f'{item}_{value}': 0 for item in x_lists for value in x_lists[item]}

for item in x_numerics:
    if item == 'latitude' or item == 'longitude':
        value = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        value = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        value = st.number_input(f'{item}', step=1, value=0)
    x_numerics[item] = value

for item in x_truefalse:
    value = st.selectbox(f'{item}', ('Sim', 'Não'))
    if value == "Sim":
        x_truefalse[item] = 1
    else:
        x_truefalse[item] = 0

for item in x_lists:
    value = st.selectbox(f'{item}', x_lists[item])
    features[f'{item}_{value}'] = 1

button = st.button('Prever Preço do Imóvel')

if button:
    features.update(x_numerics)
    features.update(x_truefalse)
    values_x = pd.DataFrame(features, index=[0])

    data = pd.read_csv('data.csv')
    columns_df = list(data.columns)[1:-1]
    values_x = values_x[columns_df]
    model = joblib.load('model.joblib')
    price = model.predict(values_x)
    st.write(f'Valor sugerido: R${price[0]}')

