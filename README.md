# Buggy-Cars-Rating-Automation-Tests
## Descripción General

Este proyecto automatiza funcionalidades clave de la aplicación web [Buggy Cars Rating](https://buggy.justtestit.org), enfocándose en el registro de usuarios, inicio de sesión y votación por los autos más populares. El objetivo es demostrar mis habilidades en **automatización de pruebas** usando **Selenium WebDriver** con **Python** y **pytest**, cubriendo escenarios importantes para un entorno real de QA.

## Funcionalidades Probadas

- **Registro de Usuario**: Automatización de la validación del formulario de registro.
- **Inicio de Sesión**: Pruebas del proceso de inicio de sesión con un usuario recién creado.
- **Votación por Autos**: Simulación de la votación de los modelos de autos más populares y la publicación de comentarios.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python 
- **Framework de Automatización**: Selenium WebDriver
- **Framework de Pruebas**: pytest
- **Automatización de Navegador**: Chrome WebDriver
- **Aserciones**: pytest

## Instalación y Configuración

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/DaveLedriv/buggy-cars-rating-automation.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd buggy-cars-rating-automation
    ```
3. Instala las dependencias:
    ```bash
    pip install selenium pytest
    ```
4. Descarga el [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) y asegúrate de que coincida con la versión de tu navegador.

5. Ejecuta las pruebas:
    ```bash
    pytest
    ```

## Escenarios de Prueba

### 1. Registro de Usuario
- **Objetivo**: Asegurar que los usuarios puedan registrarse correctamente validando los campos del formulario como nombre de usuario, nombre, apellido, contraseña y confirmación de contraseña.
- **Resultado Esperado**: El registro del usuario es exitoso y se muestra un mensaje de confirmación.

### 2. Inicio de Sesión
- **Objetivo**: Verificar que un usuario recién registrado pueda iniciar sesión con credenciales válidas.
- **Resultado Esperado**: El usuario inicia sesión correctamente y es redirigido al panel de control.

### 3. Votación por Autos Populares
- **Objetivo**: Automatizar el proceso de seleccionar un modelo de auto popular y dejar un comentario.
- **Resultado Esperado**: El voto del usuario se registra con éxito y se muestra un mensaje de agradecimiento.

## Mejoras Futuras
- Añadir más casos de prueba que cubran escenarios límite como la entrada inválida en los formularios.
- Integrar con herramientas de CI/CD como Jenkins para pruebas continuas.
- Ampliar la cobertura de pruebas para otras funcionalidades como categorías de autos y gestión de perfiles de usuario.

## Conclusión
Este proyecto demuestra mis habilidades para automatizar funcionalidades clave en aplicaciones web, asegurando la calidad a través de casos de prueba bien estructurados. Mi objetivo es aplicar estas habilidades en un rol profesional de QA.
