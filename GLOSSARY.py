import streamlit as st
import pandas as pd
from googletrans import Translator

def translate_excel(uploaded_file, source_lang, target_lang):
    """Translates terms in an Excel file.

    Args:
        uploaded_file: The uploaded Excel file.
        source_lang: The source language of the terms.
        target_lang: The target language for translation.

    Returns:
        The translated DataFrame.
    """

    # Read the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Translate terms in column A
    translator = Translator()
    df['Translated Terms'] = df['Terms'].apply(lambda x: translator.translate(x, src=source_lang, dest=target_lang).text)

    return df

def main():
    st.title("Excel Term Translator")

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload an Excel file")

    # Select source and target languages
    source_lang = st.selectbox("Select source language", options=["English", "Spanish", "French", "Other"])
    target_lang = st.selectbox("Select target language", options=["English", "Spanish", "French", "Other"])

    # Translate terms if file is uploaded and languages are selected
    if uploaded_file and source_lang and target_lang:
        translated_df = translate_excel(uploaded_file, source_lang, target_lang)
        st.dataframe(translated_df)

if __name__ == '__main__':
    main()
