
import unittest
from cpu import CPU


class TestesCPU(unittest.TestCase):

    def setUp(self):
        self.cpu = CPU()

    # Teste da instrucao LOAD
    def test_load(self):
        self.cpu.executar_instrucao("LOAD R0, 5")
        self.assertEqual(self.cpu.registradores["R0"], 5)

    # Teste da instrucao STORE
    def test_store(self):
        self.cpu.executar_instrucao("LOAD R0, 10")
        self.cpu.executar_instrucao("STORE R0, 15")
        self.assertEqual(self.cpu.memoria[15], 10)

    # Teste da soma
    def test_add(self):
        self.cpu.executar_instrucao("LOAD R0, 5")
        self.cpu.executar_instrucao("LOAD R1, 8")
        self.cpu.executar_instrucao("ADD R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 13)

    # Teste da subtracao
    def test_sub(self):
        self.cpu.executar_instrucao("LOAD R0, 10")
        self.cpu.executar_instrucao("LOAD R1, 3")
        self.cpu.executar_instrucao("SUB R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 7)

    # Teste da operacao AND
    def test_and(self):
        self.cpu.executar_instrucao("LOAD R0, 6")
        self.cpu.executar_instrucao("LOAD R1, 3")
        self.cpu.executar_instrucao("AND R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 2)

    # Teste da operacao OR
    def test_or(self):
        self.cpu.executar_instrucao("LOAD R0, 6")
        self.cpu.executar_instrucao("LOAD R1, 3")
        self.cpu.executar_instrucao("OR R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 7)

    # Teste da operacao XOR
    def test_xor(self):
        self.cpu.executar_instrucao("LOAD R0, 6")
        self.cpu.executar_instrucao("LOAD R1, 3")
        self.cpu.executar_instrucao("XOR R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 5)

    # Teste do contador de programa
    def test_pc(self):
        self.cpu.executar_instrucao("LOAD R0, 5")
        self.assertEqual(self.cpu.pc, 1)

        self.cpu.executar_instrucao("LOAD R1, 8")
        self.assertEqual(self.cpu.pc, 2)

    # Teste de salto
    def test_jmp(self):
        self.cpu.executar_instrucao("JMP 8")
        self.assertEqual(self.cpu.pc, 8)

    # Teste de parada
    def test_halt(self):
        self.cpu.executar_instrucao("HALT")
        self.assertTrue(self.cpu.halted)

    # Teste de soma acima de 255
    def test_limite_8bits_soma(self):
        self.cpu.executar_instrucao("LOAD R0, 250")
        self.cpu.executar_instrucao("LOAD R1, 10")
        self.cpu.executar_instrucao("ADD R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 4)

    # Teste de subtracao negativa em 8 bits
    def test_limite_8bits_sub(self):
        self.cpu.executar_instrucao("LOAD R0, 0")
        self.cpu.executar_instrucao("LOAD R1, 1")
        self.cpu.executar_instrucao("SUB R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 255)

    # Teste do programa do professor
    def test_programa_exemplo(self):

        programa = [
            "LOAD R0, 5",
            "LOAD R1, 8",
            "ADD R0, R1",
            "STORE R0, 15",
            "HALT"
        ]

        for i, instrucao in enumerate(programa):
            self.cpu.memoria[i] = instrucao

        self.cpu.executar()

        self.assertEqual(self.cpu.memoria[15], 13)

    # Teste do programa proprio
    def test_programa_proprio(self):

        programa = [
            "LOAD R0, 10",
            "LOAD R1, 3",
            "ADD R0, R1",
            "LOAD R2, 4",
            "SUB R0, R2",
            "XOR R0, R1",
            "STORE R0, 15",
            "HALT"
        ]

        for i, instrucao in enumerate(programa):
            self.cpu.memoria[i] = instrucao

        self.cpu.executar()

        self.assertEqual(self.cpu.memoria[15], 10)


if __name__ == "__main__":
    unittest.main()
