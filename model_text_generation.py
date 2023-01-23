from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, set_seed
from util import print_result


def init(type_data):
    if type_data == 'base':
        data = 'PlanTL-GOB-ES/gpt2-base-bne'
    elif type_data == 'large':
        data = 'PlanTL-GOB-ES/gpt2-large-bne'

    tokenizer = AutoTokenizer.from_pretrained(data)
    model = AutoModelForCausalLM.from_pretrained(data)
    generator = pipeline('text-generation', tokenizer=tokenizer, model=model)
    set_seed(42)

    while True:
        sentence = input('Introduce una frase a completar: \n')
        result = generator(sentence,
                           num_return_sequences=5)
        print_result(result)

        if input('¿Quieres probar otra frase? (y/n): ') == 'n':
            break
