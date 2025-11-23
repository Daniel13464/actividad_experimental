from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import Base

class Institucion(Base):
    __tablename__ = 'institucion'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)
    
    # Relación uno a muchos con Departamento
    departamentos = relationship("Departamento", back_populates="institucion")

class Departamento(Base):
    __tablename__ = 'departamento'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(10), nullable=False)
    institucion_id = Column(Integer, ForeignKey('institucion.id'))
    
    # Relaciones
    institucion = relationship("Institucion", back_populates="departamentos")
    investigadores = relationship("Investigador", back_populates="departamento")

class Investigador(Base):
    __tablename__ = 'investigador'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    area_investigacion = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    
    # Relaciones
    departamento = relationship("Departamento", back_populates="investigadores")
    publicaciones = relationship("Publicacion", back_populates="investigador")

class Publicacion(Base):
    __tablename__ = 'publicacion'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(String(10), nullable=False)  # Formato 'YYYY-MM-DD'
    doi = Column(String(100), unique=True)
    tipo_publicacion = Column(String(50), nullable=False)
    investigador_id = Column(Integer, ForeignKey('investigador.id'))
    
    # Relación
    investigador = relationship("Investigador", back_populates="publicaciones")

def crear_tablas():
    from configuracion import engine
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    crear_tablas()
    print("Tablas creadas exitosamente!")