from flask import Flask
from utils import get_all, format_candidate, get_by_pk, get_by_skill


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
    # Поиск кандидата по id
    candidate: dict = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidate([candidate])
    return result


@app.route('/skills/<skill>')
def page_candidate(skill):
    # Поиск кандидата по навыкам
    skill_lower = skill.lower()
    candidates: list[dict] = get_by_skill(skill.lower)
    result = format_candidate(candidates)
    return result


app.run()
