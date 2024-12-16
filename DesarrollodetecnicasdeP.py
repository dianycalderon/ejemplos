# -*- coding: utf-8 -*-

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Abstracción: Método general para mostrar la información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Clase Estudiante (Herencia de Persona)
class Estudiante(Persona):

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Cambio en los atributos (Herencia)
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carrera: {self.carrera}")

    # Polimorfismo: Método de inscribirse en un curso (cada tipo de persona tiene su forma)
    def inscribirse(self, curso):
        print(f"{self.nombre} se ha inscrito en el curso: {curso.nombre}")

# Clase Profesor (Herencia de Persona)
class Profesor(Persona):

    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento

    # Cambio en los atributos (Herencia)
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    # Polimorfismo: Método para enseñar el curso (cada tipo de persona tiene su forma)
    def enseñar(self, curso):
        print(f"{self.nombre} está enseñando el curso: {curso.nombre}")

# Clase Curso
class Curso:

    def __init__(self, nombre, codigo, duracion):
        self.nombre = nombre
        self.codigo = codigo
        self.duracion = duracion
        self.estudiantes = []
        self.profesor = None

    # Método para asignar profesor al curso
    def asignar_profesor(self, profesor):
        self.profesor = profesor
        print(f"{profesor.nombre} ha sido asignado como profesor del curso {self.nombre}")

    # Método para inscribir estudiantes en el curso
    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} ha sido inscrito en el curso {self.nombre}")

    # Mostrar los detalles del curso
    def mostrar_detalles(self):
        print(f"Curso: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Duración: {self.duracion} semanas")
        if self.profesor:
            print(f"Profesor: {self.profesor.nombre}")
        if (self.estudiantes):
            print("Estudiantes inscritos:")
            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre}")
        else:
            print("No hay estudiantes inscritos aún.")

# Función para realizar un resumen de un curso
def resumen_curso(curso):
    curso.mostrar_detalles()

# Crear instancias de personas
estudiante_1 = Estudiante("Juan Pérez", 20, "Ingeniería de Sistemas")
estudiante_2 = Estudiante("Ana López", 22, "Biología")
profesor_1 = Profesor("Dr. García", 40, "Ciencias de la Computación")
profesor_2 = Profesor("Lic. Martínez", 35, "Biología")

# Crear un curso y asignar profesores y estudiantes
curso_1 = Curso("Introducción a la Programación", "CS101", 12)
curso_2 = Curso("Biología Molecular", "BIO201", 16)

# Asignar profesor a los cursos
curso_1.asignar_profesor(profesor_1)
curso_2.asignar_profesor(profesor_2)

# Inscribir estudiantes en los cursos
curso_1.inscribir_estudiante(estudiante_1)
curso_2.inscribir_estudiante(estudiante_2)

# Mostrar información de los cursos
resumen_curso(curso_1)
resumen_curso(curso_2)

# Mostrar detalles de estudiantes y profesores
print("\nInformación de estudiantes y profesores:")
estudiante_1.mostrar_informacion()
estudiante_2.mostrar_informacion()
profesor_1.mostrar_informacion()
profesor_2.mostrar_informacion()





