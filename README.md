# Charla Programación en Python (práctica)

 - Crear carpeta
 - Abrir VSC, colocar el profile de Python
 - Arrastrar la carpeta
 - Crear proyecto.txt
 - Copiar la problemática del PPT

### Problemática:

La compañía estadounidense Freedom Trains está realizando un nuevo modelo de trenes basados en los planos del famoso Ingeniero francés Barnabé Brisson pero muchas piezas no han encajado correctamente debido a que los planos están en cms y las maquinarias americanas en pulgadas

---

 - Escribir el algoritmo que resolvería el problema

### Algoritmo

1 - Pedir al usuario que ingrese una medida en centímetros
2 - Leer la medida en centímetros
3 - Convertir la medida de centímetros a pulgadas usando la fórmula de conversión
4 - Mostrar el resultado en pulgadas al usuario

---

 - Escribir el pseudocódigo que resolvería el problema

```
Inicio
    Mostrar "Ingrese la medida en centímetros:"
    Leer medida_cm
    pulgadas = medida_cm / 2.54
    Mostrar "La medida en pulgadas es: " + pulgadas
Fin
```

- Escribir el diagrama de flujo que resolvería este problema

```
Inicio: Representado por un óvalo.
Mostrar mensaje "Ingrese la medida en centímetros:": Representado por un paralelogramo.
Leer medida_cm: Representado por un paralelogramo.
pulgadas = medida_cm / 2.54: Representado por un rectángulo.
Mostrar "La medida en pulgadas es: " + pulgadas : Representado por un paralelogramo.
Fin: Representado por un óvalo.
```

---

 - Finalmente realizar el código en Python:

```python
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
```

---

### ¿Cómo se podría hacer lo mismo usando Programación Orientada a Objetos?

```python
class Conversor:
    def __init__(self, centimetros):
        self.centimetros = centimetros

    def convertir_a_pulgadas(self):
        return self.centimetros / 2.54

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
```
