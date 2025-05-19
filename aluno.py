from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self._cpf = cpf
        self.__matricula = matricula

@abstractclassmethod

def MarcarPresenca(self):
    pass

def GerenciaMatricula(self):
    return self.__matricula

def setMatricula(self, nova_matricula):
    self.__matricula = nova_matricula

class aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf, matricula)
        self.curso = curso

def MarcarPresenca(self):
    print (f"Aluno{self.nome} Marcou Presença")

def main():
    Aluno = aluno("Pedro", "000.000.000-00", "222200022", "ADS")
    print ("Nome: ", Aluno.nome)
    print ("Curso: ", Aluno.curso)
    print ("Matricula(velha): ", Aluno.getMatricula())

    Aluno.setMatricula("180050099")

    print ("Matricula(nova", Aluno.getMatricula())

    Aluno.marcarPresenca()

if __name__ == "__main__":
    main()
