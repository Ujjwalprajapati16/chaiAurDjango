from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('GR', 'GINGER'),
        ('ML', 'MASALA'),
        ('BL', 'BLACK'),
        ('CH', 'CHAI LATTE'),
        ('HD', 'HERBAL DECAF'),
        ('MT', 'MATCHA'),
        ('GR', 'GREEN'),
        ('WH', 'WHITE'),
        ('OL', 'OOLONG'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

# One to many
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comment = models.TextField(blank=True, max_length=500)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    
# Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVariety, related_name='stores')
    
    def __str__(self):
        return self.name
    

# One to One

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai}'
    