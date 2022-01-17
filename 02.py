horas = float(input('Diigte o número de horas gastas: '))
if horas < 10:
    total = horas * 0.5
elif horas > 10 and horas < 20:
    total = horas * 0.45
else:
    total = horas * 0.4

round(total, 2)

print(f'O valor a ser pago em R$ é {total}')