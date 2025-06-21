# 🦋 Detector de Partes de Mariposas

Una aplicación web interactiva desarrollada con **Streamlit** y **YOLOv8** que detecta y clasifica automáticamente las diferentes partes anatómicas de las mariposas en imágenes, mostrando los resultados con descripciones científicas en español.

## 🌟 Características Principales

- **🔍 Detección Automática**: Identifica 5 partes principales de las mariposas usando IA
- **🌈 Visualización Colorida**: Cada parte detectada se resalta con colores vibrantes únicos
- **🇪🇸 Interfaz en Español**: Descripciones científicas completas en español
- **📊 Métricas de Confianza**: Muestra el nivel de certeza de cada detección
- **📱 Interfaz Responsive**: Compatible con dispositivos móviles y escritorio

## 🔬 Partes Detectadas

| Parte | Color | Descripción |
|-------|-------|-------------|
| **Antena** | 🟠 Naranja | Órganos sensoriales para detectar olores y vibraciones |
| **Ala Anterior** | 🟢 Verde | Alas delanteras con patrones distintivos |
| **Ala Posterior** | 🩷 Rosa Fucsia | Alas traseras que proporcionan estabilidad |
| **Banda Postdiscal** | 🔵 Azul Cielo | Franja importante para identificación taxonómica |
| **Banda Apical** | 🟣 Violeta | Franja característica en la punta del ala |

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd app-mariposas
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Descargar el modelo entrenado
Asegúrate de tener el archivo `best.pt` (modelo YOLOv8 entrenado) en el directorio raíz del proyecto.

### 4. Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📖 Cómo Usar la Aplicación

### Paso 1: Subir Imagen
- Haz clic en **"Browse files"** o arrastra una imagen
- Formatos soportados: JPG, JPEG, PNG
- Recomendación: Imágenes claras con buena iluminación

### Paso 2: Visualizar Resultados
La aplicación mostrará:
1. **Imagen Original**: Tu imagen sin modificaciones
2. **Imagen Anotada**: Con cajas de colores y etiquetas en español
3. **Información Detallada**: Lista con descripciones científicas y métricas

### Paso 3: Interpretar Resultados
- **Cajas de colores**: Delimitan cada parte detectada
- **Etiquetas**: Nombres en español de cada parte
- **Confianza**: Porcentaje de certeza de la detección (0-100%)
- **Descripciones**: Explicaciones científicas detalladas

## 🛠️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)** - Framework para aplicaciones web
- **[YOLOv8](https://github.com/ultralytics/ultralytics)** - Modelo de detección de objetos
- **[OpenCV](https://opencv.org/)** - Procesamiento de imágenes
- **[Pillow](https://pillow.readthedocs.io/)** - Manipulación de imágenes
- **[NumPy](https://numpy.org/)** - Computación numérica

## 📁 Estructura del Proyecto

```
app-mariposas/
│
├── app.py              # Aplicación principal de Streamlit
├── best.pt             # Modelo YOLOv8 entrenado
├── requirements.txt    # Dependencias del proyecto
├── README.md          # Documentación (este archivo)
└── images/            # Carpeta para imágenes de ejemplo (opcional)
```

## 🎯 Casos de Uso

- **🔬 Investigación Científica**: Análisis automatizado de especímenes
- **📚 Educación**: Herramienta didáctica para enseñar anatomía de lepidópteros
- **🌿 Conservación**: Identificación rápida de especies
- **👨‍🎓 Estudiantes**: Apoyo en estudios de entomología

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Changelog

### v2.0.0 - Actualización Mayor
- ✨ Agregadas descripciones en español superpuestas en imagen
- 🎨 Implementado sistema de colores vibrantes
- 📊 Mejorada interfaz con métricas detalladas
- 🔧 Optimizado renderizado personalizado con OpenCV

### v1.0.0 - Versión Inicial
- 🚀 Detección básica de partes de mariposas
- 📱 Interfaz web con Streamlit

## ⚠️ Limitaciones

- El modelo funciona mejor con imágenes de alta calidad
- Requiere buena iluminación para detecciones precisas
- Optimizado para mariposas con alas extendidas
- Tiempo de procesamiento depende del tamaño de la imagen

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:
- Abre un issue en GitHub
- Contacta al equipo de desarrollo

---

**Desarrollado con ❤️ para la comunidad científica y educativa**
