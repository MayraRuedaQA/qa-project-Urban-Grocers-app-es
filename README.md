# Proyecto Urban Grocers 
# Proyecto 7: Pruebas de API para Urban Grocers

## Descripción del Proyecto

Este proyecto contiene pruebas automatizadas para la API de la aplicación "Urban Grocers". Las pruebas están diseñadas para verificar la funcionalidad del endpoint de creación de kits de productos, enfocándose específicamente en la validación del campo "name" según una lista de comprobación predefinida. El objetivo es asegurar la robustez y el comportamiento esperado de la API ante diferentes tipos de datos de entrada.

---

## 📄 Fuente de Documentación

La principal fuente de documentación para entender el funcionamiento de la API y los endpoints utilizados en este proyecto es  **https://cnt-b399ec90-3da0-4c3c-ada1-3582ea7da5b2.containerhub.tripleten-services.com/docs/#api-Main.Kits-CreateKit**.


Esta documentación detalla los endpoints disponibles, los métodos HTTP, los parámetros requeridos, los cuerpos de las solicitudes y los posibles códigos de respuesta, siendo una herramienta esencial para el desarrollo de las pruebas.

---

## 🚀 Tecnologías y Técnicas Utilizadas

* **Python:** Lenguaje de programación principal sobre el que se construyó todo el proyecto.
* **pytest:** Framework utilizado para escribir y ejecutar las pruebas de manera estructurada y escalable. Permite el uso de aserciones (`assert`) para validar los resultados.
* **requests:** Biblioteca estándar de facto en Python para realizar solicitudes HTTP. Se utilizó para interactuar con la API de Urban Grocers, enviando solicitudes `POST` y analizando las respuestas.
* **Modularización:** El código se ha separado en diferentes archivos ("configuration.py", "data.py", "sender_stand_request.py") para mejorar la organización, la legibilidad y la reutilización del código, siguiendo las mejores prácticas de desarrollo de software.
* **Git y GitHub:** Se utilizó Git para el control de versiones del código local y GitHub como repositorio remoto para almacenar el proyecto y colaborar.

