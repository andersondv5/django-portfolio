from django.db import models
from django.core.exceptions import ValidationError

#modelo para formulário e contato
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
    # validação do formulário
    def clean(self):
        if not self.nome:
            raise ValidationError("O nome não pode estar vazio.")
        if not self.email:
            raise ValidationError("O e-mail não pode estar vazio.")
        if len(self.mensagem) < 10:
            raise ValidationError("A mensagem deve ter pelo menos 10 caracteres.")
    
# modelo para projetos
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(default='')
    ano = models.IntegerField()
    link = models.URLField()
    
    def __str__(self):
        return self.titulo
    
    