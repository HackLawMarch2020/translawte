from flask import Flask, request, render_template
from functions import get_AWS_Credentials, translate_AWS

ACCESS_ID, ACCESS_KEY = get_AWS_Credentials("credentials.json")

app = Flask(__name__)

TRANSLATION_ERROR = "Translation error"

FoundIssues = ["de 1 000 000 actions", "Société Stock", "lois fédérales", "l'annexe d'information",
               "de la société", "et ayant droit à titre de bénéficiaire",
               "non admissible", "tableau d'information"]

YellowIssues = ["de série A, valeur nominale de 0,001", "de série B, valeur nominale de 0,001", "sur les valeurs mobilières", "fidèle",
                "option d'achat d'actions incitatif (régime incitatif d'ption d'achat d'action)"]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():
    if request.form:
        print(request.form)

    tr = translate_AWS(request.form["data"], ACCESS_ID, ACCESS_KEY)
    return markIssues(tr)

def markIssues(text):
    text = markIssuesFromList(text, FoundIssues, "red")
    text = markIssuesFromList(text, YellowIssues, "orange")
    return text


def markIssuesFromList(text, issueList, color):
    for issue in issueList:
        start = text.find(issue)
        if start > 0:
            end = start+len(issue)
            text = text[:start] + "<font color=\"" + color + "\">" + text[start:end] + "</font>" + text[end:]

    return text


if __name__ == "__main__":
    app.run(debug=True)

