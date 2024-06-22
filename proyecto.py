def convertir_cm_a_pulgadas(cm):
    return cm / 2.54

def main():
    # Pedir al usuario la medida en centímetros
    medida_cm = float(input("Ingrese la medida en centímetros: "))
    
    # Convertir la medida a pulgadas
    medida_pulgadas = convertir_cm_a_pulgadas(medida_cm)
    
    # Mostrar el resultado
    print(f"La medida en pulgadas es: {medida_pulgadas}")

if __name__ == "__main__":
    main()