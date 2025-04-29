import streamlit as st
import base64
import os
import requests
from google import genai
from google.genai import types
from api_keys import gemini_api_key, stability_api_key
import io


# Stability AI API Configuration (Replace with your actual API key)
API_HOST = "https://api.stability.ai"
# Or another suitable engine
ENGINE_ID = "stable-diffusion-xl-1024-v1-0"
OUTPUT_DIR = "output_images"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


# page layout
st.set_page_config(layout="wide")

# title of our app
st.title("BlogMaker: Your AI Writing Companion 🤖🎨")

# create subheader
st.subheader("Now you can craft perfect blog with the help of AI")

blog = ""
# sidebar for user input
with st.sidebar:
    st.image("whitelogo.png",width=128)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.title("Input Your Blog Details")
    st.subheader("Enter your blog details")

    # blog title
    blog_title = st.text_input("Blog Title")

    # keywords input
    keywords = st.text_input("Explain your idea")

    # number of words
    num_words = st.slider(
        "Number of words:", min_value=250, max_value=1000, step=250
    )

    # number of images -  using NumberInput instead of Slider to align with your requirement
    num_images = st.number_input(
        "Number of images:", min_value=0, max_value=10, step=1
    )

    # submit
    submit_button = st.button("Generate Blog")

    def generate_blog(blog_title, keywords, num_words):
        client = genai.Client(
            api_key=gemini_api_key,
        )

        model = "gemini-1.5-flash"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=f"""generate a comprehensive, engaging blog post to the given title {blog_title} and keywords{keywords}. the blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""
                    ),
                ],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0,),
            response_mime_type="text/plain",
        )

        full_blog = ""
        try:
            for chunk in client.models.generate_content_stream(
                model=model, contents=contents, config=generate_content_config,
            ):
                if chunk.text:
                    full_blog += chunk.text
            return full_blog
        except Exception as e:
            return f"❌ API Error: {e}"

def generate_image(prompt):
    # Make sure API_KEY is defined and accessible here (it's outside the function scope in your example)
    if not dream_API_KEY: 
        st.error(
            "API key not found.  Please ensure you've configured your API key correctly."
        )
        return None

    try:
        response = requests.post(
            f"{API_HOST}/v1/generation/{ENGINE_ID}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "image/png",  # Request a PNG image directly
                "Authorization": f"Bearer {API_KEY}",
            },
            json={
                "text_prompts": [{"text": prompt, "weight": 1}],
                "cfg_scale": 7,
                # --- CHANGE THESE LINES ---
                "height": 1024,  # Use an allowed dimension
                "width": 1024,   # Use an allowed dimension
                # --------------------------
                "samples": 1,
                "steps": 30, 
                # Optional: You might want to add a style preset for SDXL
                # "style_preset": "photorealistic", # e.g., cinematic, fantasy-art, etc.
            },
            timeout=30 # Add a timeout to prevent hanging indefinitely
        )

        response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)

        return response.content # Return the raw image bytes

    except requests.exceptions.RequestException as e:
        # More specific error reporting
        error_message = f"Error during image generation request: {e}"
        if e.response is not None:
            try:
                # Attempt to parse the error response from the API
                error_details = e.response.json()
                error_message += f"\nAPI Response: {error_details}"
            except ValueError: # If the response is not JSON
                error_message += f"\nAPI Response Text: {e.response.text}"
        st.error(error_message)
        return None
    except Exception as e: # Catch any other unexpected errors
        st.error(f"An unexpected error occurred: {e}")
        return None

if submit_button:
        # Generate the blog post
        blog = generate_blog(blog_title, keywords, num_words)
        st.markdown("<h2 style='padding: 10px; border-radius: 10px; outline: 2px solid transparent; outline-offset: 0px; background-image: linear-gradient(to right, #FFD700, #FFA500, #FF4500); background-clip: padding-box;'>Your Blog Post:</h2>", unsafe_allow_html=True)

        st.write(blog)
        st.write(blog)

        # Generate and display images (if requested)
        for i in range(num_images):
            # Added index to the prompt
            image_data = generate_image(f"{blog_title} - image {i+1}")
            if image_data:
                st.image(
                    image_data,
                    caption=f"Generated Image {i+1}",
                    use_container_width=True,
                )
