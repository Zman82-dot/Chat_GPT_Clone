import os
from flask import Flask, render_template, request, jsonify
import openai
openai.api_key ='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'

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

@app.route('/', methods=['GET', 'POST'])
def collect_messages():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        context = [{'role': 'user', 'content': prompt}]
        response = get_completion_from_messages(context)
        return jsonify({'response': response})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
