# products/models.py

from django.db import models

class Category(models.Model):
    """
    Representa uma categoria de produto no e-commerce. (exemplo : Eletrônicos, Roupas, etc.)

    """

    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição da Categoria")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado Em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado Em")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name'] # Ordena as categorias por nome

    # MOVIDO PARA FORA DA CLASSE META, DIRETAMENTE DENTRO DA CLASSE Category
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Representa um produto individual no e-commerce.
    """

    name = models.CharField(max_length=200, verbose_name="Nome do Produto")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição do Produto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço do Produto")
    stock = models.PositiveIntegerField(default=0, verbose_name="Estoque do Produto")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoria do Produto"
    )
    is_active = models.BooleanField(default=True, verbose_name="Produto Ativo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado Em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado Em")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']


    def __str__(self):
        return self.name