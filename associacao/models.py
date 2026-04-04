from django.db import models


# ======================
# NOTÍCIAS
# ======================

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# ======================
# CURSOS
# ======================

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


# ======================
# DIRETORIA
# ======================

class Diretoria(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='diretoria/', blank=True, null=True)

    def __str__(self):
        return self.nome


# ======================
# ESPORTES
# ======================

class Esporte(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='esportes/', blank=True, null=True)

    def __str__(self):
        return self.nome


# ======================
# EVENTOS
# ======================

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


# ======================
# PARCEIROS
# ======================

class Parceiro(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='parceiros/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


# ======================
# HISTÓRIA
# ======================

class Historia(models.Model):
    texto = models.TextField()
    imagem = models.ImageField(upload_to='historia/', blank=True, null=True)

    def __str__(self):
        return "História ASSGA"


# ======================
# MEMBROS
# ======================

class Membro(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome