from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Indica el API KEY
openai.api_key = "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"

# Uso de ChatGPT en PYTHON
model_engine = "text-davinci-003"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('user_input', '')

    # Genera una respuesta utilizando el modelo de OpenAI
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    respuesta = completion.choices[0].text

    return jsonify({'respuesta': respuesta})

if __name__ == "__main__":
    app.run(debug=True)
