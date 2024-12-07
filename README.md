# Mejor CDT API

Este proyecto proporciona un servicio basado en FastAPI para calcular métricas financieras como el retorno de inversión (ROI) y las tasas vencidas para inversiones bancarias.

## Descripción del Proyecto
Un sistema de cálculo de tasas de inversión financiera basado en Python y FastAPI, enfocado en tasas de inversión y rendimientos bancarios.

## Modificaciones e Implementaciones Clave

### Servicios Implementados
1. **Servicio Calculadora**:
   - `calculate_expired_rate()`: Calcula tasas vencidas para bancos
   - `calculate_roi()`: Calcula el retorno de inversión
   - `find_rates()`: Recupera tasas anuales efectivas

2. **Procesamiento de Datos**
   - Mejora en el manejo de archivos CSV
   - Implementación de filtrado robusto para montos y plazos de inversión
   - Adición de comprobación de tipos y manejo de errores

### Pruebas
- Creación de un conjunto de pruebas completo utilizando pytest
- Adición de pruebas para:
  - Cálculo de ROI
  - Cálculo de tasas vencidas
  - Funcionalidad de búsqueda de tasas
- Implementación de resolución de rutas de archivos dinámica para compatibilidad entre máquinas

### Endpoints de la API
- `/rates`: Devuelve tasas de interés bancarias
- `/expired-rate`: Calcula tasas de periodos vencidos
- `/roi`: Calcula el retorno de inversión

## Decisiones Técnicas
- Uso de FastAPI como framework web
- Pandas para manipulación de datos
- Arquitectura modular basada en servicios
- Manejo de rutas relativas para referencias de archivos

## Dependencias
- Python 3.10
- FastAPI
- Pandas
- Pytest

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone git@github.com:SaraHdez02/mejorCDT.git
   cd mejorCDT
   ```

2. **Crear un Entorno Virtual**

   Se recomienda usar un entorno virtual para gestionar las dependencias.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de la Aplicación

1. **Iniciar el Servidor FastAPI**

   Navega al directorio raíz del proyecto y ejecuta:

   ```bash
   uvicorn app.main:app --reload
   ```

   La API estará disponible en `http://127.0.0.1:8000`.

## Ejecución de Pruebas

Para ejecutar las pruebas, utiliza `pytest`:

```bash
pytest app/tests
```

## Estructura del Proyecto
```
mejorCDT/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── gestion_datos.py
│   ├── services/
│   │   └── calculadora_service.py
│   ├── tests/
│   │   └── test_calculadora.py
│   └── utils/
│       └── file_utils.py
│
└── data/
    └── bank_rates.csv
```

## Elementos No Resueltos / Mejoras Potenciales
- Añadir un manejo de errores más completo
- Implementar registro de logs
- Crear opciones de filtrado más granulares
- Añadir autenticación para cálculos financieros

## Consideraciones de Seguridad
- Validación básica de entrada implementada
- Se recomienda añadir una autenticación más robusta
- Validar y sanitizar todos los datos de entrada

## Entorno de Desarrollo
- Ubicación: `/home/sarahdez02/Documents/Test Mejor CDT/mejorCDT/`
- Enfoque principal de desarrollo: Cálculos de tasas financieras y servicios de API

## Notas Especiales
- Énfasis en nombres en inglés
- Uso de type hinting en todo el código
- Docstrings para todas las funciones
- Diseño modular con separación de responsabilidades

## Próximos Pasos
1. Mejorar el manejo de errores
2. Añadir pruebas más completas
3. Implementar mecanismos de registro de logs
4. Considerar añadir caché para cálculos de tasas

## Notas
- Asegúrate de que el archivo `data/bank_rates.csv` esté presente en el directorio `data` para que la aplicación funcione correctamente.
- Modifica las rutas en los archivos de prueba si cambia la estructura del directorio.
