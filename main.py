
from cpu import CPU


# Funcao para executar um programa na CPU
def executar_programa(nome, instrucoes):

    cpu = CPU()

    # Coloca as instrucoes na memoria
    for endereco, instrucao in enumerate(instrucoes):
        cpu.memoria[endereco] = instrucao

    print()
    print("================================")
    print(nome)
    print("================================")

    # Inicia a execucao
    cpu.executar()

    # Mostra o resultado final
    print()
    print("Execucao encerrada!")
    print("Memoria[15]:", cpu.memoria[15])

    return cpu


# Programa de exemplo do professor
programa_exemplo = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT"
]


# Programa proprio com 8 instrucoes
programa_proprio = [
    "LOAD R0, 10",
    "LOAD R1, 3",
    "ADD R0, R1",
    "LOAD R2, 4",
    "SUB R0, R2",
    "XOR R0, R1",
    "STORE R0, 15",
    "HALT"
]


# Executa os dois programas
if __name__ == "__main__":

    executar_programa(
        "PROGRAMA 1 - EXEMPLO DO PROFESSOR",
        programa_exemplo
    )

    executar_programa(
        "PROGRAMA 2 - PROGRAMA PROPRIO",
        programa_proprio
    )
