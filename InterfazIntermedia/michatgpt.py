import sys
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QTextBrowser

# Indica el API KEY
openai.api_key = "sk-yqj8VavOD2ZRet0HlbB4T3BlbkFJaxXKS8Ns2ssasdasdasdasda"

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Chat con GPT-3")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.chat_display = QTextBrowser(self)
        layout.addWidget(self.chat_display)

        self.user_input = QTextEdit(self)
        layout.addWidget(self.user_input)

        self.send_button = QPushButton("Enviar", self)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Salir", self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

        self.central_widget.setLayout(layout)

    def send_message(self):
        user_input_text = self.user_input.toPlainText()
        if user_input_text.strip() == "":
            return

        # Generar una respuesta utilizando el modelo de OpenAI
        completion = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_input_text, 
            max_tokens=1024, 
            n=1, 
            stop=None, 
            temperature=0.7
        )

        respuesta = completion.choices[0].text
        self.chat_display.append(f"Usuario: {user_input_text}")
        self.chat_display.append(f"Respuesta: {respuesta}\n")

        self.user_input.clear()
        self.user_input.setFocus()

def main():
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
