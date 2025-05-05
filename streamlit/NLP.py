import nltk.corpus
import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize, WhitespaceTokenizer, wordpunct_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
pst = PorterStemmer()
lcs = LancasterStemmer()
sbst = SnowballStemmer(language="english")
word_net = WordNetLemmatizer()

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

st.subheader('Stemming')
st.text("Select one of the following stemmer to see result for each word in the text box above")



bt1 = st.button(label = 'LancasterStemmer')
bt2 = st.button(label = 'PorterStemmer')
bt3 = st.button(label = 'SnowballStemmer')


word_tokens = nltk.word_tokenize(text)
stop_words = stopwords.words('english')

filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]
dic = {}


if bt1:
    for i in filtered_sentence:
        dic[i] = lcs.stem(i)
    st.write(dic)
    
if bt2:
    for i in filtered_sentence:
        dic[i] = pst.stem(i)
    st.write(dic)
    
if bt3:
    for i in filtered_sentence:
        dic[i] = sbst.stem(i)
    st.write(dic)
    
    
    

st.subheader('Lemmmatization')

st.text("Press the button to Lemmatize the text")
bt4 = st.button(label = "WordNetLemmatizer")

if bt4:
    for i in filtered_sentence:
        dic[i] = word_net.lemmatize(i)
    st.write(dic)
        