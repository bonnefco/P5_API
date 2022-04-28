from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import re

##Delete html balises
def delete_balise_html(question):
    return BeautifulSoup(question).get_text()

#Delete code in code
def delete_code_balise_in_html(string_to_modify):
  soup = re.sub('<[^<]+?>', '', string_to_modify)
  return soup

#Tokenize
def delete_code_balise_in_html_and_tokenize(soup):
  tokenizer = nltk.RegexpTokenizer(r'\w+')
  soup = tokenizer.tokenize(soup.lower())
  soup = [element for element in soup if len(element)>1]
  return soup

#Lemantization 
def lemmatizer_delete_words_in_corpus(list_of_words_tokenized) :

    lemmatizer = WordNetLemmatizer()
    list_of_words_tokenized_lemmantized = []
    for token in list_of_words_tokenized:
        lemmetized_word = lemmatizer.lemmatize(token)
        list_of_words_tokenized_lemmantized.append(lemmetized_word)
    
    return list_of_words_tokenized_lemmantized

#Delete_stop_words nltk

def delete_stop_words_in_corpus(x) :
    words_corpus = ['the', 'to', 'in', 'is', 'and', 'this', 'it', 'of', 'for', 'that', 'with', 'my', 'but', 'not', 'on', 'have', 'how', 'can', 'at', 'if', 'from', 'a', 'file', 'be', 'error']
    stop_words = list(set(stopwords.words('english')))+words_corpus
    for element in stop_words :
        while element in x: x.remove(element)
    return x

def delete_smallest(list_of_words):
  new_list = [element for element in list_of_words if len(element)>1]
  new_list_bis = []
  for element in new_list :
    try:
        int(element)
    except ValueError:
        new_list_bis.append(element)
  return new_list_bis

def delete_if_not_in(liste):
    words_to_keep = open(r'C:\Users\Corentin\Desktop\Vie\Post_ecole_inge\Alternance\projet5\moi\API\moi_json\utils\words_to_keep.txt', 'r')
    lines = words_to_keep.readlines()
    words_to_keep = []
    for line in lines : 
        words_to_keep.append(line[:-1])
    words_in_list = [i for i in liste if i in words_to_keep]
    return list(set(words_in_list))

def from_area_get_token(question):
    question = delete_balise_html(question)
    question = delete_code_balise_in_html(question)
    question = delete_code_balise_in_html_and_tokenize(question)
    question = lemmatizer_delete_words_in_corpus(question)
    question = delete_stop_words_in_corpus(question)
    question = delete_smallest(question)
    question = delete_if_not_in(question)

    return question
