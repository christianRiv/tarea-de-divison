from tkinter import ttk
from tkinter import *
class CHRISTIAN:
    def __init__(self, window):
        # Inicio

        #ancho y alto de la ventana
        ancho = 800
        alto = 600

        #Colocamos a la ventana una variable de la clase llamada "wind"
        self.wind = window

        #Colocamos el ancho y el alto a la ventana 
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centrar el contenido 
        self.wind.columnconfigure(0, weight=1)

        #Asignamos un titulo a la ventana
        self.wind.title('PROGRAMA DE CHRISTIAN')

        #Creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Dividicón de 2 valores',background ="blue")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Creamos un etiqueta
        Label(frame, text = 'Escriba su Primer Número: ',background ="red").grid(row = 1, column = 0)

        #Creamos t donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        # colocamos una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Escriba su Segundo Número: ',background = "red").grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #Creamos un boton para ejecutar la Division
        Button(frame, text = 'Presione Para Dividir', background ="blue", command = self.dividir).grid(row = 3, columnspan = 2, sticky = W + E)
      
        #Establecemos un mensaje
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    #Creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0

    #función que ejecuta la división
    def dividir(self):
        if self.validation():
            resultado = int( self.var1.get() ) / int( self.var2.get() )
            resultado2 = int( self.var1.get() ) % int( self.var2.get())
            if(resultado2 == 0):
                self.message['text'] = 'La división realizada es exacta y su cociente es: {}'.format(resultado)
            else:
                self.message['text'] = 'La división realizada es inexacta y su cociente es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son necesarios.'                        

if __name__ == '__main__':

    window = Tk()

    app = CHRISTIAN(window)
   
    window.mainloop()