
import tkinter as tk
root = tk.Tk()
marcas_carros = tk.StringVar()
listbox = tk.Listbox(root)
label = tk.Label(text="Marcas de carro:")
label.pack()
for item in ["BMW ", "Mercedes-Benz", "Audi", "Volvo ", "Land Rover", "Porsche", "Lexus", "Jaguar","Maserati"]:
 listbox.insert(tk.END, item)
listbox.pack()


root.mainloop()