import ttkbootstrap as tb
import customtkinter
from tkinter import *
from ttkbootstrap.constants import *

root = tb.Window(themename="cyborg")


class PricePredictor:

    def __init__(self):
        self.root = root
        self.root.title("")
        self.center()
        self.frames()
        self.widgets()
        self.root.mainloop()

    def center(self):
        APP_WIDTH = 850
        APP_HEIGHT = 600

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
        # Customtkinter
        self.latitude_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                     placeholder_text="Latitude", border_width=1)
        self.latitude_entry.place(relx=0.03, rely=0.31, relwidth=0.25)

        self.longetude_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                      placeholder_text="Longetude", border_width=1)
        self.longetude_entry.place(relx=0.3, rely=0.31, relwidth=0.25)

        self.extra_people_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                         placeholder_text="Extra Pessoas", border_width=1)
        self.extra_people_entry.place(relx=0.578, rely=0.31, relwidth=0.17)

        self.month_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                  placeholder_text="Mês", border_width=1)
        self.month_entry.place(relx=0.77, rely=0.31, relwidth=0.07)

        self.year_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                 placeholder_text="Ano", border_width=1)
        self.year_entry.place(relx=0.86, rely=0.31, relwidth=0.1)



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
        self.host_is_superhos_label.place(relx=0.23, rely=0.424, relwidth=0.18, relheight=0.11)
        tb.Radiobutton(text='Sim', variable=self.host_is_superhost,
                       value=1, command=lambda: print(self.host_is_superhost.get()),
                       bootstyle="light-outline-toolbutton").place(relx=0.25, rely=0.46)
        tb.Radiobutton(text='Não', variable=self.host_is_superhost,
                       value=0, command=lambda: print(self.host_is_superhost.get()),
                       bootstyle="light-outline-toolbutton").place(relx=0.33, rely=0.46)


        self.instant_bookable = tb.IntVar()
        self.instant_bookable.set(9)
        self.instant_bookable_label = tb.Labelframe(text='Reserva Imediata')
        self.instant_bookable_label.place(relx=0.56, rely=0.424, relwidth=0.18, relheight=0.11)
        tb.Radiobutton(text='Sim', variable=self.instant_bookable,
                       value=1, command=lambda: print(self.instant_bookable.get()),
                       bootstyle="light-outline-toolbutton").place(relx=0.58, rely=0.46)
        tb.Radiobutton(text='Não', variable=self.instant_bookable,
                       value=0, command=lambda: print(self.instant_bookable.get()),
                       bootstyle="light-outline-toolbutton").place(relx=0.66, rely=0.46)


        # TB - OPTIONS
        property_type = ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel',
                              'House', 'Loft', 'Others', 'Serviced apartment']
        self.property_type = tb.Combobox(values=property_type)
        self.property_type.set("Tipo de Imóvel")
        self.property_type.place(relx=0.07, rely=0.6, relwidth=0.25)



        room_type = ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']
        self.room_type = tb.Combobox(values=room_type)
        self.room_type.set("Tipo de Quarto")
        self.room_type.place(relx=0.357, rely=0.6, relwidth=0.25)

        cancellation_policy = ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
        self.cancellation_policy = tb.Combobox(values=cancellation_policy)
        self.cancellation_policy.set("Política de Cancelamento")
        self.cancellation_policy.place(relx=0.65, rely=0.6, relwidth=0.25)


        # TB - BUTTON
        self.save_button = tb.Button(text="Prever Preço", bootstyle=LIGHT)
        self.save_button.place(relx=0.357, rely=0.71, relwidth=0.25)

        # self.label_mode = tb.Label(master=self.frame_1, text="Preço")
        # self.label_mode.place(relx=0.05, rely=0.75, relwidth=0.9)


if __name__ == "__main__":
    app = PricePredictor()
