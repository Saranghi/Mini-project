import openai
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.form.get('text')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Generate an image using OpenAI's DALL·E model
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the image
        )
        image_url = response['data'][0]['url']
        
        return jsonify({"image_url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
