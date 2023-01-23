from transformers import pipeline
from util import print_result


def init(type_data):
    if type_data == 'base':
        model = 'PlanTL-GOB-ES/roberta-base-bne-capitel-ner'
    elif type_data == 'plus':
        model = 'PlanTL-GOB-ES/roberta-base-bne-capitel-ner-plus'
    elif type_data == 'large':
        model = 'PlanTL-GOB-ES/roberta-large-bne-capitel-ner'

    nlp = pipeline('ner', model=model)

    while True:
        sentence = input(
            'Introduce una frase para obtener las entidades: \n')

        result = nlp(sentence)
        print_result(result)

        if input('¿Quieres probar otra frase? (y/n): ') == 'n':
            break
