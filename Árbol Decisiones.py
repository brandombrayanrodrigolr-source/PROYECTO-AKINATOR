import csv
class Nodo:
    def __init__(self, id_nodo, contenido, tipo):
        self.id = id_nodo
        self.contenido = contenido
        self.tipo = tipo
        self.si = None
        self.no = None

def guardar_juego_en_csv(raiz, nombre_archivo):
    # Recorremos el árbol para recolectar todos los nodos (BFS o DFS)
    filas = []
    nodos_a_visitar = [raiz]
    while nodos_a_visitar:
        actual = nodos_a_visitar.pop(0)
        id_si = actual.si.id if actual.si else "-"
        id_no = actual.no.id if actual.no else "-"
        filas.append({
            'ID': actual.id,
            'Texto': actual.contenido,
            'ID_Si': id_si,
            'ID_No': id_no,
            'Tipo': actual.tipo
        })
        if actual.si: nodos_a_visitar.append(actual.si)
        if actual.no: nodos_a_visitar.append(actual.no)
    with open(nombre_archivo, mode='w', encoding='utf-8-sig', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=['ID', 'Texto', 'ID_Si', 'ID_No', 'Tipo'])
        escritor.writeheader()
        escritor.writerows(filas)

def jugar(nodo, raiz, archivo_csv):
    if nodo.tipo == 'Personaje':
        res = input(f"✨ ¿Es {nodo.contenido}? (s/n): ").lower().strip()
        if res == 's': # Si adivina personaje
            print("¡Soy un crack! Otra victoria 😎")
        else:# Sino adivina personaje
            print("Me ganaste 🏳️")
            # --- FASE DE APRENDIZAJE ---
            nuevo_pj = input("¿En qué personaje estabas pensando?: ").strip()
            pregunta = input(f"Escribe una pregunta que diferencie a {nuevo_pj} de {nodo.contenido}: ").strip()
            # Generación de ID usando timestamps
            import time
            id_nuevo_pj = str(int(time.time()))
            id_viejo_pj = str(int(time.time()) + 1)
            # Guardamos el personaje viejo en un nuevo nodo
            personaje_viejo = Nodo(id_viejo_pj, nodo.contenido, 'Personaje')
            # Guardamos el nuevo personaje
            personaje_nuevo = Nodo(id_nuevo_pj, nuevo_pj, 'Personaje')
            # El nodo actual se transforma en pregunta
            nodo.contenido = pregunta
            nodo.tipo = 'Pregunta'
            nodo.si = personaje_nuevo
            nodo.no = personaje_viejo
            print(f"✅ ¡Aprendido! Ahora soy más inteligente.")
            guardar_juego_en_csv(raiz, archivo_csv)
        return
    # --- CASO: PREGUNTA ---
    res = input(f"🤔 {nodo.contenido} (s/n): ").lower().strip()
    if res == 's':
        jugar(nodo.si, raiz, archivo_csv)
    else:
        jugar(nodo.no, raiz, archivo_csv)

def cargar_juego(archivo_csv):
    nodos = {}
    raiz = None

    try:
        with open(archivo_csv, mode='r', encoding='utf-8-sig') as f:
            lector = csv.DictReader(f)
            lector.fieldnames = [n.strip() for n in lector.fieldnames]
            filas = list(lector)

            # 1. Crear nodos con su tipo 
            for fila in filas:
                id_n = fila['ID'].strip()
                nodos[id_n] = Nodo(id_n, fila['Texto'].strip(), fila['Tipo'].strip())
                if raiz is None: raiz = nodos[id_n]

            # 2. Conectar la lógica
            for fila in filas:
                id_act = fila['ID'].strip()
                id_si = fila['ID_Si'].strip()
                id_no = fila['ID_No'].strip()

                if id_si != '-' and id_si in nodos:
                    nodos[id_act].si = nodos[id_si]
                if id_no != '-' and id_no in nodos:
                    nodos[id_act].no = nodos[id_no]
                    
        return raiz
    except Exception as e:
        print(f"💥 ¡Explotó algo!: {e}")
        return None
    
if __name__ == "__main__":
    nombre_del_archivo = 'preguntas.csv' # Guardamos el nombre en una variable
    arbol_genio = cargar_juego(nombre_del_archivo)
    
    if arbol_genio:
        print("--- 🧙‍♂️ Bienvenido al Akinator Chafa V2.0 ---")
        # Pasamos los 3 argumentos: el nodo actual, la raíz y el nombre del archivo
        jugar(arbol_genio, arbol_genio, nombre_del_archivo)
        print("\n¡Gracias por jugar, crack! ✌️")