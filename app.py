from datetime import datetime

from flask import (Flask, Response, flash, make_response, redirect,
                   render_template, request, session, url_for)
from flask_admin import Admin
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from adminview import MoviesView, MyAdminIndexView, MyModelView, OrderView
from api_bp.api import api_bp
from models import Movies, Order, User, db

app = Flask(__name__,
            static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://app:123@localhost:5430/flaskDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'newsletters.with.love@gmail.com'
app.config['MAIL_PASSWORD'] = 'wdpj uywv jjkf xbom'

app.config['FLASK_ADMIN_SWATCH'] = 'cyborg'

db.init_app(app)
mail = Mail(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

admin = Admin(app, index_view=MyAdminIndexView(), name='ExampleStore',
              template_mode='bootstrap3')

admin.add_view(MyModelView(User, db.session))
admin.add_view(MoviesView(Movies, db.session))
admin.add_view(OrderView(Order, db.session))

app.register_blueprint(api_bp, url_prefix="/api")


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


@app.route('/home', methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    session.modified = True
    session["Cart"] = {"items": {}, "total": 0}
    movies = Movies.query.all()
    if request.method == 'POST':
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        msg = Message("Клиент оставил обращение на сайте",
                      sender='newsletters.with.love@gmail.com', recipients=[email])
        msg.body = f"Номер телефона клиента: {phone}, почта клиента: {email}, сообщение от клиента: {message}"
        try:
            mail.send(msg)
            flash('Успешно отправлено!', 'success')
        except Exception as e:
            flash(f'Произошла ошибка: {str(e)}', 'danger')
        return redirect('/home')
    return render_template('home.html', movies=movies)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = User.query.filter(User.email == email).one()
        except:
            flash("Пользователь с указанными данными не найден")
            return redirect("/login")
        if check_password_hash(user.password, password):
            if user.role == 2:
                login_user(user)
                return redirect("/")
            else:
                login_user(user)
                return redirect('/admin')
        else:
            flash("Пользователь с указанными данными не найден")
            return redirect('/login')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session["Cart"] = {"items": {}, "total": 0}
    logout_user()
    flash('Вы успешно вышли!', 'info')
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=password, role=2)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
        except:
            return "Добавление не удалось"
    else:
        return render_template('register.html')


@app.route('/films')
def films():
    movies = Movies.query.filter(Movies.kind == 'Movie')
    return render_template('films.html', movies=movies)


@app.route('/tvseries')
def tvseries():
    tvseries = Movies.query.filter(Movies.kind == 'TV Series')
    return render_template('tvseries.html', movies=tvseries)


@app.route('/cartoons')
def cartoons():
    cartoons = Movies.query.filter(Movies.kind == 'Cartoon')
    return render_template('cartoons.html', movies=cartoons)


@app.route('/item/<int:movie_id>', methods=['GET', 'POST'])
def show_item(movie_id: int):
    if request.method == 'GET':
        item = Movies.query.filter(
            Movies.id == movie_id).first()
        return render_template('film.html', item=item)
    return Response("Данную страницу можно посетить только после посещения каталога", 404)


@app.route('/add_to_cart/<int:movie_id>', methods=['GET', 'POST'])
def add_to_cart(movie_id: int):
    if request.method == 'POST':
        if "Cart" in session:
            if not str(movie_id) in session["Cart"]["items"]:
                session["Cart"]["items"][str(movie_id)] = {
                    "movie": movie_id, "qty": 1}
                session.modified = True
            else:
                session.modified = True
        return redirect("/cart")
    return redirect("/home")


@app.route("/cart")
def cart():
    if "Cart" in session:
        session["Cart"]["total"] = 0
        for movie_id in session["Cart"]["items"]:
            movie = Movies.query.filter(Movies.id == movie_id).first()
            session["Cart"]["items"][movie_id] = {"item": movie.title,
                                                  "qty": session["Cart"]["items"][movie_id]["qty"],
                                                  "price": movie.price * session["Cart"]["items"][movie_id]["qty"]}
            session.modified = True
            session["Cart"]["total"] += session["Cart"]["items"][movie_id]["price"]
        return render_template("cart.html", cart=session["Cart"])


@app.route("/remove_item/")
def remove_from_cart():
    movie_id = request.args.get("movie_id")
    session["Cart"]["items"].pop(str(movie_id))
    session.modified = True
    return redirect("/cart")


@app.route("/make_order")
def make_order():
    if "Cart" in session and session["Cart"]["total"] != 0:
        if current_user.is_authenticated:
            new_order = Order(user_id=current_user.get_id(),
                              date=datetime.now(),
                              total=session["Cart"]["total"])
            for movie_id in session["Cart"]["items"]:
                for _ in range(session["Cart"]["items"][movie_id]["qty"]):
                    movie = Movies.query.filter(Movies.id == movie_id).first()
                    new_order.cart.append(movie)
            db.session.add(new_order)
            db.session.commit()
            session["Cart"] = {"items": {}, "total": 0}
            return redirect('/')
        else:
            return redirect("/login")
    else:
        return redirect("/")


@app.route('/cookies')
def cookies():
    res = make_response("Send cookie")
    res.set_cookie("Name", "Valya", max_age=60 * 60 * 24 * 365)
    return res


@app.route('/show_cookies')
def show():
    if request.cookies.get("Name"):
        return "Hello" + request.cookies.get("Name")
    else:
        return "No cookies"


@app.route('/delete_cookies')
def delete_cookies():
    res = make_response("Мы тебе удаляем куку")
    res.set_cookie("Name", "aaa", max_age=0)
    return res


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
