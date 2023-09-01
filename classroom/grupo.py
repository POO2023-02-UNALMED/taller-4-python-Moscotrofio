from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if asignaturas is None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes is None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes
        self._grupo = grupo

    def listadoAsignaturas(self, **kwargs):
            for x in list(kwargs.values()):
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        for i in lista:
            self.listadoAlumnos.append(i)

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
