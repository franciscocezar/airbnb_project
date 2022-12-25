import pandas as pd
import joblib
import ttkbootstrap as tb
import customtkinter
from tkinter import *
from ttkbootstrap.constants import *

root = tb.Window(themename="cyborg")


class PricePredictor:

    def __init__(self):
        self.root = root
        self.root.title("Property Price Prediction Tool")
        self.center()
        self.frames()
        self.widgets()
        self.root.mainloop()

    def center(self):
        APP_WIDTH = 850
        APP_HEIGHT = 500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        app_center_coordinate_x = (screen_width / 2) - (APP_WIDTH / 2)
        app_center_coordinate_y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Position App to the Centre of the Screen
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    def frames(self):
        self.frame_1 = tb.Frame()
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets(self):
        title_label = tb.Label(text="Previsão de Preço Airbnb RJ", font=('Helvetica', 28), anchor=CENTER)
        title_label.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.06)

        # Customtkinter
        self.latitude_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                     placeholder_text="Latitude", border_width=0, fg_color='gray10')
        self.latitude_entry.place(relx=0.03, rely=0.33, relwidth=0.25)

        self.longetude_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                      placeholder_text="Longetude", border_width=0, fg_color='gray10')
        self.longetude_entry.place(relx=0.3, rely=0.33, relwidth=0.25)

        self.extra_people_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                         placeholder_text="Pessoa Extra", border_width=0,
                                                         fg_color='gray10')
        self.extra_people_entry.place(relx=0.578, rely=0.33, relwidth=0.17)

        self.month_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                  placeholder_text="Mês", border_width=0, fg_color='gray10')
        self.month_entry.place(relx=0.77, rely=0.33, relwidth=0.07)

        self.year_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                 placeholder_text="Ano", border_width=0,
                                                 fg_color='gray10', border_color=None)
        self.year_entry.place(relx=0.86, rely=0.33, relwidth=0.1)

        # TTKBOOTSTRAP - INT
        self.accom_label = tb.Labelframe(text='Acomodações')
        self.accom_label.place(relx=0.043, rely=0.18, relwidth=0.12, relheight=0.10)
        self.accommodates_entry = tb.Spinbox(from_=0, to=10)
        self.accommodates_entry.place(relx=0.053, rely=0.21, relwidth=0.10)

        self.bedrooms_label = tb.Labelframe(text='Quartos')
        self.bedrooms_label.place(relx=0.173, rely=0.18, relwidth=0.12, relheight=0.10)
        self.bedrooms_entry = tb.Spinbox(from_=0, to=10)
        self.bedrooms_entry.place(relx=0.183, rely=0.21, relwidth=0.10)

        self.beds_label = tb.Labelframe(text='Camas')
        self.beds_label.place(relx=0.303, rely=0.18, relwidth=0.12, relheight=0.10)
        self.beds_entry = tb.Spinbox(from_=0, to=10)
        self.beds_entry.place(relx=0.313, rely=0.21, relwidth=0.10)

        self.bathrooms_label = tb.Labelframe(text='Banheiros')
        self.bathrooms_label.place(relx=0.433, rely=0.18, relwidth=0.12, relheight=0.10)
        self.bathrooms_entry = tb.Spinbox(from_=0, to=10)
        self.bathrooms_entry.place(relx=0.443, rely=0.21, relwidth=0.10)

        self.min_nt_label = tb.Labelframe(text='Noites Mín.')
        self.min_nt_label.place(relx=0.563, rely=0.18, relwidth=0.12, relheight=0.10)
        self.minimum_nights_entry = tb.Spinbox(from_=1, to=10)
        self.minimum_nights_entry.place(relx=0.573, rely=0.21, relwidth=0.10)

        self.ameni_label = tb.Labelframe(text='Comodidades')
        self.ameni_label.place(relx=0.693, rely=0.18, relwidth=0.12, relheight=0.10)
        self.n_amenities_entry = tb.Spinbox(from_=0, to=10)
        self.n_amenities_entry.place(relx=0.703, rely=0.21, relwidth=0.10)

        self.host_list_label = tb.Labelframe(text='Qtd Imóveis')
        self.host_list_label.place(relx=0.823, rely=0.18, relwidth=0.12, relheight=0.10)
        self.host_listings_count_entry = tb.Spinbox(from_=0, to=10)
        self.host_listings_count_entry.place(relx=0.833, rely=0.21, relwidth=0.10)

        # TB - TRUE/FALSE
        self.host_is_superhost = tb.IntVar()
        self.host_is_superhost.set(9)
        self.host_is_superhos_label = tb.Labelframe(text='Super Host')
        self.host_is_superhos_label.place(relx=0.23, rely=0.56, relwidth=0.18, relheight=0.11)
        tb.Radiobutton(text='Sim', variable=self.host_is_superhost,
                       value=1,
                       bootstyle="light-outline-toolbutton").place(relx=0.25, rely=0.6)
        tb.Radiobutton(text='Não', variable=self.host_is_superhost,
                       value=0,
                       bootstyle="light-outline-toolbutton").place(relx=0.33, rely=0.6)

        self.instant_bookable = tb.IntVar()
        self.instant_bookable.set(9)
        self.instant_bookable_label = tb.Labelframe(text='Reserva Imediata')
        self.instant_bookable_label.place(relx=0.56, rely=0.56, relwidth=0.18, relheight=0.11)
        tb.Radiobutton(text='Sim', variable=self.instant_bookable,
                       value=1, bootstyle="light-outline-toolbutton").place(relx=0.58, rely=0.6)
        tb.Radiobutton(text='Não', variable=self.instant_bookable,
                       value=0,
                       bootstyle="light-outline-toolbutton").place(relx=0.66, rely=0.6)

        # TB - OPTIONS
        self.property = ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment']
        self.property_type = tb.Combobox(values=self.property)
        self.property_type.set("Tipo de Imóvel")
        self.property_type.place(relx=0.07, rely=0.45, relwidth=0.25)

        self.room_t = ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']
        self.room_type = tb.Combobox(values=self.room_t)
        self.room_type.set("Tipo de Quarto")
        self.room_type.place(relx=0.357, rely=0.45, relwidth=0.25)

        self.cancellation_pol = ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
        self.cancellation_policy = tb.Combobox(values=self.cancellation_pol)
        self.cancellation_policy.set("Política de Cancelamento")
        self.cancellation_policy.place(relx=0.65, rely=0.45, relwidth=0.25)

        # TB - BUTTON
        self.save_button = tb.Button(text="Prever Preço", bootstyle=LIGHT, command=self.back_end)
        self.save_button.place(relx=0.36, rely=0.74, relwidth=0.25)

        self.label_mode = tb.Label(text="Resultado da Previsão: R$", anchor=CENTER)
        self.label_mode.place(relx=0.03, rely=0.86, relwidth=0.93, relheight=0.06)

    def back_end(self):

        values = {f'cancellation_policy_{self.cancellation_policy.get()}': 1,
                  f'room_type_{self.room_type.get()}': 1,
                  f'property_type_{self.property_type.get()}': 1,
                  'host_is_superhost': self.host_is_superhost.get(),
                  'instant_bookable': self.instant_bookable.get(),
                  'latitude': float(self.latitude_entry.get()), 'longitude': float(self.longetude_entry.get()),
                  'accommodates': int(self.accommodates_entry.get()), 'bathrooms': int(self.bathrooms_entry.get()),
                  'bedrooms': int(self.bedrooms_entry.get()), 'beds': int(self.beds_entry.get()),
                  'extra_people': float(self.extra_people_entry.get()),
                  'minimum_nights': int(self.minimum_nights_entry.get()),
                  'year': int(self.year_entry.get()), 'month': int(self.month_entry.get()),
                  'n_amenities': int(self.n_amenities_entry.get()),
                  'host_listings_count': int(self.host_listings_count_entry.get())}

        x_numerics = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0,
                      'extra_people': 0,
                      'minimum_nights': 0, 'year': 0, 'month': 0, 'n_amenities': 0, 'host_listings_count': 0}

        x_truefalse = {'host_is_superhost': 0, 'instant_bookable': 0}

        x_lists = {'property_type': self.property,
                   'room_type': self.room_t,
                   'cancellation_policy': self.cancellation_pol}
        dictionary = {f'{item}_{valor}': 0 for item in x_lists for valor in x_lists[item]}

        dictionary.update(x_numerics)
        dictionary.update(x_truefalse)
        dictionary.update(values)

        values_x = pd.DataFrame(dictionary, index=[0])

        data = pd.read_csv('data.csv')
        columns_df = list(data.columns)[1:-1]
        values_x = values_x[columns_df]
        model = joblib.load('model.joblib')
        price = model.predict(values_x)
        self.label_mode.config(text=f"Resultado da Previsão: R${price[0]}")


if __name__ == "__main__":
    app = PricePredictor()
