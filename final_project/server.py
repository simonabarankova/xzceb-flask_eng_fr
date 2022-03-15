from urllib import request
from flask import Flask, render_template
from flask import request
import machinetranslation

app = Flask("Translate app")

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/englishToFrench", methods=["GET"])
def translate_to_french():
    text = request.args.get('textToTranslate')
    return machinetranslation.translator.english_to_french(text)

@app.route("/frenchToEnglish", methods=["GET"])
def translate_to_english():
    text = request.args.get('textToTranslate')
    return machinetranslation.translator.french_to_english(text)

if __name__=="__main__":
    app.run(debug=True, port=8080) 
    # When no port is specified, starts at default port 5000
