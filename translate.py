from flask import Flask, request, render_template

app = Flask(__name__)

TRANSLATION_ERROR = "Translation error"

FoundIssues = ["de (dont)", "Les", "Société Stock", "lois fédérales (de l'État)", "l'annexe d'information",
               "de la société (des actions de la société)", "et ayant droit à titre de bénéficiaire (inscrite et à titre véritable)",
               "de la société (d'actions de la société)", "non admissible (non qualifiées)", "tableau d'information"]

YellowIssues = ["à une valeur nominale de 0,001", "sur les valeurs mobilières", "fidèle",
                "option d'achat d'actions incitatif (régime incitatif d'ption d'achat d'action)"]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():
    if request.form:
        print(request.form)

    tr = getTranslated(request.form["data"])
    return markIssues(tr)


def getTranslated(text):
    # Translate the text from the translation service

    tr = {
        "(a) The au": "(a) Le capital-actions autorisé de la Société se compose uniquement de (i) 40 000 000 d'actions ordinaires d'une valeur nominale de 0,001 $(« actions ordinaires »), dont 12 000 actions ordinaires sont émises et en circulation, (ii) 11 000 000 d'actions privilégiées de série A à une valeur nominale de 0,001 $(« actions privilégiées de série A »), de (dont) 1 000 000 000 Les actions privilégiées de série A sont émises et en circulation, (iii) 5 000 000 d'actions privilégiées de série B à valeur nominale de 0,001 $(« actions privilégiées de série B »), dont 4 000 000 d'actions privilégiées de série B sont émises et en circulation.",
        "The Compan": "Les actions ordinaires, les actions privilégiées de série A et les actions privilégiées de série B de la société sont collectivement appelées « actions de la société ». Toutes les actions émises et en circulation des actions de la Société et le capital-actions de chaque Filiale de la Société ont été dûment autorisées et sont valablement émises, intégralement payées et non imposables.",
        "All of the": "Toutes les actions émises et en circulation de la Société Stock ont été émises conformément aux lois fédérales (de l'État) et fédérales sur les valeurs mobilières. L'annexe 3.2 a) de l'annexe d'information contient une liste fidèle et complète des détenteurs d'actions de la société (des actions de la société) et le nombre de ces actions détenues et ayant droit à titre de bénéficiaire (inscrite et à titre véritable) par chacun de ces détenteurs.",
        "Schedule 3": "L'annexe 3.2 (a) de l'annexe d'information contient une liste fidèle et complète des options d'achat d'actions en circulation à la date des présentes, y compris le nom de chacun de ces détenteurs, le nombre d'actions de la société (d'actions de la société) assujetties à chacune de ces options d'achat d'actions, le prix d'exercice par action pour chacune de ces options d'achat d'actions, le la date d'attribution de chacune de ces options d'achat d'actions et si chacune de ces options d'achat d'actions était destinée, au moment de l'émission, à être une option d'achat d'actions incitatif (régime incitatif d'ption d'achat d'action) ou une option d'achat d'actions non admissible (non qualifiées).",
        "(a) Except": "(a) Sauf dans les cas prévus à l'annexe 3.2 (b) du tableau d'information, la Société est et sera, à la date de clôture, le seul détenteur effectif et effectif de toutes les actions émises et en circulation du capital-actions de chaque Filiale de la Société, libre et libre de tout privilège.",
        "For purpos": "Aux fins de la présente entente, le terme « privilèges » désigne les charges, créances, intérêts immobiliers communautaires, contrats de vente conditionnelle ou autres contrats de réserve de propriété, conventions, servitudes, charges, intérêts équitables, privilèges, hypothèques, options, nantissements, droits de premier refus, restrictions d'utilisation des bâtiments, les droits de passage, les sûretés, les servitudes, les privilèges légaux, les variances ou les restrictions, y compris les restrictions relatives au vote, au transfert, à l'aliénation, à la réception de revenus ou à l'exercice de tout autre attribut de propriété, à l'exception (i) des privilèges pour les impôts non encore dus et payables ou pour les impôts que le contribuable est contester de bonne foi par le biais de procédures appropriées, (ii) sauf en ce qui concerne les actions et options d'achat, les privilèges sur le fonds d'achat et les privilèges garantissant des paiements de location en vertu d'accords de location-acquisition, et (iii) les autres imperfections mineures du titre qui n'ont aucune incidence importante sur la propriété ou l'utilisation de la propriété applicable.",
    }
    key = text[:10]
    if key in tr:
        return tr[key]
    else:
        return TRANSLATION_ERROR


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

