class NotEnoughMoneyError(Exception):
    pass


def check_name(name):
    if name == "":
        raise ValueError("Имя не может быть пустым")
    return name


def check_age(age):
    try:
        age = int(age)
    except:
        raise ValueError("Возраст должен быть числом")
    if age < 12:
        raise ValueError("Слишком маленький возраст")
    return age


def check_tickets(count):
    try:
        count = int(count)
    except:
        raise ValueError("Некорректное количество билетов")
    if count <= 0 or count > 5:
        raise ValueError("Некорректное количество билетов")
    return count


def check_money(money):
    try:
        money = float(money)
    except:
        raise ValueError("Некорректный бюджет")
    if money < 0:
        raise ValueError("Некорректный бюджет")
    return money


def calc_price(count):
    return count * 500


# Главная часть
print("Бронирование билетов")

user_name = input("Имя: ")
user_age = input("Возраст: ")
ticket_count = input("Кол-во билетов: ")
user_money = input("Сколько денег: ")

try:
    user_name = check_name(user_name)
    user_age = check_age(user_age)
    ticket_count = check_tickets(ticket_count)
    user_money = check_money(user_money)

    total_price = calc_price(ticket_count)

    print("Имя:", user_name)
    print("Возраст:", user_age)
    print("Билетов:", ticket_count)
    print("Цена:", total_price)
    print("Денег:", user_money)

    if user_money < total_price:
        raise NotEnoughMoneyError("Не хватает денег")
    print("Сдача:", user_money - total_price)

except ValueError as e:
    print("Ошибка:", e)
except NotEnoughMoneyError as e:
    print("Ошибка:", e)