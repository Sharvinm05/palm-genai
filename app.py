from flask import Flask, render_template, request
import google.generativeai as palm
app = Flask(__name__)

API_KEY = "your-api-key"
palm.configure(api_key=API_KEY)

model_id = 'models/text-bison-001'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    product_name = request.form['product']
    
    prompt = f'''
    Write a marketing proposal to sell {product_name} hair product. Limit the proposal to 100 words.
    '''
    
    completion = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
        candidate_count=1
    )
    
    generated_text = completion.candidates[0]['output']
    print(generated_text)
    
    return render_template('index.html', generated_text=generated_text, product_name=product_name)

if __name__ == '__main__':
    app.run(debug=True)