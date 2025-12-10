from django.db import models

# -------------------------------
# Medicine Model
# -------------------------------
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name


# -------------------------------
# Sale Model
# -------------------------------
class Sale(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField(auto_now_add=True)
    total_price = models.FloatField()

    def __str__(self):
        return f"{self.medicine.name} - {self.sale_date}"


# -------------------------------
# Employee Model  (FIXED)
# -------------------------------
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Add this line


    def __str__(self):
        return self.name