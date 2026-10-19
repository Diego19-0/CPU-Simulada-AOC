
# CPU Simulada de 8 Bits

## Universidade Federal do Ceara - UFC

Disciplina: Arquitetura de Computadores

Professor: Wendley S. Silva

Integrantes:
Davi Ribeiro Vieira- 578123
Neutino Vicenzo Tavares Sebastião- 584262

## 1. Objetivo

Implementar uma CPU simulada de 8 bits utilizando
Python, demonstrando o funcionamento dos registradores,
memoria, ULA e ciclo de execucao de instrucoes.

## 2. Arquitetura

A CPU possui:

- Dados de 8 bits
- Quatro registradores: R0, R1, R2 e R3
- Memoria com 16 posicoes
- Contador de programa (PC)
- Unidade Logica e Aritmetica (ULA)
- Ciclo Fetch, Decode e Execute

## 3. Instrucoes

LOAD: carrega um valor em um registrador.

STORE: armazena o valor de um registrador na memoria.

ADD: realiza a soma entre dois registradores.

SUB: realiza a subtracao entre dois registradores.

AND: executa AND bit a bit.

OR: executa OR bit a bit.

XOR: executa XOR bit a bit.

JMP: altera o contador de programa.

HALT: encerra a execucao.

## 4. Organizacao dos arquivos

cpu.py:
Classe principal da CPU.

ula.py:
Operacoes da Unidade Logica e Aritmetica.

main.py:
Execucao dos programas com visualizacao dos ciclos.

testes.py:
Testes automaticos das instrucoes.

README.md:
Documentacao do projeto.

## 5. Ciclo de execucao

FETCH:
Busca a instrucao na posicao indicada pelo PC.

DECODE:
Identifica a operacao e seus operandos.

EXECUTE:
Executa a instrucao e atualiza o estado da CPU.

## 6. Programas implementados

Programa 1:
Calcula 5 + 8.
Resultado: memoria[15] = 13.

Programa 2:
Executa ADD, SUB e XOR.
Resultado: memoria[15] = 10.

Programa 3:
Demonstra a instrucao JMP.
Resultado: memoria[15] = 7.

## 7. Como executar

Requisito:
Python 3 instalado.

Executar a CPU:

python main.py

Executar os testes:

python -m unittest -v testes

## 8. Testes

Foram implementados 15 testes automaticos.

Os testes verificam:

- LOAD
- STORE
- ADD
- SUB
- AND
- OR
- XOR
- PC
- JMP
- HALT
- Limites de 8 bits
- Execucao dos programas completos

## 9. Resultados esperados

Programa 1: 13
Programa 2: 10
Programa 3: 7

Todos os resultados sao armazenados
na posicao 15 da memoria.
