import nltk.corpus
import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize, WhitespaceTokenizer, wordpunct_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.title("Natural language Understanding")
st.subheader("Tokenization")
text = st.text_area("Enter a paragraph")


st.markdown(
    """
<style>
button {
    height: 48px;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}
</style>
""",
    unsafe_allow_html=True,
)



fns = ["Word Tokenizer", "Sentence Tokenizer", "Blanklinke Tokenize", "WhiteSpace Tokenizer", "Wordpunct tokenize"]
col = len(fns)
cols = st.columns(col)

buttons = []
for i in range(col):
    with cols[i]:
        btn = st.button(f"{fns[i]}", type = "primary", key = f"btn{i+1}")
        buttons.append(btn)
        
if buttons[0]:
    st.write(word_tokenize(text))
if buttons[1]:
    st.write(sent_tokenize(text))
if buttons[2]:
    st.write(blankline_tokenize(text))
if buttons[3]:
    st.write(WhitespaceTokenizer().tokenize(text))
if buttons[4]:
    st.write(wordpunct_tokenize(text))



st.subheader('Wordcloud')

wc_button = st.button(label = "Generate word cloud for given paragraph")


if wc_button:
    fig, ax = plt.subplots(figsize=(10,8))
    wordcloud = WordCloud(width = 420, height = 200, margin = 2, background_color = "black", colormap = "Accent", mode = "RGBA")
    wordcloud.generate(text)
    plt.imshow(wordcloud, interpolation = 'quadric')
    plt.axis("off")
    plt.margins(x=0, y=0)
    # plt.show()
    st.pyplot(fig)
