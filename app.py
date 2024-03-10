import streamlit as st
import torch
from transformers import T5Tokenizer

# Load the tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base")

# Function to summarize text
def summarize_text(text, model):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    summary_ids = model.generate(
        inputs['input_ids'],
        max_length=150,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
        no_repeat_ngram_size=2
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def load_model(model_path):
    model = NewsSummaryModel()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def main():
    st.title("Text Summarization App")

    # Load the model
    model_path = "trained_model (1).pth"  # Update with your model path
    model = load_model(model_path)

    # Input text area
    input_text = st.text_area("Enter the text to be summarized", "")

    if st.button("Generate Summary"):
        if input_text:
            summary = summarize_text(input_text, model)
            st.subheader("Generated Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
