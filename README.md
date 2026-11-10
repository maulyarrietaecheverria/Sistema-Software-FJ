# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Proyecto Software FJ

**Universidad Nacional Abierta y a Distancia (UNAD)**  
**Programa:** Ingeniería de Sistemas  
**Curso:** Programación  
**Código del curso:** 213023  
**Actividad:** Tarea 4 – Desarrollo de software orientado a objetos  

---

## 1. Descripción del proyecto

El Sistema Integral de Gestión de Clientes, Servicios y Reservas es una aplicación desarrollada en Python para la empresa ficticia Software FJ. Su propósito es facilitar el registro y la gestión de clientes, la administración de diferentes servicios y el control de las reservas realizadas.

El proyecto aplica los principios de la programación orientada a objetos y utiliza excepciones personalizadas para controlar situaciones inesperadas. Además, incorpora un sistema de registro de eventos y errores mediante archivos de texto, sin utilizar bases de datos.

## 2. Objetivo

Desarrollar una aplicación que permita gestionar clientes, servicios y reservas mediante programación orientada a objetos, aplicando conceptos como abstracción, encapsulamiento, herencia y polimorfismo, junto con mecanismos de validación y manejo de excepciones.

## 3. Funcionalidades principales

El sistema cuenta con las siguientes funcionalidades:

- Registro y validación de clientes.
- Administración de servicios disponibles.
- Reserva de salas según su capacidad y disponibilidad.
- Alquiler de equipos según las unidades disponibles.
- Gestión de servicios de asesoría especializada.
- Cálculo de costos según la duración, cantidad y descuentos.
- Confirmación, cancelación y procesamiento de reservas.
- Validación de datos y parámetros de entrada.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de log.
- Ejecución de operaciones de prueba para verificar el funcionamiento del sistema.

## 4. Tecnologías utilizadas

- **Lenguaje de programación:** Python.
- **Entorno de desarrollo:** Visual Studio Code.
- **Programación:** Orientada a objetos.
- **Registro de eventos:** Módulo `logging` de Python.
- **Control de versiones:** Git.
- **Repositorio:** GitHub.

## 5. Estructura del proyecto

La organización de los archivos y carpetas es la siguiente:

```text
Sistema_Software_FJ/
│
├── main.py
├── README.md
├── .gitignore
│
├── prueba_cliente.py
├── prueba_logs.py
├── prueba_reservas.py
├── prueba_reserva_salas.py
├── prueba_servicios.py
├── prueba_servicio_base.py
│
├── excepciones/
│   ├── __init__.py
│   └── errores_personalizados.py
│
├── logs/
│   └── sistema.log
│
├── modelos/
│   ├── __init__.py
│   ├── cliente.py
│   ├── entidad.py
│   ├── reserva.py
│   └── servicio.py
│
├── servicios/
│   ├── __init__.py
│   ├── alquiler_equipos.py
│   ├── asesoria.py
│   └── reserva_salas.py
│
└── utilidades/
    ├── __init__.py
    └── gestor_logs.py
```

## 6. Requisitos para ejecutar el proyecto

Para ejecutar la aplicación se necesita:

- Tener Python instalado.
- Contar con un editor de código, preferiblemente Visual Studio Code.
- Descargar o clonar el repositorio del proyecto.
- Abrir la carpeta principal del proyecto en el editor.

El sistema utiliza módulos propios de Python, por lo que no requiere instalar librerías externas adicionales.

## 7. Ejecución del programa

Para iniciar la aplicación, se debe abrir una terminal en la carpeta principal del proyecto y ejecutar el siguiente comando:

```bash
python main.py
```

También se puede ejecutar desde Visual Studio Code utilizando la opción de ejecutar archivo de Python.

El archivo `main.py` contiene el programa principal y realiza diferentes operaciones de prueba para comprobar el funcionamiento de los módulos del sistema.

## 8. Registro de eventos y errores

El proyecto cuenta con un sistema de registro implementado en el archivo `utilidades/gestor_logs.py`.

Los eventos, advertencias y errores se almacenan en:

```text
logs/sistema.log
```

Este archivo permite consultar las operaciones realizadas, identificar errores y conservar información sobre el comportamiento de la aplicación durante su ejecución.

## 9. Pruebas del sistema

Se desarrollaron archivos independientes para verificar el funcionamiento de las diferentes clases y componentes:

- `prueba_cliente.py`: verifica el registro y la validación de clientes.
- `prueba_logs.py`: comprueba el registro de eventos y errores.
- `prueba_reserva_salas.py`: verifica la gestión y validación de salas.
- `prueba_servicios.py`: comprueba el funcionamiento de los servicios especializados.
- `prueba_servicio_base.py`: verifica la clase base de los servicios.
- `prueba_reservas.py`: comprueba la creación, confirmación, cancelación y procesamiento de reservas.

Adicionalmente, `main.py` integra los componentes y ejecuta diferentes escenarios, incluyendo operaciones correctas y situaciones que generan excepciones.

## 10. Trabajo colaborativo

El proyecto se desarrolla como parte de las actividades colaborativas del curso de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

Se utiliza Git y GitHub como herramientas de control de versiones y almacenamiento del código fuente, facilitando el seguimiento de los cambios y la participación de los integrantes del grupo.

## 11. Autores

Mauly Arrieta Echeverria
Dina Maria Acevedo Zabaleta