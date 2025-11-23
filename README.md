# Sistema de Gestión de Investigadores

## Descripción
Sistema completo de base de datos para gestionar investigadores, publicaciones, departamentos e instituciones usando SQLAlchemy.

## Estructura del Proyecto
```
actividad_experimental/
├── models/                 # Modelos de la base de datos
│   ├── __init__.py
│   └── crear_base_entidades.py
├── database/              # Configuración de la base de datos
│   ├── __init__.py
│   └── configuracion.py
├── queries/               # Consultas y operaciones
│   ├── __init__.py
│   ├── consultas.py
│   └── consultas_ejemplo.py
├── scripts/               # Scripts de utilidad
│   ├── __init__.py
│   └── poblar_base.py
├── tests/                 # Pruebas unitarias
├── data/                  # Datos y recursos
├── docs/                  # Documentación
├── main.py               # Punto de entrada principal
└── requirements.txt      # Dependencias
```

## Características
- Modelos completos: Institucion, Departamento, Investigador, Publicacion
- Sistema de consultas con SQLAlchemy
- Población automática de datos de ejemplo
- Consultas: FILTER, ORDER BY, OR, AND, JOIN

## Uso
```bash
python main.py
```

## Tecnologías
- Python 3
- SQLAlchemy
- SQLite
