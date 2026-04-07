def classificar_triangulo(a: int, b: int, c: int) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "nao forma triangulo"

    if a + b <= c or a + c <= b or b + c <= a:
        return "nao forma triangulo"

    if a == b == c:
        return "equilátero"

    if a == b or a == c or b == c:
        return "isósceles"

    return "escaleno"


def main() -> None:
    try:
        a = int(input("Digite o primeiro lado (inteiro): "))
        b = int(input("Digite o segundo lado (inteiro): "))
        c = int(input("Digite o terceiro lado (inteiro): "))
    except ValueError:
        print("Entrada invalida: digite apenas numeros inteiros.")
        return

    resultado = classificar_triangulo(a, b, c)

    if resultado == "nao forma triangulo":
        print("As entradas nao formam um triângulo.")
    else:
        print(f"As entradas formam um triângulo {resultado}.")


if __name__ == "__main__":
    main()