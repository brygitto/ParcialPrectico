import tkinter as tk
from tkinter import scrolledtext
import openai

# Indica el API KEY
openai.api_key = "sk-yqj8VavOD2ZRet0HlbB4T3BlbkFJaxXKS8Ns2ssasdasdasdasda"

# Función para generar una respuesta
def generar_respuesta():
    # Obtiene el texto ingresado por el usuario desde la entrada de texto
    usuario_input = entrada_usuario.get("1.0", "end-1c")
    
    # Genera una respuesta utilizando el modelo de OpenAI
    completion = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=usuario_input, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.7
    )
    
    # Obtiene la respuesta generada por el modelo y la muestra en la ventana
    respuesta = completion.choices[0].text
    chat_display.config(state="normal")
    chat_display.insert("end", f"Usuario: {usuario_input}\n")
    chat_display.insert("end", f"Respuesta: {respuesta}\n\n")
    chat_display.config(state="disabled")
    
    # Limpia la entrada de texto del usuario
    entrada_usuario.delete("1.0", "end")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Chat con GPT-3")

# Caja de texto para la conversación
chat_display = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state="disabled")
chat_display.pack(expand=True, fill="both")

# Entrada de texto para el usuario
entrada_usuario = tk.Text(ventana, height=4)
entrada_usuario.pack(expand=True, fill="both")

# Botón para enviar la pregunta
boton_enviar = tk.Button(ventana, text="Enviar", command=generar_respuesta)
boton_enviar.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
