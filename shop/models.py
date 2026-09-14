from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, help_text="Available stock quantity")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.quantity > 0


class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.product.name} x{self.quantity}"
