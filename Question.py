
class Question:

    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer - 1

    def display_questions(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f'{i}. {option}')

    def check_answer(self, player_answer):
        return player_answer - 1 == self.correct_answer

questions = [
    Question('В каком году основан Python?', ["1991", "2000", "1989", "2005"], 1),
    Question('Что является основным принципом ООП?', ["Инкапсуляция", "Наследование", "Полиморфизм", "Абстракция"], 3 ),
    Question('Столица России?', ['Казань', 'Набережные челны', 'Санкт-Петербург', 'Москва'], 4),
    Question('Какая кошка самая большая на земле?', ['Лев', 'Тигр', 'Гепард', 'Барс'], 2),
    Question('Какие животное самое крупное на земле?', ['Слон', 'Синий кит', 'Кашалот', 'Гиганский Кальмар'], 2),
    Question("Кто автор 'Войны и мира'?",["Фёдор Достоевский", "Лев Толстой", "Иван Тургенев","Александр Пушкин"], 2),
    Question("В каком году произошла Великая Французская революция?",["1776", "1789", "1804", "1815"], 1),
    Question("Какой химический элемент обозначается символом 'O'?",["Кислород", "Углерод", "Гелий", "Натрий"], 1),
    Question("Какая столица Японии?", ["Шанхай", "Пекин", "Сеул", "Токио"], 4),
    Question("Как называется самая большая планета в Солнечной системе?",["Марс", "Венера", "Юпитер", "Сатурн"], 3),
    Question("Кто изображен на картине 'Мона Лиза'?",["Рембрандт", "Леонардо да Винчи", "Ван Гог", "Пикассо"], 2),
]

def run_quiz(player):
    player_score = 0
    for question in questions:
        question.display_questions()
        player_answer = int(input('Выберите номер правильного ответа: '))
        if question.check_answer(player_answer):
            print('Правильно!\n')
            player_score += 1
        else:
            print('Неправильно, правильный ответ: ', question.correct_answer + 1, '\n')
    return player_score

player1_score = run_quiz('Игрок 1')
player2_score = run_quiz('Игрок 2')

print('Результаты: \n')
print('Игрок 1:', player1_score, 'очков')
print('Игрок 2:', player2_score, 'очков')

if player1_score > player2_score:
    print('Игрок 1 победил!')
elif player2_score > player1_score:
    print('Игрок 2 победил!')
else:
    print('Ничья!')