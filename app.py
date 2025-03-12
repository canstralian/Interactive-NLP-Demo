import nltk
import pandas as pd
import plotly.express as px
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


class NLPDemo:
    def __init__(self):
        self.available_nlp_tasks = [
            {"name": "tokenization", "description": "Split text into tokens"},
            {"name": "stop_words", "description": "Remove common stop words"},
            {"name": "stemming", "description": "Reduce words to their root/stem form"},
            {"name": "lemmatization", "description": "Reduce words to their base form"},
        ]

    def preprocess_text(self, text, options):
        result = text
        visualizations = []

        if options.get("tokenize"):
            tokens = word_tokenize(result)
            result = " ".join(tokens)
            visualizations.append(("Tokens", tokens))

        if options.get("stop_words"):
            stop_words = set(stopwords.words("english"))
            tokens = word_tokenize(result)
            filtered_tokens = [
                word for word in tokens if word.lower() not in stop_words
            ]
            result = " ".join(filtered_tokens)
            visualizations.append(("Without Stop Words", filtered_tokens))

        if options.get("stem"):
            stemmer = PorterStemmer()
            tokens = word_tokenize(result)
            stemmed_tokens = [stemmer.stem(word) for word in tokens]
            result = " ".join(stemmed_tokens)
            visualizations.append(("Stemmed", stemmed_tokens))

        if options.get("lemmatize"):
            lemmatizer = WordNetLemmatizer()
            tokens = word_tokenize(result)
            lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
            result = " ".join(lemmatized_tokens)
            visualizations.append(("Lemmatized", lemmatized_tokens))

        return result, visualizations


def main():
    st.title("Interactive NLP Demo")

    nlp_demo = NLPDemo()

    # Input section
    st.header("Input Text")
    input_type = st.radio("Input Type", ["Text", "File"])

    if input_type == "Text":
        text = st.text_area("Enter your text here")
    else:
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file:
            text = uploaded_file.getvalue().decode()
        else:
            text = ""

    # Preprocessing options
    st.header("Preprocessing Options")
    options = {
        "tokenize": st.checkbox("Tokenization"),
        "stop_words": st.checkbox("Remove Stop Words"),
        "stem": st.checkbox("Stemming"),
        "lemmatize": st.checkbox("Lemmatization"),
    }

    if text and any(options.values()):
        processed_text, visualizations = nlp_demo.preprocess_text(text, options)

        # Display results
        st.header("Results")

        # Original text
        st.subheader("Original Text")
        st.write(text)

        # Processed text
        st.subheader("Processed Text")
        st.write(processed_text)

        # Visualizations
        st.header("Analysis")
        for title, tokens in visualizations:
            st.subheader(title)
            df = pd.DataFrame({"token": tokens})
            fig = px.histogram(df, x="token")
            st.plotly_chart(fig)


if __name__ == "__main__":
    main()
