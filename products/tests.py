# products/tests.py

from django.test import TestCase
from django.utils import timezone
from .models import Category, Product
import decimal # Para lidar com DecimalField (preço)

class CategoryModelTest(TestCase):
    """
    Testes para o modelo Category.
    """
    def setUp(self):
        """
        Configura dados de teste que serão usados em vários testes.
        """
        self.category = Category.objects.create(
            name="Eletrônicos",
            description="Diversos produtos eletrônicos."
        )

    def test_category_creation(self):
        """
        Verifica se uma categoria é criada corretamente.
        """
        self.assertEqual(self.category.name, "Eletrônicos")
        self.assertEqual(self.category.description, "Diversos produtos eletrônicos.")
        self.assertIsNotNone(self.category.created_at)
        self.assertIsNotNone(self.category.updated_at)
        # Verifica se updated_at é maior ou igual a created_at (deve ser no momento da criação)
        self.assertGreaterEqual(self.category.updated_at, self.category.created_at)

    def test_category_str_representation(self):
        """
        Verifica a representação __str__ do modelo Category.
        """
        self.assertEqual(str(self.category), "Eletrônicos")

    def test_category_unique_name(self):
        """
        Verifica se o campo 'name' da categoria é único.
        """
        with self.assertRaises(Exception): # Espera que uma exceção seja levantada
            Category.objects.create(
                name="Eletrônicos", # Nome duplicado
                description="Outra descrição"
            )

    def test_category_update(self):
        """
        Verifica se uma categoria pode ser atualizada.
        """
        old_updated_at = self.category.updated_at
        self.category.name = "Smartphones"
        self.category.save()
        self.assertEqual(self.category.name, "Smartphones")
        self.assertGreater(self.category.updated_at, old_updated_at) # updated_at deve ser atualizado

    def test_category_blank_description(self):
        """
        Verifica se a descrição pode ser em branco/nula.
        """
        category_no_desc = Category.objects.create(name="Livros", description="")
        self.assertEqual(category_no_desc.description, "")
        # self.assertIsNone(category_no_desc.description) # TextField(blank=True, null=True) salva como None se for string vazia

class ProductModelTest(TestCase):
    """
    Testes para o modelo Product.
    """
    def setUp(self):
        """
        Configura dados de teste.
        """
        self.category = Category.objects.create(name="Informática")
        self.product = Product.objects.create(
            name="Notebook Gamer",
            description="Um notebook potente para jogos.",
            price=decimal.Decimal('7500.50'), # Use Decimal para preços
            stock=10,
            category=self.category,
            is_active=True
        )

    def test_product_creation(self):
        """
        Verifica se um produto é criado corretamente.
        """
        self.assertEqual(self.product.name, "Notebook Gamer")
        self.assertEqual(self.product.price, decimal.Decimal('7500.50'))
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category, self.category)
        self.assertTrue(self.product.is_active)
        self.assertIsNotNone(self.product.created_at)
        self.assertIsNotNone(self.product.updated_at)

    def test_product_str_representation(self):
        """
        Verifica a representação __str__ do modelo Product.
        """
        self.assertEqual(str(self.product), "Notebook Gamer")

    def test_product_default_stock(self):
        """
        Verifica o valor padrão do estoque.
        """
        product_no_stock = Product.objects.create(
            name="Teclado Mecânico",
            price=decimal.Decimal('450.00'),
            category=self.category
        )
        self.assertEqual(product_no_stock.stock, 0)

    def test_product_category_null_on_delete(self):
        """
        Verifica se a categoria do produto se torna NULL quando a categoria é deletada.
        """
        product_id = self.product.id
        category_id = self.category.id

        # Deleta a categoria
        self.category.delete()

        # Recarrega o produto do banco de dados
        # É importante recarregar, pois o objeto self.product ainda pode ter a referência antiga
        updated_product = Product.objects.get(id=product_id)
        self.assertIsNone(updated_product.category) # A categoria deve ser nula

        # Verifica se a categoria ainda existe (não deve)
        self.assertFalse(Category.objects.filter(id=category_id).exists())


    def test_product_is_active_default(self):
        """
        Verifica o valor padrão de is_active.
        """
        product_default_active = Product.objects.create(
            name="Mouse Sem Fio",
            price=decimal.Decimal('120.00'),
            category=self.category
        )
        self.assertTrue(product_default_active.is_active)

    def test_product_price_decimal_precision(self):
        """
        Verifica a precisão do campo de preço.
        """
        product_precise_price = Product.objects.create(
            name="Monitor",
            price=decimal.Decimal('1999.99'),
            category=self.category
        )
        self.assertEqual(product_precise_price.price, decimal.Decimal('1999.99'))