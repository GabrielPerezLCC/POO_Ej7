from typing import Optional, List
class ViajeroFrecuente:
    __num_viajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int


    def __init__(self,num_viajero=0,dni='0',nombre='0',apellido='0',millas_acum=0):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum

    def get_nombre(self) -> str:
        return self.__nombre
    def set_nombre(self, nuevo_nombre: str):
        self.__nombre=nuevo_nombre

    def get_apellido(self) -> str:
        return self.__apellido
    def set_apellido(self, nuevo_apellido: str):
        self.__apellido=nuevo_apellido
    
    def get_num_viajero(self) ->int:
        return self.__num_viajero
    def set_num_viajero(self, numviaj: int):
        self.__num_viajero=numviaj

    def get_dni(self) -> str:
        return self.__dni
    def set_dni(self, dni: str):
        self.__dni=dni

    def get_millas_acum(self) -> str:
        return self.__millas_acum
    def set_millas_acum(self, mas_millas: str):
        self.__millas_acum=mas_millas
    
    def TotalMillas(self):
        return self.__millas_acum
    
    def AcumularMillas(self, millas:int) ->int:
        self.__millas_acum+=millas
        return self.__millas_acum
    
    def CanjearMillas(self, millas: int) ->int:
        
        if millas<=self.__millas_acum:
            self.__millas_acum-=millas
            a=self.__millas_acum
        else:
            a=-1
        return a
        #['ViajeroFrecuente']) -> Optional['ViajeroFrecuente']:
    def BuscarViajero(self, num_viajero: int, lista_viajeros: list):
        
        encontrado = next((viajeroObj for viajeroObj in lista_viajeros if viajeroObj.get_num_viajero() == num_viajero), None)
        return encontrado
    def __gt__(self,otro):
        if not isinstance(otro, ViajeroFrecuente):
            raise ValueError("No es de la clase viajero frecuente")
        return self.__millas_acum>otro.__millas_acum
    def __iadd__(self,millas:int):
        self.__millas_acum+=millas
        return self 
    def __isub__(self,millas:int):
        self.__millas_acum-=millas
        return self
    def __rsub__(self, millas):
        return ViajeroFrecuente(self.__numero, millas - self.__millas_acum)
    def __radd__(self, millas):
        return ViajeroFrecuente(self.__numero, self.__millas_acum + millas)
    def __eq__(self, other):
        return self.__millas_acum == other
    
    
    
