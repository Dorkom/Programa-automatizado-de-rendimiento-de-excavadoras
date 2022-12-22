from tkinter import *
from tkinter import ttk

print('excavadora1')
# selwin.withdraw()

def calcular_rend():
    # if tiempo1_text.get() != '' or tiempo2_text.get() != '' or tiempo3_text.get() != '':
    #     calt = float(tiempo1_text.get()) + float(tiempo2_text.get()) + float(tiempo3_text.get())
    #     prod = float(calt)*float(volumen_text.get())
    #     rend = prod*8.0
    #     productividad_text.set(prod)
    #     rendimiento_text.set(rend)
    # print('productividad')
    print(prod)
    # print('rendimiento')
    print(rend)

# def on_closingapp():
#     selwin.deiconify()
#     app.destroy()

app = Tk()

appframe = Frame(app, width=100, height=100)
appframe.pack(side='top',  fill='both',  padx=10, pady=5,  expand=True)

applabelframe = Frame(appframe, width=10, height=10)
applabelframe.pack(side='left', fill='both', padx=5, pady=5, expand=True)
appentryframe = Frame(appframe, width=10, height=10)
appentryframe.pack(side='right', fill='both', padx=5, pady=5, expand=True)

# Tiempo de ciclo
tiempo1_text = StringVar(app,'','tiempo1')
tiempo1_label = Label(app, text='Tiempo 1', font=('bold',14))
tiempo1_label.pack()
tiempo1_entry = Entry(app, textvariable=tiempo1_text)
tiempo1_entry.pack()

tiempo2_text = StringVar(app,'','tiempo2')
tiempo2_label = Label(app, text='Tiempo 2', font=('bold',14))
tiempo2_label.pack()
tiempo2_entry = Entry(app, textvariable=tiempo2_text)
tiempo2_entry.pack()

tiempo3_text = StringVar(app,'','tiempo3')
tiempo3_label = Label(app, text='Tiempo 3', font=('bold',14))
tiempo3_label.pack()
tiempo3_entry = Entry(app, textvariable=tiempo3_text)
tiempo3_entry.pack()

# Volumen
volumen_text = StringVar(app,'','volumen')
volumen_label = Label(app, text='Volumen', font=('bold',14))
volumen_label.pack()
volumen_entry = Entry(app, textvariable=volumen_text)
volumen_entry.pack()

# Productividad
productividad_text = StringVar(app,'','prod')
productividad_label = Label(app, text='Productividad', font=('bold',14))
productividad_label.pack()
productividad_output = Label(app, textvariable=productividad_text, relief=RAISED, font=('bold',14))
productividad_output.pack()

# Rendimiento
rendimiento_text = StringVar(app,'','rend')
rendimiento_label = Label(app, text='Rendimiento', font=('bold',14))
rendimiento_label.pack()
rendimiento_output = Label(app, textvariable=rendimiento_text, relief=RAISED, font=('bold',14))
rendimiento_output.pack()

# Buttons
calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend)
calcular_btn.pack()

app.title('Rendimiento')
app.maxsize(700, 500)

app.mainloop()