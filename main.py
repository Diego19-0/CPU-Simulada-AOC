"""
MAIN — Demonstração do código-base
AOC 2026.2

Este programa utiliza somente LOAD, JMP e HALT,
que já estão implementados no código-base.

Depois de implementar as demais instruções, substitua
o programa de teste por um programa mais completo.
"""

from cpu import CPU


cpu = CPU()

# ==========================================
# PROGRAMA DE TESTE
# ==========================================
#


cpu.memoria[0] = "LOAD R0, 10"
cpu.memoria[1] = "LOAD R1, 3"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "LOAD R2, 4"
cpu.memoria[4] = "JMP 6"
cpu.memoria[5] = "SUB R0, R2"
cpu.memoria[6] = "XOR R0, R1"
cpu.memoria[7] = "STORE R0, 15"
cpu.memoria[8] = "HALT"


print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado()
