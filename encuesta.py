from pregunta import pregunta

class encuestas():
    def _init_ (self,nombre:str,preguntas:list):
        self.nombre = nombre
        self.__preguntas =[
            pregunta(
            p ['enunciado'].
            p ['ayuda'].
            p ['alternativa'].
            p ['requerido']
            )for p in preguntas
         ]
self._listados_respuestas =[]
        
def mostrar_respuestas(self):
         print(self,respuesta)
         for p in self._preguntas:
             p.mostrar_pregunta()
  
    
def agregar_listado_respuesta(self,__listado_respuestas):
         self._listados_respuesta.append(__listados_respuestas)  

class encuestalimitadaedad(encuesta):
    def_init_(self.nombre:str.preguntas:list.edad_min:int.edad_max:int):
    super()._init_(nombre,preguntas) 
    self._edad_min = edad_min
    self._edad_max = edad_max  
      
    @property
    def edad_min(self) ->int:
           return self._edad_min

    @edad_min.setter
    def edad_min(self,edad_min) -> None:
        self._edad_min = _edad_min

    @property
    def edad_max(self) -> int:
        return self._edad_max
    
    @edad_max.setter
    def edad_max(self.edad_max) -> None:
        self._edad_max = edad_max
    
def agregar_respuesta(self,respuesta:listadorespuesta):
       self._edad_min <= self.edad_max
       super().agregar_respuesta(respuestas)

class encuestalimitadaregion(encuesta):
    def_init_(self.nombre:str.preguntas:list.regiones:list [int]):
    super()._init_(nombre,preguntas) 
    self._regiones  = regiones 
    
    @property
    def regiones(self) -> list[int]:
           return self._regiones
      
    @regiones.setter
    def regiones(self.regiones) -> None:
        self._regiones = regiones
    


       
    








    
    @property
    def 