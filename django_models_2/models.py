from django.db import models
from django.db.models import Q, F, Deferrable, UniqueConstraint
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator, EmailValidator, URLValidator, RegexValidator, validate_slug, validate_email, validate_ipv4_address, validate_ipv6_address
from django.utils import timezone
# Create your models here.



# model 1  from chatGPT
class Book1(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

# model 2 from chatGPT
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES = [
        ('E', 'Electronics'),
        ('FD', 'Food'),
        ('CL', 'clothing'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='EL')

    def __str__(self):
        return self.name

# model 3 from chatGPT
# ForeignKey

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book2(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='books')

    def __str__(self):
        return self.title

# OnToOnField()
class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.RESTRICT)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField()

    def __str__(self):
        return f'profile of {self.author.name}'

# ManyToManyField
class Book3(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
# to display ManyToManyField
    def display_authors(self):
        return ', '.join([author.name for author in self.authors.all()])
    
    display_authors.short_description = 'Authors'

class Person(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f'{self.frist_name} {self.last_name}'

class Person2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return self.full_name
    get_full_name.short_description = 'Full Name'


class Product2(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    class Meta:
        db_table = 'product_2_table'
        ordering = ['price']
        verbose_name = 'Product Item'
        verbose_name_plural = 'Product Items'
        unique_together = ('name', 'price')

class Product3(models.Model):
    name = models.CharField(max_length=100)
    caregory = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'caregory'], name='unique_product_in_category')

        ]
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'Employee_table'
        verbose_name = 'Employee'
        constraints = [
            models.CheckConstraint(check=Q(age__gte=20), name='age_must_be_18_or_more')
        ]

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer_id = models.IntegerField()

    class Meta:
        db_table = 'Order_table'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['order_number']
        constraints = [
            models.UniqueConstraint(fields=['order_number'], name='unique_order_number', deferrable=Deferrable.DEFERRED)
        ]

class Student(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.name 
    

class Course(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name 
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['student', 'course'], name='unique_student_course', deferrable=Deferrable.IMMEDIATE)
            
        ]

class Product4(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount = models.FloatField(default=0.0)

    @property
    def get_discount_price(self):
        return self.price - (self.price * Decimal( self.discount) / 100)


class Product5(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_percent = models.IntegerField(default=0)

    def discount_price(self):
        discount_amount = self.price * self.discount_percent /100
        return self.price - discount_amount

    @property
    def is_discounted(self):
         if self.discount_percent > 0:
            print(f'Discount Available: {self.discount_percent}')
            return True
         else:
            print('Discount not available')
            return False
    def clean(self):
        if self.discount_percent > 50:
            raise ValidationError('Discount cannot be more than 50%.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')


# Abstract Base Class
class CommonInfo2(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student2(CommonInfo2):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

class  Teacher(CommonInfo2):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

class Person3(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Student3(Person3):
    roll = models.IntegerField()

class Teacher2(Person3):
    subject = models.CharField(max_length=100)

class Teacher3(models.Model):
    person = models.OneToOneField(Person3, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)


class User2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def greet(self):
        return  f'Hello, {self.name}'
class AdminUser(User2):
    class Meta:
        proxy = True
    @property
    def greet(self):
        return f'Welcome Admin {self.name}'

class Employee2(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class HighSalaryEmployee(Employee2):
    class Meta:
        proxy = True

    def is_high_salary(self):
        return self.salary > 100000

class User3(models.Model):
    name = models.CharField(max_length=100,editable=False, db_index=True)
    is_active = models.BooleanField(default=True)
    website = models.URLField(help_text='আপনার ব্যক্তিগত ওয়েবসাইট লিংক দিন', null=True)

    def greet(self):
        return f'Hello, {self.name}'

class VIPUser3(User3):
    class Meta:
        proxy = True
        

    def greet(self):
        return f'Welcome VIP {self.name}'

class Product6(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['category', 'brand'])
        ]

class Oeder2(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    paid = models.BooleanField(default=False)

    def make_paid(self):
        self.paid = True
        self.save(update_fields=['paid'])

    @property
    def status(self):
        return 'Paid' if self.paid else 'Unpaid'

# 🔹 ৫.১ Field Level Validation (Validator Functions)
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} is not even number')
def max_num(value):
    if value > 100000:
        raise ValidationError(f'value is can not must be 100000')

class Mymodel(models.Model):
    number = models.IntegerField(validators=[validate_even, max_num])

# ✅ Django Built-in Validators (Full List)

class Check(models.Model):
    age = models.IntegerField(blank=True,null=True, validators=[MaxValueValidator(100), MinValueValidator(1)])
    price = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2, validators=[MaxValueValidator(10)])
    name = models.CharField(blank=True,null=True,max_length=100, validators=[MaxLengthValidator(10)])
    password = models.CharField(blank=True,null=True,max_length=50, validators=[MinLengthValidator(8)])
    email = models.CharField(blank=True,null=True,max_length=100, validators=[EmailValidator()])
    website = models.CharField(blank=True,null=True,max_length=200, validators=[URLValidator()])
    phone = models.CharField(blank=True,null=True,max_length=11, validators=[RegexValidator(regex=r'^\d{11}$', message='phone number must be 11 degites.')])
    slug = models.CharField(blank=True,null=True,max_length=50, validators=[validate_slug])
    email2 = models.CharField(blank=True,null=True,max_length=100, validators=[validate_email])
    id_address_v4 = models.GenericIPAddressField(blank=True,null=True,validators=[validate_ipv4_address])
    id_address_v6 = models.GenericIPAddressField(blank=True,null=True,validators=[validate_ipv6_address])

    
# 🔹 ৫.২ Model Level Validation: clean() method
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.end_time <= self.start_time:
            raise  ValidationError('End time must be after start time')
    def clean_name(self):
        if self.name == 'nasir':
            raise ValidationError('error')
        return self.name
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    
class Name(models.Model):
    name = models.CharField(max_length=100)

    def clean_name(self):
        if self.name == 'hasan':
            raise ValidationError('error')
        return self.name

    def clean(self):
        self.clean_name()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)




class User4(models.Model):
    name = models.CharField(max_length=100, validators=[validate_slug])
    email = models.EmailField(validators=[EmailValidator()])
    def __str__(self):
        return self.name

class User4Profile(models.Model):
    user4 = models.OneToOneField(User4, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True, null=True)
    

class User5(models.Model):
    name = models.CharField(max_length=100)

class User5profile(models.Model):
    user5 = models.OneToOneField(User5, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(null=True)


# Custom Manager

class PublishedManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(is_published=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    # attach custom manager
    objects = models.Manager()
    published = PublishedManager()

class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Post1(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    # objects = models.Manager()
    is_active_manager = MyManager() # এখন সব query শুধুমাত্র active data return করবে

# Custom Queryset

class EventQuerySet(models.QuerySet):
    def upcoming(self):
        return self.filter(start_time__gte=timezone.now())
    
    def past(self):
        return self.filter(start_time__lt=timezone.now())

# Custom Manager
class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)

    def upcoming_events(self):
        return self.get_queryset().upcoming()

# add in models
class Event1(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()

    objects = EventManager()

