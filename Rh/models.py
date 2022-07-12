from django.db import models

# Create your models here.


class Departamento (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    CARGOS = [
        ("CEO", "Presidente"),
        ("DIR", "Diretor"),
        ("GER", "Gerente"),
        ("COORD", "Coordenador"),
        ("SUPER", "Supervisor"),
        ("LID", "Líder"),
        ("SR", "Sênior"),
        ("PL", "Pleno"),
        ("JR", "Júnior"),
        ("TR", "Trainee")
    ]
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30, choices=CARGOS)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nasc = models.DateField(null=True)
    
    class Meta():
        ordering =["nome"]


    def __str__(self):
        return self.nome