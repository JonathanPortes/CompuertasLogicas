import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importar ttk para los estilos
from puertaAND import PuertaAND
from PuertaOR import PuertaOR
from PuertaNOT import PuertaNOT



class AppCompuertasLogicas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Compuertas Lógicas")
        self.geometry("600x400")  # tamaño de la ventana
        self.configure(bg="lightblue")  # color de fondo de la ventana
        self.crear_widgets()

    def crear_widgets(self):
        self.tipo_compuerta_var = tk.StringVar()
        self.num_entradas_var = tk.IntVar()
        self.entradas_var = []

        etiqueta_compuerta = tk.Label(self, text="Seleccionar Tipo de Compuerta:", bg="lightblue", font=("Arial", 12, "bold"))
        etiqueta_compuerta.pack(pady=10)

        # Creamos el menú desplegable
        opciones_compuerta = ["AND", "OR", "NOT"]
        self.tipo_compuerta_var.set("AND")
        menu_compuerta = tk.OptionMenu(self, self.tipo_compuerta_var, *opciones_compuerta, command=self.actualizar_entradas)
        menu_compuerta.config(bg="lightgrey", fg="black", font=("Arial", 10))  # color del menú desplegable
        menu_compuerta.pack()

        etiqueta_num_entradas = tk.Label(self, text="Número de Entradas:", bg="lightblue", font=("Arial", 12, "bold"))
        etiqueta_num_entradas.pack(pady=10)
        self.entrada_num_entradas = tk.Entry(self, textvariable=self.num_entradas_var, font=("Arial", 10))
        self.entrada_num_entradas.pack()

        self.marco_entradas = tk.Frame(self, bg="lightblue")
        self.marco_entradas.pack(pady=10)

        for i in range(4):
            entrada_var = tk.IntVar()
            etiqueta_entrada = tk.Label(self.marco_entradas, text=f"Entrada {i+1}:", bg="lightblue", font=("Arial", 10))
            etiqueta_entrada.grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(self.marco_entradas, textvariable=entrada_var, font=("Arial", 10))
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas_var.append(entrada_var)

        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular_salida, bg="green", fg="white", font=("Arial", 12, "bold"))
        boton_calcular.pack(pady=20)

    def actualizar_entradas(self, *args):
        tipo_compuerta = self.tipo_compuerta_var.get()
        if tipo_compuerta == "NOT":
            self.num_entradas_var.set(1)
            self.entrada_num_entradas.configure(state="disabled")
        else:
            self.entrada_num_entradas.configure(state="normal")

    def calcular_salida(self):
        tipo_compuerta = self.tipo_compuerta_var.get()
        num_entradas = self.num_entradas_var.get()
        entradas = [entrada_var.get() for entrada_var in self.entradas_var[:num_entradas]]

        if tipo_compuerta == "AND":
            compuerta = PuertaAND(entradas)
        elif tipo_compuerta == "OR":
            compuerta = PuertaOR(entradas)
        elif tipo_compuerta == "NOT":
            if num_entradas != 1:
                messagebox.showerror("Error", "La compuerta NOT requiere exactamente 1 entrada")
                return
            compuerta = PuertaNOT(entradas)
        else:
            messagebox.showerror("Error", "Tipo de compuerta no válido")
            return

        # cuadro de diálogo
        self.style = ttk.Style()  # Usar ttk.Style en lugar de tk.ttk.Style
        self.style.configure('My.TFrame', background='#f0d09d', foreground='#82C8BD')
        self.style.map('My.TFrame', background=[('active', '#f0d09d')])

        salida = compuerta.calcular_salida()
        messagebox.showinfo("Salida", f"La salida es: {salida}")

def main():
    app = AppCompuertasLogicas()
    app.mainloop()

if __name__ == "__main__":
    main()
