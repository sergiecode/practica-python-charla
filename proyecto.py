def convertir_cm_a_pulgadas(cm):
    return cm / 2.54

def main():
    while True:
        # Pedir al usuario la medida en centímetros
        medida_cm = float(input("Ingrese la medida en centímetros: "))
        
        # Convertir la medida a pulgadas
        medida_pulgadas = convertir_cm_a_pulgadas(medida_cm)
        
        # Mostrar el resultado
        print(f"La medida en pulgadas es: {medida_pulgadas}")
        
        # Preguntar si el usuario quiere continuar
        continuar = input("¿Desea continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
