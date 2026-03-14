# 🧞 Proyecto Akinator - Árboles de Decisión
Este proyecto es una implementación en **Python** de un sistema basado en **Árboles de Decisión Binarios**, diseñado para adivinar personajes mediante preguntas cerradas.

## 🎓 Contexto Académico
* **Institución:** Universidad Da Vinci de Guatemala
* **Curso:** Estructuras de Datos / Ingeniería en Sistemas
* **Desarrollador:** Brandom López

## 🧠 Lógica y Algoritmos
El núcleo del programa utiliza una estructura de datos no lineal (Árbol Binario):
* **Clase Nodo:** Cada pregunta es un nodo interno y cada personaje es un nodo hoja.
* **Recursividad:** Se utiliza para recorrer el árbol según las respuestas ("Sí" / "No") del usuario.
* **Persistencia:** El sistema carga y guarda su "memoria" desde un archivo `preguntas.csv`.

## 🛠️ Tecnologías Usadas
* **Lenguaje:** Python
* **Interfaz:** Tkinter (en desarrollo)
* **Almacenamiento:** CSV para base de conocimientos (Quizá lo reemplaze con JSON)

## 🚀 Cómo ejecutar
1. Clona este repositorio.
2. Asegúrate de tener el archivo `preguntas.csv` en la misma carpeta. (a la fecha, aun no está qui)
3. Ejecuta: `python "Árbol Decisiones.py"`
