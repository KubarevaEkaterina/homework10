from flask import Flask
from utils import load_candidates, get_all, format_candidate


app = Flask(__name__)


@app.route('/')
# функция, которая покажет главную страницу
def page_main():
    # Главная страница
    candidates: list[dict] = get_all()
    result: str = format_candidate(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):



app.run()
