# Exercício TDD – FizzBuzz

## Objetivo

Implementar o jogo FizzBuzz utilizando a metodologia **Test Driven Development (TDD)**, desenvolvendo o sistema em pequenos passos (baby steps), sempre seguindo o ciclo:

1. **Red:** escrever um teste que falha;
2. **Green:** implementar apenas o código necessário para passar no teste;
3. **Refactor:** melhorar o código sem alterar seu comportamento.

---

# Baby Step 1 – Número comum

## RED

Primeiro foi criado um teste para verificar se um número que não é múltiplo de 3 nem de 5 retorna o próprio número.

```python
def test_numero_comum(self):
    self.assertEqual("1", self.fb.answer(1))
```

Como o método ainda não estava implementado, o teste falhou.

Resultado esperado:

```
FAIL
```

---

## GREEN

Foi implementado o menor código possível para fazer o teste passar.

```python
def answer(self, number):
    return "1"
```

Agora o teste passa.

Resultado:

```
OK
```

---

## REFACTOR

Nenhuma refatoração foi necessária nesse momento.

---

# Baby Step 2 – Múltiplos de 3

## RED

Foi criado um novo teste.

```python
def test_multiplo_de_tres(self):
    self.assertEqual("fizz", self.fb.answer(3))
```

O teste falhou porque o método sempre retornava "1".

---

## GREEN

Foi implementada a menor solução possível.

```python
def answer(self, number):
    if number == 3:
        return "fizz"

    return "1"
```

Os testes passaram.

---

## REFACTOR

A implementação foi generalizada para qualquer múltiplo de 3.

```python
if number % 3 == 0:
    return "fizz"
```

---

# Baby Step 3 – Múltiplos de 5

## RED

Foi criado o teste.

```python
def test_multiplo_de_cinco(self):
    self.assertEqual("buzz", self.fb.answer(5))
```

O teste falhou.

---

## GREEN

Foi implementada apenas a condição necessária.

```python
if number % 5 == 0:
    return "buzz"
```

Agora todos os testes passam.

---

## REFACTOR

Nenhuma alteração estrutural foi necessária.

---

# Baby Step 4 – Múltiplos de 3 e 5

## RED

Foi criado o teste.

```python
def test_fizzbuzz(self):
    self.assertEqual("fizzbuzz", self.fb.answer(15))
```

O teste falhou porque o método retornava apenas "fizz".

---

## GREEN

Foi adicionada uma condição antes das demais.

```python
if number % 3 == 0 and number % 5 == 0:
    return "fizzbuzz"
```

Todos os testes passaram.

---

## REFACTOR

Foi reorganizada a ordem das condições para manter o código mais legível.

---

# Baby Step 5 – Generalização

Foram adicionados novos testes para vários valores da sequência.

```python
1 -> "1"
2 -> "2"
4 -> "4"
6 -> "fizz"
10 -> "buzz"
30 -> "fizzbuzz"
45 -> "fizzbuzz"
```

Nenhuma alteração foi necessária, indicando que a implementação já atendia aos novos cenários.

---

# Baby Step 6 – Tratamento de erros

Além dos cenários válidos, foram criados testes para entradas inválidas.

## Zero

```python
with self.assertRaises(ValueError):
    self.fb.answer(0)
```

## Número negativo

```python
with self.assertRaises(ValueError):
    self.fb.answer(-5)
```

## String

```python
with self.assertRaises(TypeError):
    self.fb.answer("15")
```

## Float

```python
with self.assertRaises(TypeError):
    self.fb.answer(3.5)
```

## None

```python
with self.assertRaises(TypeError):
    self.fb.answer(None)
```

Após a criação desses testes, foi implementada a validação das entradas.

```python
if not isinstance(number, int):
    raise TypeError(...)

if number <= 0:
    raise ValueError(...)
```

Todos os testes passaram.

---

# Resultado Final

Ao final do desenvolvimento, a aplicação possui testes para:

## Caminhos felizes

* Número comum;
* Múltiplos de 3;
* Múltiplos de 5;
* Múltiplos de 3 e 5.

## Caminhos de erro

* Zero;
* Número negativo;
* String;
* Float;
* Valor None.