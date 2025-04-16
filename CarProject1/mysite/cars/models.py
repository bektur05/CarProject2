from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField



class UserProfile(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_photo', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    STATUS_ROLE = (
        ('администратор', 'администратор'),
        ('продавец', 'продавец'),
        ('покупатель', 'покупатель')
    )
    Role = models.CharField(max_length=200, default='продавец', choices=STATUS_ROLE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, Role: {self.Role}'



class Brand(models.Model):
    brand = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f'{self.brand}'


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return f'{self.model}, {self.brand}'


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1950),
                                                   MaxValueValidator(2030)])
    TYPE_STATUS = (
        ('Бензин', 'Бензин'),
        ('Газ', 'Газ'),
        ('Электронный', 'Электронный'),
        ('Гибридный', 'Гибридный ')
    )
    type_status = MultiSelectField(max_choices=2,  choices=TYPE_STATUS)
    TRANSMISSION_CHOICES = (
        ('Авто','Авто'),
        ('Механика', 'Механика')
    )
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, max_length=200)
    price = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    Description = models.TextField()
    images = models.ImageField(upload_to='car_images')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.brand}, {self.seller}'


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('active', 'active'),
        ('completed', 'completed'),
        ('canceled', 'canceled')
    )
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)


    def __str__(self):
        return f'{self.car}, {self.status}'


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.buyer}, {self.amount}'


class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_seller')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_buyer')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                         null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)











