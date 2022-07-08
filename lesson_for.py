classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_class_avg(student_scores):
    scores_sum = 0
    for score in student_scores:
        scores_sum += score
    return scores_sum/len(student_scores)

school_avg_sum = 0
for one_class in classes:
    class_avg = count_class_avg(one_class['scores'])
    print(f"Средняя оценка класса {one_class['name']}: {class_avg}")
    school_avg_sum += class_avg

print(f"Средняя оценка по школе равняется {round(school_avg_sum/len(classes),2)}")

"""
stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

def discounted(price, discount, max_discount=30, phone_name=""):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)

for phone in stock:
    phone['price_final']= discounted(phone['price'], phone['discount'], phone_name=phone['name'])

print(stock)


grades = [3, 5, 4, 5, 2, 3]

avg_score =0
for score in grades:
    avg_score = avg_score + score

class_avg =avg_score/len(grades)

print(class_avg)


for number in range(3):
    print(f"Номер {number}")

for letter in 'python':
    print(letter.upper())

my_string = "hi, i`m going to learn Python!"

for word in my_string.split():
    print(f"Длина слова {word} имеет {len(word)} буков")
"""