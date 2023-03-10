# Rio de Janeiro (RJ) Airbnb Project - Property price prediction tool for ordinary people

![Captura de Tela 2022-12-25 às 21 24 12](https://user-images.githubusercontent.com/102926017/209485772-06dedaa9-e9fc-41d3-803c-97ff54bbc8bf.png)

![Captura de Tela 2022-12-25 às 21 19 34](https://user-images.githubusercontent.com/102926017/209485721-83f5b66a-c161-41ef-83eb-89198d6da90a.png)

<img src="https://user-images.githubusercontent.com/102926017/209567585-02ce6623-6d12-4b45-b419-c49b0b425e85.png" width="870px"/>

## Objective

Build a price prediction model that allows a person who owns a property to know how much they should charge per day for renting their property.

Or even, for those who want to rent someone else's property, it helps them to know if the price of that property is attractive (below average for properties with the same characteristics) or not.

## Important information about the datasets

They are from Kaggle website: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

- The datasets contain prices of properties and their respective characteristics in each month.
- Prices are in Brazilian currency: real (R$).
- The data are from April 2018 to May 2020, except for the month of June 2018, which has no database.

## Initial Expectations

- I believe seasonality can be an important factor, since months like December are usually very expensive in RJ due to the summer.
- The location of the property should make a big difference in the price, as it can completely change the characteristics of the place (safety, natural beauty, tourist attractions).
- Amenities can have a significant impact, as we have many old buildings and houses in Rio de Janeiro.

## Used technologies:

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/getting_started.html)
* [Scikit-Learn](https://scikit-learn.org/stable/getting_started.html)
* [Seaborn](https://seaborn.pydata.org)
* [Joblib](https://joblib.readthedocs.io/en/latest/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Streamlit](https://docs.streamlit.io/library/get-started)


## Credits

This is an activity from the [Hashtag Programação Course](https://portalhashtag.com/login) inspired by **Allan Bruno's** data science project, which is available here: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb
