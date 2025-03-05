import gradio as gr
from textblob import TextBlob

def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text."
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Custom CSS to improve styling
css = """
body {
    background-color: #f0f2f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
#title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.5rem;
    color: #333;
}
#description {
    font-size: 1.2rem;
    text-align: center;
    margin-bottom: 2rem;
    color: #555;
}
.gr-button {
    background-color: #4CAF50 !important;
    color: white !important;
    border: none !important;
    font-weight: bold;
}
.gr-textbox {
    border: 2px solid #ddd !important;
    border-radius: 5px !important;
}
"""

# Build a more attractive UI with Gradio Blocks
with gr.Blocks(css=css) as demo:
    gr.Markdown("<div id='title'>Sentiment Analysis API</div>")
    gr.Markdown("<div id='description'>Enter a sentence, and the model will predict if it's <b>Positive</b>, <b>Negative</b>, or <b>Neutral</b>.</div>")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(lines=5, placeholder="Type your sentence here...", label="Input Text")
            analyze_btn = gr.Button("Analyze Sentiment")
        with gr.Column():
            output = gr.Textbox(label="Sentiment")
    
    analyze_btn.click(fn=analyze_sentiment, inputs=text_input, outputs=output)

if __name__ == "__main__":
    demo.launch()
