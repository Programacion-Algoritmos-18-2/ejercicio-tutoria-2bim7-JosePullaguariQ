class Persona:#Creamos la clase equipo
    """
    """   
    def __init__(self, n, ape, ed):#Contructor de la clase estudiante que recibe 4 atributos
        """
        """
        self.nombre = n
        self.apellido = ape
        self.edad = int(ed)

    #Metodos de agregar y obtener para los atributos de la clase
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_apellido(self, n):
        """
        """
        self.apellido = n

    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad

    #Metodo str para presentar datos
    def __str__(self):
        return "%s %s - %d"%(self.nombre, self.apellido, self.edad)