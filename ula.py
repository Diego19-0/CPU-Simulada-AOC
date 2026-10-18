"""
ULA — Código-base para o projeto de CPU Simulada
AOC 2026.2

Os alunos devem implementar as operações marcadas como IMPLEMENTAR.
"""

def limitar_8bits(valor):
    return valor & 0xFF


def ula(operacao, a, b=0):
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    if operacao == "ADD":
        resultado = limitar_8bits(a + b)

    elif operacao == "SUB":
        resultado = limitar_8bits(a - b)

    elif operacao == "AND":
        resultado = limitar_8bits(a & b)

    elif operacao == "OR":
        resultado = limitar_8bits(a | b)

    elif operacao == "XOR":
        resultado = limitar_8bits(a ^ b)

    else:
        raise ValueError(f"Operação inválida: {operacao}")

    return limitar_8bits(resultado)
