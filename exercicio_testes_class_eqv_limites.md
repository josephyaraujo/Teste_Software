# Exercício de Testes – Particionamento em Classes de Equivalência e Análise do Valor Limite

Disciplina: Teste de Software  
Professora: Marília A. Freire  

---

## 1. Função de Desconto por Cliente e Quantidade

### 1.1 Descrição da função

A função recebe duas variáveis de entrada e produz um desconto percentual como saída:

- **Cliente**: tipo de cliente (A, B ou C).
- **Qtd**: quantidade de itens comprados (de 1 a 1000).
- **Desconto**: valor percentual de desconto aplicado à compra.

Regras de negócio:

- **Cliente A**  
  - Qtd < 10 → 0%  
  - 10 ≤ Qtd ≤ 99 → 5%  
  - Qtd ≥ 100 → 10%
- **Cliente B**  
  - Qtd < 10 → 5%  
  - 10 ≤ Qtd ≤ 99 → 15%  
  - Qtd ≥ 100 → 25%
- **Cliente C**  
  - Qtd < 10 → 0%  
  - 10 ≤ Qtd ≤ 99 → 20%  
  - Qtd ≥ 100 → 25%  

---

### 1.2 Variáveis de entrada e saída

- **Variáveis de entrada**
  - `Cliente`: categórica, domínio especificado {A, B, C}.
  - `Qtd`: numérica inteira, domínio especificado [1..1000].

- **Variável de saída**
  - `Desconto`: percentual aplicado, conforme regras do tipo de cliente e faixa de quantidade.

---

### 1.3 Classes de Equivalência

#### 1.3.1 Cliente

Assumindo que somente A, B e C são aceitos:

- **Classes válidas**
  - C1: Cliente = A
  - C2: Cliente = B
  - C3: Cliente = C

- **Classe inválida (opcional, se o sistema tratar)**
  - CI1: Cliente ∉ {A, B, C}

#### 1.3.2 Quantidade (Qtd)

Domínio informado: 1 a 1000.

- **Classes válidas (faixas funcionais)**
  - V1: 1 ≤ Qtd ≤ 9 (faixa “< 10”)
  - V2: 10 ≤ Qtd ≤ 99 (faixa “entre 10 e 99”)
  - V3: 100 ≤ Qtd ≤ 1000 (faixa “acima de 100” dentro do domínio permitido)

- **Classes inválidas (domínio)**
  - I1: Qtd < 1
  - I2: Qtd > 1000

---

### 1.4 Análise do Valor Limite

Aplicando análise de valor limite sobre as faixas e domínio de Qtd, os limites relevantes são: 1, 9, 10, 99, 100 e 1000, além de valores imediatamente fora do domínio (0 e 1001).

- Limites de domínio:
  - mínimo válido: 1
  - máximo válido: 1000
  - imediatamente abaixo do mínimo: 0
  - imediatamente acima do máximo: 1001

- Limites de faixas:
  - transição 1 ↔ 9 ↔ 10
  - transição 10 ↔ 99 ↔ 100

Clientes A, B e C compartilham as mesmas fronteiras de Qtd, mas com descontos diferentes; portanto, é importante testar essas fronteiras para cada tipo de cliente.

---

### 1.5 Conjunto de Casos de Teste

Os casos a seguir cobrem as classes de equivalência (válidas e inválidas) e os valores de fronteira, seguindo a diretriz de que cada caso inválido cobre uma única classe inválida por vez.

```md
#### Tabela 1 – Casos de teste para função Cliente/Qtd → Desconto

| ID   | Cliente | Qtd   | Classes Cobertas                          | Resultado Esperado             |
|------|---------|-------|-------------------------------------------|--------------------------------|
| CT1  | A       | 9     | C1, V1 (próximo do limite 10)            | Desconto = 0%                  |
| CT2  | A       | 10    | C1, V2 (limite inferior da faixa 5%)     | Desconto = 5%                  |
| CT3  | A       | 99    | C1, V2 (limite superior da faixa 5%)     | Desconto = 5%                  |
| CT4  | A       | 100   | C1, V3 (limite inferior da faixa 10%)    | Desconto = 10%                 |
| CT5  | A       | 1000  | C1, V3 (limite superior do domínio)      | Desconto = 10%                 |

| CT6  | B       | 1     | C2, V1 (mínimo válido da faixa <10)      | Desconto = 5%                  |
| CT7  | B       | 9     | C2, V1 (próximo do limite 10)            | Desconto = 5%                  |
| CT8  | B       | 10    | C2, V2 (limite inferior da faixa 15%)    | Desconto = 15%                 |
| CT9  | B       | 99    | C2, V2 (limite superior da faixa 15%)    | Desconto = 15%                 |
| CT10 | B       | 100   | C2, V3 (limite inferior da faixa 25%)    | Desconto = 25%                 |

| CT11 | C       | 9     | C3, V1 (próximo do limite 10)            | Desconto = 0%                  |
| CT12 | C       | 10    | C3, V2 (limite inferior da faixa 20%)    | Desconto = 20%                 |
| CT13 | C       | 99    | C3, V2 (limite superior da faixa 20%)    | Desconto = 20%                 |
| CT14 | C       | 100   | C3, V3 (limite inferior da faixa 25%)    | Desconto = 25%                 |

| CT15 | A       | 0     | C1, I1 (Qtd abaixo do mínimo permitido)  | Erro: quantidade inválida      |
| CT16 | B       | 1001  | C2, I2 (Qtd acima do máximo permitido)   | Erro: quantidade inválida      |
| CT17 | X       | 10    | CI1, V2 (Cliente inválido)               | Erro: tipo de cliente inválido |
```

---

## 2. Caso de Uso – Incluir Contato em Agenda Telefônica

### 2.1 Descrição do caso de uso

Caso de uso: **Incluir contato** em uma agenda telefônica.

Cada contato possui os dados:

- Nome
- Telefone
- Email

Regras de negócio:

1. Todo contato deve possuir um número telefônico.
2. Não pode haver dois contatos com o mesmo número telefônico.
3. Um número telefônico deve ter entre 8 e 15 dígitos numéricos.
4. Todo contato deve possuir um email em formato alfanumérico que siga a regra `*@*.*` (parte local, domínio e TLD separados).

---

### 2.2 Variáveis de entrada e saída

- **Variáveis de entrada**
  - `Nome`: texto do nome do contato.
  - `Telefone`: string de dígitos (ou campo numérico) representando o número de telefone.
  - `Email`: string representando o endereço de email.

- **Saída / Resultado**
  - Inclusão bem-sucedida do contato, ou
  - Mensagem de erro indicando a violação de alguma regra (telefone obrigatório, duplicidade, formato inválido de telefone ou email etc.).

---

### 2.3 Classes de Equivalência

#### 2.3.1 Telefone

- **Válidas**
  - T1: Telefone presente e com comprimento entre 8 e 15 dígitos numéricos.

- **Inválidas**
  - T2: Telefone ausente (null, vazio).
  - T3: Telefone com comprimento < 8.
  - T4: Telefone com comprimento > 15.
  - T5: Telefone contendo caracteres não numéricos.
  - T6: Telefone já existente na agenda (violação de unicidade).

#### 2.3.2 Email

Considerando a regra geral `*@*.*`:

- **Válidas**
  - E1: Email presente e contendo:
    - parte local alfanumérica,
    - um `@`,
    - domínio,
    - um `.`,
    - parte final (com/br/org).

- **Inválidas**
  - E2: Email ausente.
  - E3: Email sem `@`.
  - E4: Email com `@`, mas sem `.` após o `@`.
  - E5: Partes vazias ou mal formadas (por exemplo: `@dom.com`, `user@.com`, `user@dom.`, `@.`).

#### 2.3.3 Nome

Para fins de teste:

- **Válida**
  - N1: Nome não vazio (contém caracteres significativos).

- **Inválida (opcional)**
  - N2: Nome vazio ou apenas espaços, considerando que o sistema exige nome (obrigatório).

---

### 2.4 Análise do Valor Limite

Aplicando análise de valor limite principalmente sobre o tamanho do telefone:

- Comprimento do telefone:
  - mínimo válido: 8 dígitos.
  - máximo válido: 15 dígitos.
  - imediatamente abaixo do mínimo: 7 dígitos.
  - imediatamente acima do máximo: 16 dígitos.

---

### 2.5 Conjunto de Casos de Teste

Assumindo que já existe um contato previamente cadastrado:

- Contato existente na agenda:  
  - Nome: `"João"`  
  - Telefone: `"12345678"`  
  - Email: `"joao@ex.com"`

```md
#### Tabela 2 – Casos de teste para incluir contato na agenda

| ID    | Nome        | Telefone           | Email              | Classes Cobertas                    | Resultado Esperado                 |
|-------|-------------|--------------------|--------------------|-------------------------------------|------------------------------------|
| CT20  | Ana         | 12345678           | ana@ex.com         | N1, T1 (8 dígitos), E1              | Contato incluído                   |
| CT21  | Ana Silva   | 123456789012345    | ana.silva@ex.com   | N1, T1 (15 dígitos – limite sup.)   | Contato incluído                   |

| CT22  | Bia         | 1234567            | bia@ex.com         | N1, T3 (7 dígitos – < mínimo)       | Erro: telefone inválido            |
| CT23  | Caio        | 1234567890123456   | caio@ex.com        | N1, T4 (16 dígitos – > máximo)      | Erro: telefone inválido            |
| CT24  | Dani        | 1234abcd           | dani@ex.com        | N1, T5 (caracteres não numéricos)   | Erro: telefone inválido            |
| CT25  | Eva         | (ausente/null)     | eva@ex.com         | N1, T2 (telefone ausente)           | Erro: telefone obrigatório         |
| CT26  | Fábio       | 12345678           | fabio@ex.com       | N1, T6 (telefone já existente)      | Erro: telefone duplicado           |

| CT27  | Gabi        | 87654321           | gabi@ex.com        | N1, T1, E1 – outro caso válido      | Contato incluído                   |
| CT28  | Hugo        | 87654321           | (ausente/null)     | N1, T1, E2 (email ausente)          | Erro: email obrigatório            |
| CT29  | Iris        | 87654321           | iris.ex.com        | N1, T1, E3 (sem '@')                | Erro: email inválido               |
| CT30  | Júlia       | 87654321           | julia@excom        | N1, T1, E4 (sem '.' após '@')       | Erro: email inválido               |
| CT31  | Karen       | 87654321           | @ex.com            | N1, T1, E5 (parte local vazia)      | Erro: email inválido               |
| CT32  | Leo         | 87654321           | leo@.com           | N1, T1, E5 (domínio vazio)          | Erro: email inválido               |
| CT33  | Mia         | 87654321           | mia@ex.            | N1, T1, E5 (TLD vazio)              | Erro: email inválido               |

| CT34  | (vazio)     | 87654321           | vazio@ex.com       | N2, T1, E1 (se nome obrigatório)    | Erro: nome obrigatório             |
```

---

## 3. Conclusão

Foram identificadas e documentadas as classes de equivalência válidas e inválidas e, sobre essas classes, aplicou-se a análise de valor limite nos pontos críticos (faixas de quantidade e limites de tamanho de telefone). A partir disso, foi construído um conjunto de casos de teste mínimos, mas abrangentes, para verificar o comportamento correto da função de desconto e do caso de uso de inclusão de contato em agenda.