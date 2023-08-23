import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Função para converter uma sentença em cláusula de predicado em formato Prolog
def convert_to_predicate_clause(subject, verb, objects):
    argument_list = ', '.join(objects)
    return f"{verb}({subject}, {argument_list})."

def main():
    input_text = input("Digite o texto: ")
    
    sentences = sent_tokenize(input_text)
    predicate_clauses = []
    
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tagged_tokens = pos_tag(tokens)
        
        subject = None
        verb = None
        objects = []
        
        for token, tag in tagged_tokens:
            if tag.startswith('N') and not subject:
                subject = token.lower()
            elif tag.startswith('V') and not verb:
                verb = token.lower()
            elif tag.startswith('N') or tag.startswith('V'):
                objects.append(token.lower())
        
        if subject and verb:
            clause = convert_to_predicate_clause(subject, verb, objects)
            predicate_clauses.append(clause)

    print("\nCláusulas de predicado (formato Prolog):\n")
    if predicate_clauses:
        for clause in predicate_clauses:
            print(clause)
    else:
        print("Não foi possível criar cláusulas de predicado para o texto fornecido.")

if _name_ == "_main_":
    main()