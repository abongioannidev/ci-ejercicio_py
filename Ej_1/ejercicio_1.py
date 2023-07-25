from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio 1
Alumno: Nombre, Apellido
Division: Div J

'''


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=0, column=0, pady=10, padx=10)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, column=0, pady=10, padx=10)

        self.lista_nombres = ["Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Pedro",
                              "Sofía", "Miguel", "Valentina",
                              "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina",
                              "Jorge", "Camila", "Ricardo", "Isabella",
                              "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela",
                              "Gustavo", "Carolina", "Emilio", "Antonella",
                              "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina",
                              "Raul", "Rocio", "Javier", "Marina",
                              "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena",
                              "Oscar", "Pilar", "Hugo", "Juana", "Guillermo", "Natalia", "Francisco", "Constanza", "Hector",
                              "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
                              "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia",
                              "Camilo", "Teresa", "Samuel", "Rosa",
                              "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano",
                              "Silvia", "Nicolas", "Alicia",
                              "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo",
                              "Beatriz", "Elias", "Rita",
                              "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes",
                              "Gerardo", "Manuela", "Feliciano", "Marta"]
        self.lista_edades = [25, 33, 20, 29, 16, 40, 22, 28, 35, 18,
                             26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
                             29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
                             19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
                             35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
                             31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
                             29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
                             32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
                             31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
                             25, 29, 16, 38, 40, 18, 27, 30, 32, 24]

        self.lista_generos = [
            "Masculino", "Femenino", "Masculino", "Femenino", "Otro",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
        ]
        # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.lista_tipo_entrada = [
            "General", "Campo delantero", "Platea", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Campo delantero", "Platea", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
        ]

        # Lista de medio de pago (Credito, Debito, Efectivo)
        self.lista_medio_pago = [
            "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito"
        ]

        # Lista de precios correspondientes a cada tipo de entrada
        self.lista_precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000
                              ]

    def btn_agregar_on_click(self):
        print("hice click en agregar")

    def btn_mostrar_on_click(self):
        print("hice click en mostar")


print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
