import json


# функция, которая загрузит данные из файла
def load_candidates() -> list[dict]:
    with open('candidates.json', 'rt', encoding='utf-8') as file:
        data = json.load(file)
        return data


def format_candidate(candidates: list[dict]) -> str:
    # Форматирование списка кандидатов
    candidates = load_candidates()
    result = '<pre>'

    for candidate in candidates:
        result += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}"
    result += '<pre>'
    return result


def get_all() -> list[dict]:
    # покажет всех кандидатов
    return load_candidates()


# вернет кандидата по pk
def get_by_pk(uid: int) -> dict | None:
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None

# вернет кандидатов по навыку
def get_by_skill(skill: str) -> list[dict]:
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
