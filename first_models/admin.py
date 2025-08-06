from django.contrib import admin
from .models import Person, Musician, Album, Person2, Runner, Fruit, Group, Membership, Ox,Person3,Student,CommonInfo,Student2,Expense, Admission, Product,User, UserProfile, Post1
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']

# admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)

@admin.register(Person2)
class Person2Admin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size']
@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    list_display = ['MedalType', 'name', 'medal']

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['person', 'group', 'date_joined', 'invite_reason']

@admin.register(Ox)
class OxAdmin(admin.ModelAdmin):
    list_display = ['horn_length']

@admin.register(Person3)
class Person3Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'home_group']

@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['name', 'year']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['currency']

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'image']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

@admin.register(Post1)
class Post1Admin(admin.ModelAdmin):
    list_display = ['title', 'content']