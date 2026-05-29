# Portal Literario - Proyecto Final Django

Plataforma web tipo Blog desarrollada con el framework **Django**. Este proyecto integra gestión de contenido profesional con funcionalidades sociales entre usuarios.

## 🚀 Arquitectura Técnica
* **Patrón MVT**: Estructura modular que separa la lógica (Views), los datos (Models) y la interfaz (Templates).
* [cite_start]**Gestión de Contenido**: Implementación de **CKEditor** para edición de texto enriquecido en artículos literarios[cite: 12].
* [cite_start]**Autenticación y Perfiles**: Sistema de registro y login con perfiles de usuario personalizados, incluyendo avatares y biografías[cite: 9, 10, 31].
* [cite_start]**Mensajería Interna**: Sistema de comunicación privada entre miembros registrados de la plataforma[cite: 13, 85].
* [cite_start]**Diseño Responsivo**: Interfaz moderna basada en CSS Flexbox y variables de estilo nativas[cite: 61, 72].

## 🛠️ Stack Tecnológico
* [cite_start]**Framework**: Django 6.0 
* [cite_start]**Base de Datos**: SQLite3 
* **Frontend**: HTML5, CSS3 Nativo
* [cite_start]**Librerías clave**: Pillow (imágenes), CKEditor (texto enriquecido) 

## ⚙️ Configuración Local
1. Clonar el repositorio.
2. [cite_start]Crear entorno virtual: `python -m venv venv` [cite: 19]
3. [cite_start]Instalar dependencias: `pip install -r requirements.txt` [cite: 20]
4. [cite_start]Realizar migraciones: `python manage.py migrate` [cite: 20]
5. Crear superusuario: `python manage.py createsuperuser`
6. [cite_start]Iniciar servidor: `python manage.py runserver` [cite: 20]