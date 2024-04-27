from flask import render_template, Flask, url_for, request

app = Flask(__name__)


@app.route('/')
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
