from flask import render_template, Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    title = request.args.get('title', 'Mission to Mars')
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        type_prof = "Научные симуляторы"
        image_dir = url_for('static', filename='img/train.jpg')
    else:
        type_prof = "Тренажеры"
        image_dir = url_for('static', filename='img/train1.jpg')

    return render_template("trainings.html", title=type_prof, type_prof=type_prof,
                           image_dir=image_dir)


@app.route('/list_prof/<type_prof>')
def list_profs(type_prof):
    list_prof = ["Инженер-исследователь", "Пилот", "Строитель", "Климатолог", "Астрогеолог", "Метеоролог",
                 "Штурман", "Пилот дронов", "Киберинженер", "Экзобиолог", "Ученый", "Врач"]
    return render_template("list_prof.html", list_prof=list_prof, types=type_prof)


@app.route('/')
@app.route('/auto_answer')
@app.route('/answer')
def answer():
    person = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
              'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
              'ready': 'True'}
    return render_template("anwser.html", title="Анкета", person=person,
                           css=url_for('static', filename='css/anwser_style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
