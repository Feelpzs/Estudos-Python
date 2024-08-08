velocidade_maxima = 100
multa_leve = 180
multa_grave = 550
multa_gravissima = 1500

def calcular_multa (velocidade,velocidade_maxima):
    if velocidade <= velocidade_maxima:
        print ('Não levou multa')

    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print ('Levou multa leve') 

    elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
        print ('levou multa grave')

    elif velocidade > velocidade_maxima + 20:
        print ('Levou multa gravissima')


    calcular_multa (100,130) 