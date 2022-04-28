from flask import Flask, render_template, request
from utils import Pre_processing_questions, TFIDF, RandomForest
import nltk
import ast
import joblib
nltk.download('omw-1.4')

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/predict_tags', methods=['POST'])
def predict_tags():
    question = request.form.get('question')
    token_question = Pre_processing_questions.from_area_get_token(question)
    question_merged = [' '.join(token_question)]
    df = TFIDF.tdf_idf_question(question_merged)
    predictions = RandomForest.apply_ml_model(df)[0]
    names = RandomForest.get_namefrom_mlb()

    results = []
    for pred, name in zip(predictions,names):
        if pred == 1 :
            results.append(name)
    return render_template('models_output.html', tags_question = token_question, question = question, results = results)



# https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/

@app.route('/postjson', methods = ['POST'])
def predictwith_JSON():
    question = request.get_json()
    question = question['Question']
    token_question = Pre_processing_questions.from_area_get_token(question)
    question_merged = [' '.join(token_question)]
    df = TFIDF.tdf_idf_question(question_merged)
    predictions = RandomForest.apply_ml_model(df)[0]
    names = RandomForest.get_namefrom_mlb()

    results = []
    for pred, name in zip(predictions,names):
        if pred == 1 :
            results.append(name)

    return str(results)


if __name__ == '__main__':
	app.run(debug=True)