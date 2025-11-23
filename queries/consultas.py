from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from database.configuracion import SessionLocal
from models.crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def realizar_consultas():
    db = SessionLocal()
    
    try:
        print("=== CONSULTAS CON SQLALCHEMY ===")
        # ... el resto de tu código existente
