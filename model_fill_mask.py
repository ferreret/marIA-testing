from transformers import pipeline
from util import print_result


def init(type_data):
    if type_data == 'base':
        model = 'PlanTL-GOB-ES/roberta-base-bne'
    elif type_data == 'large':
        model = 'PlanTL-GOB-ES/roberta-large-bne'

    unmasker = pipeline('fill-mask', model=model)

    while True:
        mask = input(
            'Introduce una frase con una palabra a completar marcada como <mask>: \n')

        result = unmasker(mask)
        print_result(result)

        if input('¿Quieres probar otra frase? (y/n): ') == 'n':
            break
