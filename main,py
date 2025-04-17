from copypaste import Copiador
import time
import keyboard
import atexit

def main():
    print("Iniciando el programa...")

    copiador = Copiador()

    # Simulamos una orden para comenzar
    print("Iniciando tarea del copiador...")

    # Esperamos un poco y luego verificamos el estado
    time.sleep(1)

    if copiador.terminado:
        print("Copiador terminó su tarea.")
        # Reiniciamos el estado
        copiador.cambiar_estado()
        print(f"Estado de la tarea: {copiador.terminado}")
    else:
        print("Copiador aún no ha terminado.")

    print(f"Estado final: {copiador.terminado}")

    keyboard.add_hotkey("shift+1", tarea_copy)
    
    def tarea_copy():
        print("Ejecutando tarea")
        copiador.copia_pegar()

    #Esperar a que se precione ESC para salir
    try:
        keyboard.wait('esc')
        # temporizador.detener()
        print("Programa finalizado.")
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario.")
    finally:
        atexit.register(keyboard.unhook_all)
        keyboard.unhook_all()


if __name__ == "__main__":
    main()
