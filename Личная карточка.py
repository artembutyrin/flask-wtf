from flask import render_template, Flask, url_for, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'


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


class LoginForm(FlaskForm):
    austronavt_username = StringField('Id астронавта', validators=[DataRequired()])
    austronavt_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_username = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('login.html', title='Авторизация', form=form,
                           css=url_for('static', filename='css/authorization_style.css'),
                           img=url_for('static', filename='img/icon.png'))


@app.route('/distribution')
def distribution():
    user_list = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('rooms_order.html', title='Расселение', user_list=user_list)


@app.route('/table/<sex>/<int:year>')
def table(sex, year):
    if sex == "male":
        img = "blue"
    else:
        img = "red"
    if int(year) <= 21:
        img2 = "male.png"
        img += "dark.png"
    else:
        img += ".png"
        img2 = "female.png"

    return render_template('style_room.html', title='Дизайн', css=url_for("static", filename="css/style_room.css"),
                           img=url_for("static", filename=f"img/{img}"),
                           img2=url_for("static", filename=f"img/{img2}"))


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"static/img/cash/{len(os.listdir('static/img/cash'))}.png")
    print([url_for("static", filename=f"img/cash/{file}")
           for file in os.listdir('static/img/cash')])
    return render_template('carousel.html', title='Дизайн',
                           imgs=[url_for("static", filename=f"img/cash/{file}")
                                 for file in os.listdir('static/img/cash')])


@app.route('/memory')
def memory():
    with open("templates/peoples.json", mode="r") as json_file:
        data = json.load(json_file)
    return render_template('memory.html', title='Анкета', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
