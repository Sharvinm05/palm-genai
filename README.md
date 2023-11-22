# GPT-3 Business Proposal Generator

## Overview

This Flask web application utilizes the OpenAI GPT-3 model through the GenerativeAI Palm API to generate business proposals for a given product. Users can input the product name, and the application generates a marketing proposal in response.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following:

- Python installed on your machine
- Flask framework (`pip install Flask`)
- A valid API key for the GenerativeAI Palm API

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sharvinm05/palm-genai.git
    cd palm-genai
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set your GenerativeAI Palm API key:**

    Replace `"your-api-key"` in `app.py` with your actual API key.

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).**

3. **Enter a product name in the input box and click the "Generate Proposal" button.**

4. **View the generated business proposal on the web page.**

## Customization

- **Model Configuration:**
  You can customize the GPT-3 model by modifying the `model_id` variable in the `app.py` file.

- **Styling:**
  Adjust the HTML and CSS files in the `templates` folder to change the look and feel of the web interface.
