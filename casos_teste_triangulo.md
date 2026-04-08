# Casos de teste - Triângulo por classes de equivalência

## 1. Função analisada
Classificar três lados informados como:
- Equilátero
- Isósceles
- Escaleno
- Inválido

## 2. Variáveis de entrada
- ladoA
- ladoB
- ladoC

## 3. Condições identificadas
Para que o triângulo seja válido:
- ladoA > 0
- ladoB > 0
- ladoC > 0
- ladoA + ladoB > ladoC
- ladoA + ladoC > ladoB
- ladoB + ladoC > ladoA

Para classificação:
- ladoA = ladoB = ladoC → equilátero
- exatamente dois lados iguais → isósceles
- três lados diferentes → escaleno

## 4. Classes de equivalência

### 4.1 Validade dos lados
- CE1 válida: ladoA > 0
- CE2 inválida: ladoA <= 0
- CE3 válida: ladoB > 0
- CE4 inválida: ladoB <= 0
- CE5 válida: ladoC > 0
- CE6 inválida: ladoC <= 0

### 4.2 Desigualdade triangular
- CE7 válida: ladoA + ladoB > ladoC
- CE8 inválida: ladoA + ladoB <= ladoC
- CE9 válida: ladoA + ladoC > ladoB
- CE10 inválida: ladoA + ladoC <= ladoB
- CE11 válida: ladoB + ladoC > ladoA
- CE12 inválida: ladoB + ladoC <= ladoA

### 4.3 Classificação do triângulo
- CE13 válida: três lados iguais
- CE14 válida: exatamente dois lados iguais
- CE15 válida: três lados diferentes

## 5. Classes impossíveis ou redundantes
- Um triângulo equilátero nunca é escaleno.
- Um caso inválido não deve ser simultaneamente usado para cobrir múltiplas invalidezes, recomenda-se invalidar uma condição por vez.

## 6. Casos de teste mínimos

| ID | Entrada (A,B,C) | Classes cobertas | Resultado esperado |
|---|---|---|---|
| CT01 | (3,3,3) | CE1, CE3, CE5, CE7, CE9, CE11, CE13 | Equilátero |
| CT02 | (3,3,2) | CE1, CE3, CE5, CE7, CE9, CE11, CE14 | Isósceles |
| CT03 | (3,4,5) | CE1, CE3, CE5, CE7, CE9, CE11, CE15 | Escaleno |
| CT04 | (0,3,4) | CE2 | Inválido |
| CT05 | (3,0,4) | CE4 | Inválido |
| CT06 | (3,4,0) | CE6 | Inválido |
| CT07 | (2,3,5) | CE8 | Inválido |
| CT08 | (2,5,3) | CE10 | Inválido |
| CT09 | (5,2,3) | CE12 | Inválido |