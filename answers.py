# def find_person(name):
#     list_of_names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#     counter = 0
#     for n in list_of_names:
#         if n == name:
#             print("{} has been found".format(list_of_names.pop(counter)))
#         counter +=1
#     print(list_of_names)

def ask_user():
    print("Привет")
    while True:
        answer = input('Спроси что нибудь: ')
        if answer == "Пока":
            print('Увидимся еще!')
            break
        elif answer.__contains__("?"):
            try:
                get_answer(answer.lower())
            except KeyError:
                print('Напиши верный вопрос!')


def get_answer(question):
    answers = {"как дела?": "Отлично!",
               "что делаешь?": "Отвечаю тебе =)",
               "сколько тебе лет?": "Очень много"}
    print(answers[question])

if __name__=="__main__":
    ask_user()