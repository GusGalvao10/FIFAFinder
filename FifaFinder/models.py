from django.db import models

# Create your models here.


# User Model
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50, blank=True, null=True)  # Platform information
    horarios_disponibilidade = models.TextField(blank=True, null=True)  # Availability

    def __str__(self):
        return self.nome

# Championship Model
class Campeonato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    modo = models.CharField(max_length=50)  # Mode
    formato = models.CharField(max_length=50)  # Format
    qnt_max_jogadores = models.PositiveIntegerField()  # Max players
    data = models.DateField()  # Date
    horario = models.TimeField()  # Time
    organizador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="campeonatos_organizados")
    participantes = models.ManyToManyField(User, related_name="campeonatos_participados", blank=True)  # Enrolled users

    def __str__(self):
        return self.nome

# Team Model
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    capitao = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="times_como_capitao")
    qnt_jogadores = models.PositiveIntegerField()  # Number of players
    regiao = models.CharField(max_length=50)  # Region
    informacoes = models.TextField(blank=True, null=True)  # Additional information

    def __str__(self):
        return self.nome

# Player Model
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=50)  # Position
    descricao = models.TextField(blank=True, null=True)  # Description
    time = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="jogadores")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="jogador")

    def __str__(self):
        return self.nome