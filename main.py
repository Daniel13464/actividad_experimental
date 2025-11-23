#!/usr/bin/env python3
"""
Sistema de Gestión de Investigadores - Punto de entrada principal
"""
from scripts.poblar_base import poblar_datos
from queries.consultas import realizar_consultas
from database.configuracion import engine
from models.crear_base_entidades import Base

def main():
    print("=== SISTEMA DE GESTIÓN DE INVESTIGADORES ===")
    
    # Crear tablas
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    
    # Poblar datos
    print("Poblando base de datos...")
    poblar_datos()
    
    # Ejecutar consultas
    print("Ejecutando consultas de ejemplo...")
    realizar_consultas()
    
    print("=== PROCESO COMPLETADO ===")

if __name__ == "__main__":
    main()
