# CPU Simulada de 8 Bits

**Universidade Federal do Ceará — UFC**  
**Disciplina:** Arquitetura de Computadores (AOC) — 2026.2  
**Professor:** Wendley S. Silva  
**Integrantes:** Davi Ribeiro Vieira - 578123
Neutino Vicenzo Tavares Sebastiao - 584262

---

## 1. Descrição do projeto

Este projeto consiste na implementação de uma CPU simulada de 8 bits utilizando a linguagem Python, desenvolvido para a disciplina de Arquitetura de Computadores.

O objetivo é representar, de forma simplificada, o funcionamento de um processador, integrando registradores, memória, Unidade Lógica e Aritmética (ULA), contador de programa (PC) e um conjunto de instruções.

A execução da CPU segue o ciclo **Fetch → Decode → Execute**, permitindo visualizar as instruções executadas e acompanhar as alterações dos registradores durante o funcionamento.

## 2. Arquitetura da CPU

A CPU possui os seguintes componentes:

| Componente | Especificação |
|---|---|
| Tamanho dos dados | 8 bits |
| Registradores | R0, R1, R2 e R3 |
| Memória | 16 posições (0 a 15) |
| Contador de programa | PC |
| Unidade Lógica e Aritmética | ADD, SUB, AND, OR e XOR |
| Instruções adicionais | LOAD, STORE, JMP e HALT |
| Linguagem | Python |

### 2.1. Registradores

A CPU possui quatro registradores de uso geral: R0, R1, R2 e R3.

Cada registrador armazena um valor de 8 bits, sendo inicializado com zero.

Os registradores são utilizados para armazenar temporariamente os operandos e os resultados das operações.

### 2.2. Memória

A memória possui 16 posições, numeradas de 0 a 15.

Cada posição pode armazenar uma instrução ou um valor numérico.

No programa principal, as instruções são carregadas nas posições de 0 a 8, enquanto a posição 15 é utilizada para armazenar o resultado final.

### 2.3. Contador de programa (PC)

O PC (*Program Counter*) indica a posição da próxima instrução que será executada.

Normalmente, seu valor aumenta em uma unidade após cada instrução.

Na instrução JMP, o PC recebe diretamente o endereço informado, permitindo saltar para outra posição da memória.

## 3. Unidade Lógica e Aritmética (ULA)

O arquivo `ula.py` implementa as cinco operações aritméticas e lógicas da CPU.

| Operação | Descrição | Exemplo |
|---|---|---|
| ADD | Soma | 10 + 3 = 13 |
| SUB | Subtração | 10 - 3 = 7 |
| AND | Operação E bit a bit | 10 AND 3 = 2 |
| OR | Operação OU bit a bit | 10 OR 3 = 11 |
| XOR | OU exclusivo bit a bit | 10 XOR 3 = 9 |

A função `ula(operacao, a, b=0)` recebe o nome da operação e dois valores, executando o cálculo correspondente.

A função `limitar_8bits(valor)` utiliza a máscara hexadecimal `0xFF` para limitar os operandos e os resultados a 8 bits.

Dessa forma, os valores são representados no intervalo de 0 a 255, utilizando aritmética modular.

Por exemplo, uma soma de 250 + 10 resulta em 4 após a limitação a 8 bits.

Caso seja solicitada uma operação desconhecida, a ULA gera um erro `ValueError`.

## 4. Conjunto de instruções

A CPU implementa nove instruções:

| Instrução | Exemplo | Funcionamento |
|---|---|---|
| LOAD | LOAD R0, 10 | Coloca o valor 10 em R0 |
| STORE | STORE R0, 15 | Armazena R0 na posição 15 |
| ADD | ADD R0, R1 | Soma R0 com R1 |
| SUB | SUB R0, R1 | Subtrai R1 de R0 |
| AND | AND R0, R1 | Executa AND entre os registradores |
| OR | OR R0, R1 | Executa OR entre os registradores |
| XOR | XOR R0, R1 | Executa XOR entre os registradores |
| JMP | JMP 6 | Altera o PC para 6 |
| HALT | HALT | Encerra a execução |

Nas instruções ADD, SUB, AND, OR e XOR, o resultado é armazenado no primeiro registrador informado.

## 5. Ciclo Fetch → Decode → Execute

A CPU executa as instruções através de três etapas.

### FETCH — Busca da instrução

A CPU acessa a memória utilizando o endereço indicado pelo PC.

A instrução encontrada é armazenada temporariamente em uma variável para ser processada.

### DECODE — Decodificação

A instrução é separada em partes para identificar a operação e seus operandos.

Por exemplo, a instrução `ADD R0, R1` é interpretada como uma soma entre os registradores R0 e R1.

### EXECUTE — Execução

A CPU executa a operação identificada.

Dependendo da instrução, pode ocorrer uma alteração nos registradores, na memória ou no contador de programa.

A cada ciclo, o terminal apresenta:

- A etapa FETCH.
- O valor atual do PC.
- A instrução buscada.
- A indicação DECODE + EXECUTE.
- Os valores dos quatro registradores, em hexadecimal e decimal.

O processo continua até que a instrução HALT seja executada.

## 6. Programa principal de demonstração

O arquivo `main.py` implementa um programa composto por nove instruções armazenadas na memória.

### 6.1. Instruções do programa

```python
cpu.memoria[0] = "LOAD R0, 10"
cpu.memoria[1] = "LOAD R1, 3"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "LOAD R2, 4"
cpu.memoria[4] = "JMP 6"
cpu.memoria[5] = "SUB R0, R2"
cpu.memoria[6] = "XOR R0, R1"
cpu.memoria[7] = "STORE R0, 15"
cpu.memoria[8] = "HALT"
```

### 6.2. Execução passo a passo

| PC | Instrução | Resultado |
|---|---|---|
| 0 | LOAD R0, 10 | R0 recebe 10 |
| 1 | LOAD R1, 3 | R1 recebe 3 |
| 2 | ADD R0, R1 | R0 recebe 13 |
| 3 | LOAD R2, 4 | R2 recebe 4 |
| 4 | JMP 6 | PC passa diretamente para 6 |
| 5 | SUB R0, R2 | Não é executada |
| 6 | XOR R0, R1 | R0 recebe 14 |
| 7 | STORE R0, 15 | Memória[15] recebe 14 |
| 8 | HALT | CPU encerra a execução |

O programa começa carregando os números 10 e 3 nos registradores R0 e R1.

A instrução ADD realiza a soma, produzindo 13.

Em seguida, o registrador R2 recebe o valor 4.

A instrução JMP 6 altera o fluxo de execução, fazendo a CPU ignorar a subtração que está armazenada na posição 5.

Depois do salto, a CPU executa a operação XOR entre os valores 13 e 3, produzindo 14.

A instrução STORE armazena esse resultado na posição 15 da memória e HALT encerra o programa.

Embora existam nove instruções armazenadas, apenas oito são executadas.

### 6.3. Resultado esperado

| Componente | Valor decimal | Valor hexadecimal |
|---|---|---|
| R0 | 14 | 0E |
| R1 | 3 | 03 |
| R2 | 4 | 04 |
| R3 | 0 | 00 |

Ao final, o PC permanece em 8 e a posição 15 da memória contém o valor 14.

## 7. Organização dos arquivos

O projeto está organizado em arquivos com responsabilidades específicas.

### cpu.py

Implementa a classe principal da CPU.

É responsável por criar os registradores, a memória e o PC, identificar e executar as instruções, controlar os ciclos e mostrar o estado dos registradores.

### ula.py

Implementa as operações ADD, SUB, AND, OR e XOR.

Também possui a função responsável pela limitação dos valores a 8 bits.

### main.py

É o programa principal da simulação.

Cria uma instância da CPU, carrega as instruções na memória, inicia a execução e apresenta o estado final dos registradores.

### testes.py

Contém oito testes que verificam o funcionamento das instruções da CPU.

Os testes criam instâncias independentes da CPU, executam sequências de instruções e utilizam `assert` para comparar os resultados obtidos com os resultados esperados.

### README.md

Contém a documentação do projeto, sua arquitetura, instruções, funcionamento, execução e testes.

## 8. Testes implementados

O arquivo `testes.py` contém oito testes:

| Teste | Operação verificada | Resultado esperado |
|---|---|---|
| teste_load | LOAD R0, 25 | R0 = 25 |
| teste_jmp | JMP para a posição 4 | R0 = 10 e R1 = 20 |
| teste_halt | HALT | CPU interrompida |
| teste_add | 10 + 15 | 25 |
| teste_sub | 30 - 12 | 18 |
| teste_and | 11 AND 7 | 3 |
| teste_or | 10 OR 14 | 14 |
| teste_xor | 8 XOR 6 | 14 |

Cada teste executa um pequeno programa e verifica os valores finais utilizando instruções `assert`.

Quando o resultado corresponde ao esperado, o programa apresenta uma mensagem `[OK]`.

Caso alguma verificação falhe, o Python gera um `AssertionError`.

Quando todos os testes são aprovados, é apresentada a mensagem:

`Todos os testes-base foram aprovados.`

## 9. Tratamento de erros e controle da execução

O projeto implementa mecanismos para controlar situações incorretas durante a execução.

### 9.1. Validação de endereços do JMP

A instrução JMP verifica se o endereço informado está no intervalo de 0 a 15.

Caso esteja fora desse intervalo, será gerado um `ValueError`.

### 9.2. Limite de ciclos

O método `executar()` possui um parâmetro `max_ciclos`, com valor padrão de 100.

Se a execução atingir esse limite sem encontrar HALT, a CPU gera um `RuntimeError`.

Esse mecanismo evita que programas com loops infinitos sejam executados indefinidamente.

### 9.3. Instruções desconhecidas

Caso seja fornecida uma instrução não reconhecida, a CPU gera um `ValueError`, informando qual operação é inválida.

### 9.4. Limitação a 8 bits

Os valores carregados pela instrução LOAD e os resultados das operações da ULA são limitados a 8 bits, utilizando a função `limitar_8bits()`.

## 10. Como executar o projeto

### Requisitos

- Python 3 instalado.
- Arquivos `cpu.py`, `ula.py`, `main.py` e `testes.py` na mesma pasta.

### Executar o programa principal

Abra o terminal na pasta do projeto e digite:

```bash
python main.py
```

O terminal exibirá os ciclos da CPU, incluindo o PC, as instruções e os valores dos registradores.

### Executar os testes

Utilize o comando:

```bash
python testes.py
```

O programa executará os oito testes definidos em `testes.py`.

Se todos forem aprovados, será exibida a mensagem:

```text
[OK] LOAD
[OK] JMP
[OK] HALT
[OK] ADD
[OK] SUB
[OK] AND
[OK] OR
[OK] XOR

Todos os testes-base foram aprovados.
```

## 11. Conclusão

O projeto apresenta uma simulação didática de uma CPU de 8 bits, integrando registradores, memória, Unidade Lógica e Aritmética, contador de programa e ciclo de execução de instruções.

Foram implementadas as nove instruções propostas, permitindo executar operações matemáticas e lógicas, armazenar resultados na memória, realizar desvios e encerrar programas.

O programa principal demonstra o funcionamento das instruções LOAD, ADD, JMP, XOR, STORE e HALT, armazenando o resultado final 14 na posição 15 da memória.

Os oito testes implementados verificam o funcionamento de LOAD, JMP, HALT e das cinco operações da ULA.

Além disso, foram incluídos mecanismos de tratamento de erros, validação de endereços de salto e limitação do número máximo de ciclos.

A simulação permite compreender de maneira prática o funcionamento básico de um processador e a integração entre seus principais componentes.
