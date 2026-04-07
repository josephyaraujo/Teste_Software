# Casos de teste - Programa do Triângulo

## Objetivo
Definir casos de teste para o programa que recebe 3 entradas inteiras e classifica o triângulo em:
- equilátero
- isóceles
- escaleno

Também deve identificar quando as entradas não formam triângulo e quando a entrada não é inteira.

## Tecnica aplicada
Particionamento por classes de equivalência.

## Classes de equivalencia

### Classes validas
- V1: três lados inteiros positivos e iguais (equilátero)
- V2: três lados inteiros positivos, dois iguais e um diferente, respeitando desigualdade triangular (isóceles)
- V3: três lados inteiros positivos e todos diferentes, respeitando desigualdade triangular (escaleno)

### Classes invalidas
- I1: pelo menos um lado menor ou igual a zero
- I2: lados positivos, mas violam a desigualdade triangular (a + b <= c, ou equivalente)
- I3: pelo menos uma entrada não inteira (erro de conversão)

## Casos de teste representativos

| ID | Entradas (a, b, c) | Classe | Resultado esperado |
|---|---|---|---|
| CT01 | (3, 3, 3) | V1 | As entradas formam um triângulo equilatero. |
| CT02 | (5, 5, 3) | V2 | As entradas formam um triângulo isoceles. |
| CT03 | (4, 5, 6) | V3 | As entradas formam um triângulo escaleno. |
| CT04 | (0, 4, 4) | I1 | As entradas não formam um triângulo. |
| CT05 | (-1, 4, 4) | I1 | As entradas não formam um triângulo. |
| CT06 | (1, 2, 3) | I2 | As entradas não formam um triângulo. |
| CT07 | (2, 2, 4) | I2 | As entradas não formam um triângulo. |
| CT08 | ("a", 2, 3) | I3 | Entrada invalida: digite apenas números inteiros. |
| CT09 | (2.5, 2, 3) | I3 | Entrada invalida: digite apenas números inteiros. |

## Observacoes
- Os casos CT01 a CT03 cobrem as classes validas (tipos de triângulo).
- Os casos CT04 a CT07 cobrem as classes invalidas de regra de negócio.
- Os casos CT08 e CT09 cobrem a validação de tipo da entrada.
- Com particionamento por equivalência, não e necessário testar todos os valores possíveis de cada classe; um representante por classe é suficiente para a técnica.