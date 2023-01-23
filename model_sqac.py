from transformers import pipeline
from util import print_result


def init(type_data):
    if type_data == 'base':
        data = 'PlanTL-GOB-ES/roberta-base-bne-sqac'
    elif type_data == 'large':
        data = 'PlanTL-GOB-ES/roberta-large-bne-sqac'

    nlp = pipeline("question-answering", model=data)

    while True:
        context = input('Introduce el texto del contexto:\n')
        text = input('Introduce la pregunta:\n')
        qa_results = nlp(text, context)
        print_result(qa_results)

        if input('¿Quieres probar otra ? (y/n): ') == 'n':
            break
