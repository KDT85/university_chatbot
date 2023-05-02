import re
import nltk
from nltk import pos_tag, ne_chunk
from nltk.corpus.reader.tagged import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# defining our functions

# function to find the best matching question-answer pair
def find_best_match(user_input, qa_pairs):
    best_match_pair = None
    best_match_score = 0
    for pair in qa_pairs:
        question = pair["question"]
        score = get_similarity_score(user_input, question)
        if score > best_match_score:
            best_match_pair = pair
            best_match_score = score
    return best_match_pair

# function to get the similarity score between two strings
def get_similarity_score(str1, str2):
    tokens1 = word_tokenize(str1.lower())
    tokens2 = word_tokenize(str2.lower())
    return len(set(tokens1) & set(tokens2))

# function to extract named entities from a string
def extract_named_entities(text):
    named_entities = []
    chunks = ne_chunk(pos_tag(word_tokenize(text)))
    for subtree in chunks.subtrees():
        if subtree.label() == 'NE':
            named_entity = " ".join([token for token, pos in subtree.leaves()])
            named_entities.append(named_entity)
    return named_entities

def tokenize_word(txt):
    tokenized_word = word_tokenize(txt)
    return tokenized_word

# function to remove stop words
stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    sent_tokens = sent_tokenize(text)
    cleaned = []
    word_tokens = word_tokenize(text)
    for words in word_tokens:
        if words not in stop_words:
            cleaned.append(words)

    joined = " ".join(cleaned)
    cleaned = joined.split("?")
    temp_list = []
    for _ in cleaned:   
        temp_list.append(_.strip())
    cleaned = temp_list
    return joined

# function to lemmatize the text
lemmatizer = WordNetLemmatizer()
def lemmatize_word(word):
    temp_list = []
    words = tokenize_word(word)
    for word in words:
        temp_list.append(lemmatizer.lemmatize(word))
    joined = " ".join(temp_list)
    return joined
