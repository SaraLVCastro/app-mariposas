import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import numpy as np
import cv2
import os

# Cargar el modelo YOLOv8 entrenado
model = YOLO('best.pt')

# Diccionario con descripciones en español de las partes de la mariposa
descripciones_partes = {
    'antenna': 'Antena',
    'fore_wing': 'Ala anterior', 
    'fore wing': 'Ala anterior',
    'hind_wing': 'Ala posterior',
    'hind wing': 'Ala posterior',
    'postdiscal_band': 'Banda postdiscal',
    'postdiscal band': 'Banda postdiscal',
    'apical_band': 'Banda apical',
    'apical band': 'Banda apical'
}

# Descripciones detalladas para mostrar debajo
descripciones_detalladas = {
    'antenna': 'Antena - Órganos sensoriales ubicados en la cabeza que permiten a la mariposa detectar olores, vibraciones y cambios en el ambiente.',
    'fore_wing': 'Ala anterior - Las alas delanteras de la mariposa, generalmente más grandes y con patrones distintivos que ayudan en el vuelo y la identificación de especies.',
    'fore wing': 'Ala anterior - Las alas delanteras de la mariposa, generalmente más grandes y con patrones distintivos que ayudan en el vuelo y la identificación de especies.',
    'hind_wing': 'Ala posterior - Las alas traseras de la mariposa, usualmente más pequeñas que las anteriores y que proporcionan estabilidad durante el vuelo.',
    'hind wing': 'Ala posterior - Las alas traseras de la mariposa, usualmente más pequeñas que las anteriores y que proporcionan estabilidad durante el vuelo.',
    'postdiscal_band': 'Banda postdiscal - Franja de color o patrón ubicada en la región posterior del disco alar, importante para la identificación taxonómica.',
    'postdiscal band': 'Banda postdiscal - Franja de color o patrón ubicada en la región posterior del disco alar, importante para la identificación taxonómica.',
    'apical_band': 'Banda apical - Franja de color situada en la punta o ápice del ala, característica distintiva de muchas especies de mariposas.',
    'apical band': 'Banda apical - Franja de color situada en la punta o ápice del ala, característica distintiva de muchas especies de mariposas.'
}

def dibujar_anotaciones_espanol(image, results):
    """Dibuja las anotaciones con texto en español sobre la imagen"""
    # Convertir PIL a numpy array
    img_array = np.array(image)
    
    # Colores para las cajas (BGR format) - Colores más vibrantes y contrastantes
    colores = {
        'antenna': (0, 100, 255),        # Naranjo brillante
        'fore_wing': (0, 255, 0),        # Verde brillante
        'fore wing': (0, 255, 0),        # Verde brillante
        'hind_wing': (255, 0, 150),      # Rosa fucsia
        'hind wing': (255, 0, 150),      # Rosa fucsia
        'postdiscal_band': (255, 165, 0), # Azul cielo
        'postdiscal band': (255, 165, 0), # Azul cielo
        'apical_band': (128, 0, 255),     # Violeta
        'apical band': (128, 0, 255)      # Violeta
    }
    
    for r in results:
        if len(r.boxes) > 0:
            for box in r.boxes:
                # Obtener coordenadas de la caja
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Obtener clase y confianza
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                confidence = float(box.conf[0])
                
                # Obtener color para esta clase
                color = colores.get(class_name, (0, 200, 200))  # Amarillo como color por defecto
                
                # Dibujar la caja con grosor mayor para mejor visibilidad
                cv2.rectangle(img_array, (x1, y1), (x2, y2), color, 4)
                
                # Preparar el texto en español
                if class_name in descripciones_partes:
                    texto = f"{descripciones_partes[class_name]} {confidence:.2f}"
                else:
                    texto = f"{class_name} {confidence:.2f}"
                
                # Calcular el tamaño del texto
                font_scale = 0.9
                thickness = 2
                (text_width, text_height), baseline = cv2.getTextSize(texto, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
                
                # Dibujar fondo para el texto con el mismo color pero más oscuro
                color_fondo = (int(color[0]*0.7), int(color[1]*0.7), int(color[2]*0.7))
                cv2.rectangle(img_array, 
                            (x1, y1 - text_height - 15), 
                            (x1 + text_width + 15, y1), 
                            color_fondo, -1)
                
                # Dibujar el texto en español con color contrastante
                cv2.putText(img_array, texto, 
                          (x1 + 7, y1 - 7), 
                          cv2.FONT_HERSHEY_SIMPLEX, 
                          font_scale, 
                          (255, 255, 255),  # Texto blanco para contraste
                          thickness)
    
    # Convertir de vuelta a PIL Image
    return Image.fromarray(img_array)

st.set_page_config(page_title="Detector de partes de mariposas", layout="centered")

st.title("🦋 Detector de partes de mariposas")
st.write("Sube una imagen de una mariposa y detectaremos sus partes con descripciones en español directamente en la imagen.")

uploaded_file = st.file_uploader("Sube tu imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagen original", use_column_width=True)

    with st.spinner("Detectando partes..."):
        results = model.predict(image)

    # Crear imagen anotada con texto en español
    imagen_anotada = dibujar_anotaciones_espanol(image, results)
    st.image(imagen_anotada, caption="Resultado con descripciones en español", use_column_width=True)
    
    # Mostrar información detallada de cada detección
    for r in results:
        if len(r.boxes) > 0:
            st.subheader("📋 Información detallada de las partes detectadas:")
            
            for i, box in enumerate(r.boxes):
                # Obtener el nombre de la clase
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                confidence = float(box.conf[0])
                
                # Crear columnas para mejor presentación
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.metric(
                        label="Confianza",
                        value=f"{confidence:.2%}"
                    )
                
                with col2:
                    # Mostrar descripción detallada en español
                    if class_name in descripciones_detalladas:
                        st.write(f"**{descripciones_detalladas[class_name]}**")
                    else:
                        st.write(f"**{class_name}** - Parte detectada de la mariposa")
                
                st.divider()
        else:
            st.warning("No se detectaron partes de mariposa en la imagen. Intenta con una imagen más clara o con mejor iluminación.")
