def analisar_frase(frase):
    frase_normalizada = frase.lower()
  
    palavras = frase.split()
    qtd_palavras = len(palavras)
    
    vogais = "aeiou"
    qtd_vogais = sum(1 for letra in frase_normalizada if letra in vogais)
    qtd_consoantes = sum(1 for letra in frase_normalizada if letra.isalpha() and letra not in vogais)
    
    apenas_letras = "".join(c for c in frase_normalizada if c.isalpha())
    eh_palindromo = apenas_letras == apenas_letras[::-1]
    
    print("\n--- Resumo da Análise ---")
    print(f"Palavras: {qtd_palavras}")
    print(f"Vogais: {qtd_vogais}")
    print(f"Consoantes: {qtd_consoantes}")
    print(f"É um palíndromo? {'Sim' if eh_palindromo else 'Não'}")


frase = input("Digite uma frase para analisar: ")
analisar_frase(frase)
