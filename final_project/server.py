from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    print(json.dumps(translator.english_to_french(textToTranslate), indent=2, ensure_ascii=False))
    translated_string1 = translator.english_to_french(textToTranslate)
    return translated_string1

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    print(json.dumps(translator.french_to_english(textToTranslate), indent=2, ensure_ascii=False))
    translated_string2 = translator.french_to_english(textToTranslate) 
    return translated_string2

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
