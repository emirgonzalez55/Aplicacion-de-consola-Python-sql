from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import asc, desc

engine = create_engine('sqlite:///participantes.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Participantes(Base):
     __tablename__ = 'participantes'   

     id = Column(Integer, primary_key=True)
     Nombre = Column(String)
     Apellido = Column(String)
     Edad = Column(String)
     Sexo = Column(String)
     Disp1 = Column(Integer)
     Disp2 = Column(Integer)
     Disp3 = Column(Integer)
     MejorDisparo = Column(Integer)
     PromDisp = Column(Integer)

     def __repr__(self):
        return "id='%s',Nombre='%s', Apellido='%s', Edad='%s', Sexo='%s', Disp1='%s', Disp2='%s', Disp3='%s', MejorDisparo='%s', PromDisp='%s'\n" % (
                             self.id, self.Nombre, self.Apellido, self.Edad, self.Sexo, self.Disp1, self.Disp2, self.Disp3, self.MejorDisparo, self.PromDisp) 

Base.metadata.create_all(engine)    

class Torneo:
    def mostrar_participantes(self):
    	self.filas = session.query(Participantes).all()
    	print(self.filas)

    def participantes(self):
            print('Ingrese un nombre')
            Nombre = input()
            print('Ingrese un apellido')
            Apellido = input()
            print('Ingrese una edad')
            Edad = input()
            print('Ingrese un género')
            Sexo = input()
            print('Ingrese el disp1')
            Disp1 = input()
            print('Ingrese un disp2')
            Disp2 = input()
            print('Ingrese un disp3')
            Disp3 = input()
            print('Ingrese un MejorDisparo')
            MejorDisparo = input()
            print('Ingrese un PromDisp')
            PromDisp = input()
            nuevo_participante = Participantes(Nombre=Nombre, Apellido=Apellido, Edad=Edad, Sexo=Sexo, Disp1=Disp1, Disp2=Disp2, Disp3=Disp3, MejorDisparo=MejorDisparo, PromDisp=PromDisp )
            session.add(nuevo_participante)
            session.commit()
            print('Participante agregado!')
                            
    def cantidad_participantes(self):
        filas = session.query(func.count(Participantes.id)).select_from(Participantes).scalar()
        print ('Cantidad de participntes:',filas)

    def promedio_disparos(self):
        filas = session.query(func.avg(Participantes.PromDisp)).scalar()
        print ("El promedio de todos los disparos es:",filas)

    def podio(self):
        filas = session.query(Participantes).order_by(desc(Participantes.PromDisp)).limit(3).all()
        print("Top 3 participantes\n",filas)

    def participntes_ordenados_por_edad(self):
        filas = session.query(Participantes).order_by(desc(Participantes.Edad)).all()
        print("Participantes ordenados por edad\n",filas)       