velocidade = float(input('Digite sua velocidade em km/h: '))
if velocidade > 80.0:
    multa = round((velocidade - 80) * 7.0, 2)
    print(f'Você estava acima do limite de 80 km/h e deve pagar R$ {multa} pois esta {velocidade - 80} km/h acima do '
          f'limite.')
else:
    print('Você estava dentro do limite ')
