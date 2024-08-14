from usuario import usuario

class listadorespuestas():
    def_init_(self,usuario:usuario,respuestas:list) -> None:
    self._usuario = usuario
    self._respuestas = respuestas

    @property
    def usuario (self)-> list[usuario]
     return self._usuario 

    @property
    def respuestas(self) ->list[respuesta]:
     return self._respuestas 
