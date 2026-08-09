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
# HISTÓRIA

class Historia(models.Model):
    titulo = models.CharField(max_length=200, blank=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='historias/', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo or f"História {self.id}"


# =========================
# CURSOS
# =========================

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)
    data = models.DateField()
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=400.00,
        verbose_name="Valor (R$)"
    )

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
# DIRETORIA
# =========================

class Diretoria(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='diretoria/', blank=True, null=True)

    def __str__(self):
        return self.nome


# =========================
# EVENTOS
# =========================

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


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

    pagamento_janeiro = models.BooleanField(default=False)
    pagamento_fevereiro = models.BooleanField(default=False)
    pagamento_marco = models.BooleanField(default=False)
    pagamento_abril = models.BooleanField(default=False)
    pagamento_maio = models.BooleanField(default=False)
    pagamento_junho = models.BooleanField(default=False)
    pagamento_julho = models.BooleanField(default=False)
    pagamento_agosto = models.BooleanField(default=False)
    pagamento_setembro = models.BooleanField(default=False)
    pagamento_outubro = models.BooleanField(default=False)
    pagamento_novembro = models.BooleanField(default=False)
    pagamento_dezembro = models.BooleanField(default=False)

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

from django.utils import timezone

class Historico(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    ano = models.IntegerField()
    texto = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='historicos/', blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.socio.nome} - {self.ano}"

class IdentificacaoLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    remote_addr = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} {self.path}"
