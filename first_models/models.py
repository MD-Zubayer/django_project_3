from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age  = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ])
    joined_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField
    num_stars = models.IntegerField()

class Person2(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
        return self.name
class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = 'GOLD', 'Gold'
        SILVER = 'SILVER', 'Silver'
        BRONZE = 'BRONZE', 'Bronze'
    name = models.CharField(max_length=40)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

class Fruit(models.Model):
    name = models.CharField('Fruit Name',max_length=100, primary_key=True)
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person2, through='Membership')

    def __str__(self):
        return self.name
    
class Membership(models.Model):
    person = models.ForeignKey(Person2, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['person', 'group'], name='unique_person_group')
        ]

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ['horn_length']
        verbose_name_plural = 'oxen'

class Person3(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the persons baby-boomer status"
        import datetime

        if self.birth_date < datetime.date(2000,1,1):
            return 'Pre-boomer'
        elif self.birth_date < datetime.date(2004,1,1):
            return 'Baby boomer'
        else:
            return "Post-boomer"
    
    @property
    def full_name(self):
        'Returns the persons full name'
        return f'{self.first_name} {self.last_name}'

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        db_table = 'student_info'


YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]

class Student2(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)

def get_currency_choices():
    return [
        ('USD', 'Us Dollar'),
        ('EUR', 'Euro'),
        ('BDT', 'Bangladeshi Taka')

    ]

class Expense(models.Model):
    currency = models.CharField(max_length=3, choices=get_currency_choices)

class Admission(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_nid_card_no = models.BigIntegerField()
    father_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=200)
    mather_name = models.CharField(max_length=100)
    father_mather_nid_no = models.BigIntegerField()
    phone_number = PhoneNumberField()
    permanent_address_village = models.CharField(max_length=250)
    permanent_address_post_office = models.CharField(max_length=250)
    permanent_address_Upazila = models.CharField(max_length=250)
    permanent_address_district = models.CharField(max_length=250)
    current_address_village = models.CharField(max_length=250)
    current_address_post_office = models.CharField(max_length=250)
    current_address_Upazila = models.CharField(max_length=250)
    current_address_district = models.CharField(max_length=250)
    guardian_name = models.CharField(max_length=100)
    guardian_phone_number = PhoneNumberField()
    guardian_address = models.CharField(max_length=250)
    Previous_class = models.CharField(max_length=250) 
    Where_read = models.CharField(max_length=250)
    current_class = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class TimeInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(TimeInfo):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class UserProfile(TimeInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
class Post1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
