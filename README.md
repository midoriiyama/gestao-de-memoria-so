# Simulador de Gerenciamento de Memória

Trabalho destinado a disciplina de Sistemas Operacionais.
Consiste de um simulador de alocação de memória com partições variáveis, implementado em Python. Suporta quatro estratégias de alocação: First-Fit, Best-Fit, Worst-Fit e Buddy.

---

## Linguagem e versão

- **Python 3.10** ou superior (uso de type hints modernos como `list[Tipo]` exige Python 3.9+)

---

## Bibliotecas necessárias

O projeto utiliza **apenas a biblioteca padrão do Python**. Nenhuma instalação adicional é necessária.

---

## Estrutura dos arquivos

```

main.py           # Ponto de entrada; lê o arquivo de entrada e salva o log de saída
simulador.py      # Lógica principal do sistema operacional simulado
estrategias.py    # Implementações das estratégias de alocação (First-Fit, Best-Fit, Worst-Fit, Buddy)
componentes.py    # Estruturas de dados: Memória, MMU, Partição, Tabela de Partições
```

---

## Como executar

```bash
python main.py <estrategia> <arquivo_entrada>
```

### Parâmetros

| Parâmetro          | Descrição                                              | Valores aceitos                     |
|--------------------|--------------------------------------------------------|-------------------------------------|
| `<estrategia>`     | Estratégia de alocação de memória a ser utilizada      | `first`, `best`, `worst`, `buddy`   |
| `<arquivo_entrada>`| Caminho para o arquivo `.txt` com as requisições       | Ex: `entrada.txt`                  |

### Exemplos

```bash
python main.py first entrada.txt
python main.py best entrada.txt
python main.py worst entrada.txt
python main.py buddy entrada.txt
```

---

## Possíveis operações

| Operação | Argumentos          | Descrição                                      |
|----------|---------------------|------------------------------------------------|
| `aloca`  | `<pid> <tamanho>`   | Aloca `tamanho` unidades de endereçamento      |
| `libera` | `<pid>`             | Libera a partição associada ao processo        |
| `acessa` | `<pid> <endereco>`  | Traduz o endereço lógico para físico via MMU   |

### Exemplo de arquivo de entrada

```
3
P1;P2;P3
aloca P1 200
aloca P2 150
acessa P1 50
libera P1
aloca P3 100
```

---

## Saída

O simulador gera um arquivo de log com o nome:

```
log_<nome_entrada>_<estrategia>.txt
```

Por exemplo, executar `python main.py first entrada.txt` gera o arquivo `log_entrada_first.txt`.

Cada linha do log registra o resultado de uma operação:

```
alocacao <pid> <inicio> <fim>
alocacao <pid> erro!
liberacao <pid> <inicio> <fim>
acesso <pid> <endereco_logico> <endereco_fisico>
acesso <pid> <endereco_logico> violacao
```

---

## Estratégias de alocação

- **First-Fit** (`first`): escolhe a primeira área livre que satisfaça o pedido de alocação, a partir do endereço de memória menos significativo.
- **Best -it** (`best`): escolhe a menor área possível que possa receber a alocação.
- **Worst-Fit** (`worst`): escolhe sempre a maior área livre possível.
- **Buddy System** (`buddy`): realiza a alocação e liberação por pares considerando blocos de
tamanho 2^n, tal que o valor mínimo para n é 1 e o valor máximo para n é 12, totalizando blocos mínimos de 2 UA e blocos máximos de 4096 UA.



