from pprint import pprint
import model_fill_mask as mfm
import model_text_generation as mtg
import model_capitel_pos as mcp
import model_capitel_ner as mcn
import model_sqac as msq
import pyfiglet
import sys

# unmasker = pipeline('fill-mask', model='PlanTL-GOB-ES/roberta-base-bne')

# pprint(unmasker(
#     "Gracias a los datos de la BNE se ha podido <mask> este modelo del lenguaje."))


def menu():
    print(pyfiglet.figlet_format('marIA models', font='slant'))
    print('Menú principal')
    print('')
    print('1. RoBERTa-base BNE (Tipo fill-mask <mask>)')
    print('2. RoBERTa-large BNE (Tipo fill-mask <mask>)')
    print('3. GPT2-base BNE')
    print('4. GPT2-large BNE')
    print('5. RoBERTa-base-BNE for Capitel-POS (token-classification)')
    print('6. RoBERTa-large-BNE for Capitel-POS (token-classification)')
    print('7. RoBERTa-base-BNE for Capitel-NER (name entity recognition)')
    print('8. RoBERTa-base-BNE for Capitel-NER plus (name entity recognition)')
    print('9. RoBERTa-large-BNE for Capitel-NER (name entity recognition)')
    print('10. RoBERTa-base-BNE for SQAC (Question Answering)')
    print('11. RoBERTa-large-BNE for SQAC (Question Answering)')

    opcion = input("Elige una opción o 'q' para salir:\n")

    if opcion == '1':
        mfm.init('base')
    elif opcion == '2':
        mfm.init('large')
    elif opcion == '3':
        mtg.init('base')
    elif opcion == '4':
        mtg.init('large')
    elif opcion == '5':
        mcp.init('base')
    elif opcion == '6':
        mcp.init('large')
    elif opcion == '7':
        mcn.init('base')
    elif opcion == '8':
        mcn.init('plus')
    elif opcion == '9':
        mcn.init('large')
    elif opcion == '10':
        msq.init('base')
    elif opcion == '11':
        msq.init('large')
    elif opcion == 'q':
        print('Fin del programa')
        sys.exit()
    else:
        print('Opción no válida')
    menu()


menu()
