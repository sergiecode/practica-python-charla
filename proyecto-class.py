from clases.conversor import Conversor


class AplicacionConversor:
    def __init__(self):
        self.conversor = None

    def ejecutar(self):
        # Pedir al usuario la medida en centímetros
        medida_cm = float(input("Ingrese la medida en centímetros: "))
        
        # Crear un objeto Conversor
        self.conversor = Conversor(medida_cm)
        
        # Realizar la conversión
        medida_pulgadas = self.conversor.convertir_a_pulgadas()
        
        # Mostrar el resultado
        print(f"La medida en pulgadas es: {medida_pulgadas}")

if __name__ == "__main__":
    app = AplicacionConversor()
    app.ejecutar()