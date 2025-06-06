import cv2
from pyzbar.pyzbar import decode

# Lista de tipos de códigos de barra que queremos aceptar
TIPOS_CODIGOS_DE_BARRA = ["EAN13", "EAN8", "UPCA", "UPCE", "CODE128", "CODE39", "ITF", "CODABAR"]

def escanear_codigo_desde_camara():
    cap = cv2.VideoCapture(0)
    codigo_detectado = None

    print("Presioná 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Buscar códigos en la imagen
        codigos = decode(frame)

        for codigo in codigos:
            if codigo.type not in TIPOS_CODIGOS_DE_BARRA:
                continue  # ignorar códigos que no son de barra (ej: QR)

            datos = codigo.data.decode('utf-8')
            tipo = codigo.type
            print(f"Código detectado: {datos} ({tipo})")
            codigo_detectado = datos

            # Dibujar rectángulo alrededor del código
            puntos = codigo.polygon
            if len(puntos) > 4:
                puntos = puntos[:4]
            pts = [tuple(p) for p in puntos]
            for i in range(len(pts)):
                cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 2)

        cv2.imshow("Escáner de código", frame)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return codigo_detectado
