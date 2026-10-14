
class CPU:

    def __init__(self):
        # Quatro registradores de 8 bits
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # Memoria com 16 posicoes
        self.memoria = [0] * 16

        # Contador de programa
        self.pc = 0

        # Indica se a CPU parou
        self.halted = False

    # Limita um numero a 8 bits
    def limitar_8bits(self, valor):
        return valor & 0xFF

    # Unidade Logica e Aritmetica
    def ula(self, operacao, a, b):

        if operacao == "ADD":
            resultado = a + b

        elif operacao == "SUB":
            resultado = a - b

        elif operacao == "AND":
            resultado = a & b

        elif operacao == "OR":
            resultado = a | b

        elif operacao == "XOR":
            resultado = a ^ b

        else:
            raise ValueError("Operacao da ULA invalida")

        return self.limitar_8bits(resultado)

    # Executa uma instrucao
    def executar_instrucao(self, instrucao):

        partes = instrucao.replace(",", "").split()
        operacao = partes[0]

        # LOAD: coloca um valor no registrador
        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])

            self.registradores[registrador] = (
                self.limitar_8bits(valor)
            )

            self.pc += 1

        # STORE: grava um valor na memoria
        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])

            self.memoria[endereco] = (
                self.registradores[registrador]
            )

            self.pc += 1

        # Operacoes da ULA
        elif operacao in ("ADD", "SUB", "AND", "OR", "XOR"):

            destino = partes[1]
            origem = partes[2]

            a = self.registradores[destino]
            b = self.registradores[origem]

            resultado = self.ula(operacao, a, b)

            self.registradores[destino] = resultado

            self.pc += 1

        # JMP: desvia para outra instrucao
        elif operacao == "JMP":
            endereco = int(partes[1])
            self.pc = endereco

        # HALT: encerra o programa
        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(
                f"Instrucao desconhecida: {operacao}"
            )

    # Ciclo: FETCH, DECODE e EXECUTE
    def ciclo(self):

        # FETCH: busca a instrucao na memoria
        instrucao = self.memoria[self.pc]

        print()
        print("-----------------------------")
        print("PC:", self.pc)
        print("Instrucao:", instrucao)

        # DECODE e EXECUTE
        self.executar_instrucao(instrucao)

        # Mostra os registradores
        self.mostrar_estado()

    # Executa o programa completo
    def executar(self):

        while not self.halted:
            self.ciclo()

    # Mostra o estado dos registradores
    def mostrar_estado(self):

        print("Registradores:")

        for nome, valor in self.registradores.items():
            print(
                f"{nome} = {valor:02X} ({valor})"
            )
