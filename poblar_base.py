from sqlalchemy.orm import Session
from configuracion import SessionLocal, engine
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def poblar_datos():
    # Crear sesión
    db = SessionLocal()
    
    try:
        # Crear instituciones
        inst1 = Institucion(nombre="Universidad Nacional", ciudad="Bogotá", pais="Colombia")
        inst2 = Institucion(nombre="Instituto Tecnológico", ciudad="Medellín", pais="Colombia")
        
        db.add_all([inst1, inst2])
        db.commit()
        
        # Crear departamentos
        depto1 = Departamento(nombre="Ciencias de la Computación", codigo="CC01", institucion_id=inst1.id)
        depto2 = Departamento(nombre="Ingeniería de Sistemas", codigo="IS02", institucion_id=inst1.id)
        depto3 = Departamento(nombre="Matemáticas Aplicadas", codigo="MA03", institucion_id=inst2.id)
        
        db.add_all([depto1, depto2, depto3])
        db.commit()
        
        # Crear investigadores
        inv1 = Investigador(
            nombre="Ana", 
            apellido="García", 
            email="ana.garcia@email.com", 
            area_investigacion="Inteligencia Artificial",
            departamento_id=depto1.id
        )
        inv2 = Investigador(
            nombre="Carlos", 
            apellido="López", 
            email="carlos.lopez@email.com", 
            area_investigacion="Base de Datos",
            departamento_id=depto1.id
        )
        inv3 = Investigador(
            nombre="María", 
            apellido="Rodríguez", 
            email="maria.rodriguez@email.com", 
            area_investigacion="Machine Learning",
            departamento_id=depto2.id
        )
        
        db.add_all([inv1, inv2, inv3])
        db.commit()
        
        # Crear publicaciones
        pub1 = Publicacion(
            titulo="Avances en Deep Learning",
            fecha_publicacion="2024-01-15",
            doi="10.1234/deeplearning.2024",
            tipo_publicacion="Artículo",
            investigador_id=inv1.id
        )
        pub2 = Publicacion(
            titulo="Optimización de Consultas SQL",
            fecha_publicacion="2024-02-20",
            doi="10.1234/sql.optimization.2024",
            tipo_publicacion="Conferencia",
            investigador_id=inv2.id
        )
        pub3 = Publicacion(
            titulo="Tesis: Redes Neuronales Convolucionales",
            fecha_publicacion="2024-03-10",
            doi="10.1234/tesis.cnn.2024",
            tipo_publicacion="Tesis",
            investigador_id=inv1.id
        )
        
        db.add_all([pub1, pub2, pub3])
        db.commit()
        
        print("Datos poblados exitosamente!")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    poblar_datos()