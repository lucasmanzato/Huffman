from collections import Counter

class No:
    def __init__(self, valor, caractere=None):
        self.valor = valor
        self.caractere = caractere
        self.esquerda = None
        self.direita = None

def construir_arvore_huffman(caracteres_pesos):
    arvores = [No(peso, caractere) for caractere, peso in caracteres_pesos]
    while len(arvores) > 1:
        arvores.sort(key=lambda x: x.valor)
        esquerda = arvores.pop(0)
        direita = arvores.pop(0)
        nova_arvore = No(esquerda.valor + direita.valor)
        nova_arvore.esquerda = esquerda
        nova_arvore.direita = direita
        arvores.append(nova_arvore)
    return arvores[0]

def codigos_huffman(arvore, prefixo="", codigos=None):
    if codigos is None:
        codigos = {}
    if arvore.caractere is not None:
        codigos[arvore.caractere] = prefixo
    if arvore.esquerda is not None:
        codigos_huffman(arvore.esquerda, prefixo + "0", codigos)
    if arvore.direita is not None:
        codigos_huffman(arvore.direita, prefixo + "1", codigos)
    return codigos

def codificar_texto(texto, codigos):
    texto_codificado = ""
    for caractere in texto:
        texto_codificado += codigos[caractere]
    return texto_codificado

def decodificar_texto(texto_codificado, arvore):
    texto_decodificado = ""
    no_atual = arvore
    for bit in texto_codificado:
        if bit == "0":
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita
        if no_atual.caractere is not None:
            texto_decodificado += no_atual.caractere
            no_atual = arvore
    return texto_decodificado

def contar_pesos(texto):
    contagem = Counter(texto)
    return [(caractere, peso) for caractere, peso in contagem.items()]

def main():
    texto_original = "Lucas"
    caracteres_pesos = contar_pesos(texto_original)
    arvore_huffman = construir_arvore_huffman(caracteres_pesos)
    codigos = codigos_huffman(arvore_huffman)
    
    texto_codificado = codificar_texto(texto_original, codigos)
    
    print("Texto Original:", texto_original)
    print("Representação Binária:", ''.join(format(ord(char), '08b') for char in texto_original))
    print("Códigos Huffman:")
    for caractere, codigo in sorted(codigos.items()):
        print(f"'{caractere}': {codigo}")
    
    print("Texto Codificado:", texto_codificado)
    
    texto_decodificado = decodificar_texto(texto_codificado, arvore_huffman)
    print("Texto Decodificado:", texto_decodificado)

if __name__ == "__main__":
    main()
