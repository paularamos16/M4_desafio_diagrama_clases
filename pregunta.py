class pregunta:
    def __init__(selfcomunicado:str,ayuda:str,requerido:bool,lista_alternativa:list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.lista_alternativa =[
            alternativa(a['contenido'],[ayuda]) for a in lista_alternativa
        ]
        self.requerido = requerido


        