from transformers import pipeline
from util import print_result


def init(type_data):
    if type_data == 'base':
        model = 'PlanTL-GOB-ES/roberta-base-bne-capitel-pos'
    elif type_data == 'large':
        model = 'PlanTL-GOB-ES/roberta-large-bne-capitel-pos'

    nlp = pipeline('token-classification', model=model)

    while True:
        sentence = input(
            'Introduce una frase para obtener el POS de cada palabra: \n')

        result = nlp(sentence)
        print_result(result)

        if input('¿Quieres probar otra frase? (y/n): ') == 'n':
            break
