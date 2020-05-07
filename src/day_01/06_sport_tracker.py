"""
Пример программы для работы с циклами

Данные
- количество калорий = 5000
- сброс калорий за один шаг = 340

Сделать
- написать цикл для расчета шагов для сброса до 3600 калорий
- каждый шаг выводить в формате "Шаг НОМЕР, калории КОЛИЧЕСТВО"
- после достижения цели вывести сообщение "Шагов сделано: КОЛИЧЕСТВО"
"""
cal = 5000
step = 340
cnt = 0
while cal > 3600:
    cal = cal - step
    cnt += 1
    print(f"Шаг {cnt}, каллории {cal}")
else:
    print(f"Шагов сделано: {cnt}")
cal = 5000
step = 340
step_count = 0

while cal > 3600:
    cal = cal - step
    step_count = step_count + 1

    print(f"Шаг {step_count}, каллории {cal}")
else:
    print(f"Шагов сделано - {step_count}")
