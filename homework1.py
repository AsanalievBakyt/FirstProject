import random
distance = int(input('введите расстояние: '))
workload = random.randint(50,150)
start_sum = 0
som_per_km = 0
force = 0
total = 0

if workload < 50:
    start_sum = 70
    som_per_km = 15
elif 50 < workload < 80:
    start_sum = 65
    som_per_km = 13
else:
    start_sum = 39
    som_per_km = 10


if distance > 30:
    force = 1000
elif 15 < distance < 30:
    force = 500

total = start_sum + (som_per_km * distance) + force
print('общая стоимость', total)


