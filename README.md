# BlogMaker: Your AI Writing Companion 🤖🎨

## Overview

BlogMaker is a Streamlit application that helps you generate blog posts with the assistance of AI.  It combines the power of large language models (LLMs) for text generation with image generation models to create both the written content and accompanying visuals for your blog.

## Features

* **Blog Post Generation:** You provide a blog title, keywords, and desired word count, and the app uses the Gemini AI model to generate a full blog post.
* **Image Generation:** The app can generate images to accompany your blog post using the Stability AI API.  You specify the number of images you want, and the app generates them based on your blog title.
* **Customizable Output:** You can control the length of the blog post and the number of images generated.
* **Streamlit Interface:** The app provides a user-friendly interface with a sidebar for inputting blog details and a main area for displaying the generated blog post and images.

## How It Works

The app follows these steps:

1.  **User Input:**
    * The Streamlit app displays a sidebar where you can enter the following information:
        * Blog Title
        * Keywords (to guide the content generation)
        * Number of words for the blog post
        * Number of images to generate
2.  **Blog Post Generation (Gemini):**
    * When you click the "Generate Blog" button, the app uses the Gemini AI model to create the blog post.
    * The app sends a prompt to Gemini, including the blog title, keywords, and desired word count.
    * Gemini generates the blog post text, which is then displayed in the main area of the app.
3.  **Image Generation (Stability AI):**
    * If you specified a number of images to generate, the app uses the Stability AI API to create images.
    * For each image, the app sends a text prompt to the Stability API, using the blog title and an image number.
    * The Stability API generates an image, which is then displayed below the blog post text.
4.  **Output:**
    * The generated blog post is displayed in the main area of the Streamlit app.
    * The generated images (if any) are displayed below the blog post, with captions.

## Setup

### Prerequisites

* Python 3.6+
* Streamlit
* Required Python packages (see `requirements.txt`)
* API Keys:
    * Google Gemini API Key
    * Stability AI API Key

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your_repo_url>
    cd <your_repo_directory>
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate   # On Windows
    ```
3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up API Keys:**
    * Obtain API keys from Google (for Gemini) and Stability AI.
    * Create a file named `api_keys.py` in the same directory as the main script.
    * Add your API keys to `api_keys.py`:
        ```python
        gemini_api_key = "YOUR_GEMINI_API_KEY"
        dream_api_key = "YOUR_STABILITY_AI_API_KEY"
        ```
        Replace `"YOUR_GEMINI_API_KEY"` and `"YOUR_STABILITY_AI_API_KEY"` with your actual API keys.
5.  **Run the Streamlit app:**
    ```bash
    streamlit run your_app_name.py # Replace your_app_name.py
    ```

## Usage

1.  Open the Streamlit app in your web browser.
2.  In the sidebar, enter the following details:
    * Blog Title
    * Keywords
    * Number of words for the blog post
    * Number of images to generate
3.  Click the "Generate Blog" button.
4.  The app will generate the blog post and display it in the main area.
5.  If you specified images, the app will generate them and display them below the blog post.

## Code Structure

* `app.py`: The main Streamlit application script.
* `api_keys.py`:  (You need to create this)  A file to store your API keys (not included in the main script for security reasons).
* `requirements.txt`:  A file listing the Python packages required to run the app.

## Dependencies

The app uses the following Python packages:

* Streamlit:  For creating the user interface.
* google-generativeai:  For interacting with the Gemini AI model.
* requests: For making requests to the Stability AI API.

And the important packages from your canvas:

absl-py==2.1.0
aiohttp==3.11.18
altair==5.5.0
fastapi==0.115.9
h5py==3.13.0
jax==0.5.3
langchain==0.3.24
llama-index==0.12.33
matplotlib==3.10.1
numpy==1.26.4
opencv-python==4.11.0.86
pandas==2.2.3
torch==2.7.0
scikit-learn==1.6.1
scipy==1.15.2
streamlit==1.44.1
tensorflow==2.19.0
transformers==4.51.3
uvicorn==0.34.0


## API Keys

**Important:** You need to obtain API keys from Google (Gemini) and Stability AI and store them in a file named `api_keys.py`.  This file is not included in the main script to protect your keys.

## Troubleshooting

* **API Key Errors:** If you get errors related to API keys, double-check that you have correctly entered your keys in the `api_keys.py` file.
* **Installation Errors:** If you have trouble installing the required packages, make sure you are using a virtual environment and that you have a compatible version of Python.
* **Image Generation Errors:** If image generation fails, check your Stability AI API key and ensure that the API is working correctly.  The error messages in the Streamlit app should provide more details.
* **Timeout Errors:** If the app hangs, especially during image generation, try increasing the `timeout` value in the `generate_image` function.

## Disclaimer

This app uses AI models to generate content, and the output may not always be perfect.  It's essential to review and edit the generated content as needed.
