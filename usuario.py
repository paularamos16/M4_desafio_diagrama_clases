from encuesta import encuesta, encuestalimitadaedad,encuestalimitadaedadregion
from listado_respuestas import listadorespuestas

class usuario():
    def_init_(self,correo:str, edad: int, region:int):
    self._correo = Correo
    self._edad = edad
    self._region = region


    @property
    def correo(self) -> str:
           return self._correo

    @correo.setter
    def correo(self,correo) -> None:
        self._correo = correo

    @property
    def edad(self) -> int:
        return self._edad
    
    @edad_max.setter
    def edad(self.edad) -> None:
        self._edad = edad
    @property
    def region(self) ->list[int]:
           return self._region

    @region.setter
    def region(self,region) -> None:
        self._region = region

    
        
