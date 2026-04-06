from django.db import models


# =========================
# PARCEIROS (FOOTER)
# =========================

class Parceiro(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='parceiros/', blank=True, null=True)

    def __str__(self):
        return self.nome


# =========================
# NOTÍCIAS
# =========================

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# =========================
# CURSOS
# =========================

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)
    data = models.DateField()

    def __str__(self):
        return self.titulo


# =========================
# ESPORTES
# =========================

class Esporte(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='esportes/', blank=True, null=True)

    def __str__(self):
        return self.nome


# =========================
# CLIENTES / PATROCINADORES
# =========================

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='clientes/', blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


# =========================
# DOAÇÕES
# =========================

class Doacao(models.Model):
    nome = models.CharField(max_length=200)
    valor_sugerido = models.DecimalField(max_digits=8, decimal_places=2)
    qr_code = models.ImageField(upload_to='doacoes/', blank=True, null=True)

    def __str__(self):
        return self.nome


# =========================
# SÓCIOS
# =========================

class Socio(models.Model):

    STATUS = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo")
    )

    nome = models.CharField(max_length=200)
    numero_socio = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=100)

    foto = models.ImageField(upload_to='socios/', blank=True, null=True)

    status_pagamento = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Inativo"
    )

    investimento = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.nome


# =========================
# HISTÓRICO
# =========================

class Historico(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.socio.nome} - {self.ano}"