"""
Consultas SQLAlchemy demostradas en la actividad
"""
from sqlalchemy import select, and_, or_
from models.investigador import Investigador
from models.publicacion import Publicacion
from models.departamento import Departamento

def ejecutar_consultas_ejemplo(db):
    """
    Ejecuta las consultas mostradas en el log
    """
    print("2. FILTER - Investigadores de IA:")
    # Tu consulta FILTER aquí

    print("3. ORDER_BY - Publicaciones ordenadas por fecha:")
    # Tu consulta ORDER_BY aquí

    print("4. OR_ - Investigadores de IA o Machine Learning:")
    # Tu consulta OR aquí

    print("5. AND_ - Publicaciones de tipo Artículo en 2024:")
    # Tu consulta AND aquí

    print("6. JOIN - Investigadores con sus departamentos:")
    # Tu consulta JOIN aquí
