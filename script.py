import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print ("Resolviendo el sistema de ecuaciones...")

    #Definir la matris de coeficientes A y el vector de términos independientes b
    A = np.array([[3, 1, -1], [2, 4, 1 ], [1, 2, 5]])
    b = np.array([4, 1, 1])

    # Resolver le sistema Ax = b
    try: 
        x = np.linalg.solve(A, b)
        print("La solución del sistema es:")
        for i , valor in enumerate(x, start=1):
            print(f"x{i} = {valor:.4f}")
        return x
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución única.")
        return None

def graficar_soluciones(soluciones):
    if soluciones is not None:
        print ("Graficando las soluciones...")

        # Crear un gráfico de barras para las soluciones
        etiquetas = [f"x{i}" for i in range(1, len(soluciones) + 1)]
        plt.bar(etiquetas, soluciones, color=['blue', 'orange', 'green'])
        plt.xlabel('Variables')
        plt.ylabel('Valores')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        #Guardar el gráfico como imagen
        plt.savefig('soluciones.png')
        plt.close()
        print("Gráfico guardado como 'soluciones.png'.")
    else:
        print("No se pueden graficar las soluciones debido a que no se resolvió el sistema.")

def guardar_resultado_csv (soluciones):
    if soluciones is not None:
        print ("Guardando resultados en CSV...")

        with open('resultados.csv', mode='w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Variable', 'Valor'])
            for i, valor in enumerate(soluciones, start=1):
                writer.writerow([f"x{i}", f"{valor:.4f}"])
        print("Resultados guardados en 'resultados.csv'.")
    else:
        print("No se pueden guardar los resultados debido a que no se resolvió el sistema.")

def main():
    soluciones = resolver_sistema()
    graficar_soluciones(soluciones)
    guardar_resultado_csv(soluciones)

if __name__ == "__main__":    
    main()