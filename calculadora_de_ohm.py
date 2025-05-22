#mateus yuri koike
#Gabriel Eiji N Shinkae
#joão Victor Brandão

import os

def calcular_tensao(corrente, resistencia):
    return corrente * resistencia

def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

def calcular_resistencia(tensao, corrente):
    return tensao / corrente

def menu():
    print("\n=== CALCULADORA DA LEI DE OHM ===")
    print("Escolha o que você deseja calcular:")
    print("[1] Tensão (V)")
    print("[2] Corrente (I)")
    print("[3] Resistência (R)")
    print("[0] Sair")
    

def ler_valor(nome):
    while True:
        try:
            valor = float(input(f"Digite o valor de {nome}: "))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def main():
    while True:
        menu()
        opcao = input("Opção: ")
        os.system('clear')

        if opcao == "1":
            print("\n--- Cálculo da Tensão (V) ---")
            corrente = ler_valor("Corrente (A)")
            resistencia = ler_valor("Resistência (Ω)")
            tensao = calcular_tensao(corrente, resistencia)
            print(f"Tensão calculada: {tensao:.2f} V")

        elif opcao == "2":
            print("\n--- Cálculo da Corrente (A) ---")
            tensao = ler_valor("Tensão (V)")
            resistencia = ler_valor("Resistência (Ω)")
            corrente = calcular_corrente(tensao, resistencia)
            print(f"Corrente calculada: {corrente:.2f} A")

        elif opcao == "3":
            print("\n--- Cálculo da Resistência (Ω) ---")
            tensao = ler_valor("Tensão (V)")
            corrente = ler_valor("Corrente (A)")
            resistencia = calcular_resistencia(tensao, corrente)
            print(f"Resistência calculada: {resistencia:.2f} Ω")

        elif opcao == "0":
            print("saindo!")
            break

        else:
            print("Opção inválida! Escolha 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()

