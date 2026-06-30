# Simulador de Gerenciamento de Memória

Simulador de alocação de memória com partições variáveis, implementado em Python. Suporta quatro estratégias de alocação: First Fit, Best Fit, Worst Fit e Buddy System.

---

## Linguagem e versão

- **Python 3.10** ou superior (uso de type hints modernos como `list[Tipo]` exige Python 3.9+)

---

## Bibliotecas necessárias

O projeto utiliza **apenas a biblioteca padrão do Python**. Nenhuma instalação adicional é necessária.

---

## Estrutura dos arquivos

```
.
├── main.py           # Ponto de entrada; lê o arquivo de entrada e salva o log de saída
├── simulador.py      # Lógica principal do sistema operacional simulado
├── estrategias.py    # Implementações das estratégias de alocação (First, Best, Worst, Buddy)
└── componentes.py    # Estruturas de dados: Memória, MMU, Partição, Tabela de Partições
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
| `<arquivo_entrada>`| Caminho para o arquivo `.txt` com as requisições       | Ex.: `entrada.txt`                  |

### Exemplos

```bash
python main.py first entrada.txt
python main.py best entrada.txt
python main.py worst entrada.txt
python main.py buddy entrada.txt
```

---

## Formato do arquivo de entrada

```
<número de processos>
<pid1>;<pid2>;...;<pidN>
<operacao> <pid> [tamanho]
...
```

As operações disponíveis são:

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

O simulador gera automaticamente um arquivo de log com o nome:

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

- **First Fit** (`first`): aloca no primeiro espaço livre suficiente, a partir do endereço menos significativo.
- **Best Fit** (`best`): aloca na menor área livre que comporta o processo, minimizando desperdício.
- **Worst Fit** (`worst`): aloca na maior área livre disponível.
- **Buddy System** (`buddy`): aloca blocos de tamanho potência de 2 (mínimo 2 UA, máximo 4096 UA), com fusão automática de blocos adjacentes na liberação.

---

## Observações

- O tamanho total da memória simulada é de **4096 unidades de endereçamento (UA)**.
- Se não houver espaço suficiente para uma alocação, a simulação registra o erro e é encerrada.
- A tradução de endereços pela MMU usa o modelo de **partições contíguas com registrador base e limite**.
