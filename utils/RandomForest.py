import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn
from pandas import Timestamp
import calendar
from collections import Counter, defaultdict
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.preprocessing import MultiLabelBinarizer, LabelBinarizer
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score, precision_score, recall_score, f1_score, classification_report, plot_roc_curve
from sklearn.multioutput import MultiOutputClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import MultinomialNB
import ast
import time

def apply_ml_model(df):
    model_rf = joblib.load(r'C:\Users\Corentin\Desktop\Vie\Post_ecole_inge\Alternance\projet5\moi\API\moi_json\models_pkl\model_L_R_after_PCA.pkl')
    predictions = model_rf.predict(df)
    return predictions

def get_namefrom_mlb():
    model_mlb = joblib.load(r'C:\Users\Corentin\Desktop\Vie\Post_ecole_inge\Alternance\projet5\moi\API\moi_json\models_pkl\model_mlb.pkl')
    model_mlb.classes_
    return model_mlb.classes_
