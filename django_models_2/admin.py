from django.contrib import admin
from django_models_2.models import Book1, Product, Author, Book2, AuthorProfile, Book3, Person, Person2, Product2, Product3, Employee, Order, Enrollment, Student, Course, Product4, Product5,Student2, Teacher, Person3, Student3, Teacher2, Teacher3, User2, AdminUser,Employee2, HighSalaryEmployee, User3, VIPUser3, Product6, Oeder2, Mymodel, Check, Event, Name,User4, User4Profile


@admin.register(Book1)
class Book1Admin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', ]
    list_filter = ['title', 'author', 'price', ]
    search_fields = ['title', 'author', 'price', 'created_at', 'updated_at']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'available', 'created_at', 'category']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Book2)
class Book2Admin(admin.ModelAdmin):
    list_display = ['id','title', 'author']

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'bio', 'website']

@admin.register(Book3)
class Book3Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_authors']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','frist_name', 'last_name']

@admin.register(Person2)
class Person2Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'full_name']

@admin.register(Product2)
class Product2Admin(admin.ModelAdmin):
    list_display = ['id','name', 'price']

@admin.register(Product3)
class Product3Admin(admin.ModelAdmin):
    list_display = ['id','name', 'caregory']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_number', 'customer_id']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product4)
class Product4Admin(admin.ModelAdmin):
    list_display = ['name', 'price','discount']

@admin.register(Product5)
class Product5Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount_percent']

@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'created_at', 'updated_at']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'created_at', 'updated_at']

@admin.register(Person3)
class Person3Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']

@admin.register(Student3)
class Student3Admin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name', 'age']

@admin.register(Teacher2)
class Teacher2Admin(admin.ModelAdmin):
    list_display = ['id','subject', 'name', 'age']


@admin.register(Teacher3)
class Teacher3Admin(admin.ModelAdmin):
    list_display = ['id', 'subject']

@admin.register(User2)
class User2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'greet']

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'greet']

@admin.register(Employee2)
class Employee2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary']

@admin.register(HighSalaryEmployee)
class HighSalaryEmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'is_high_salary']

@admin.register(User3)
class User3Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'greet', 'website']

@admin.register(VIPUser3)
class VIPUser3Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'greet']

@admin.register(Product6)
class Product6Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'brand']

@admin.register(Oeder2)
class Oeder2Admin(admin.ModelAdmin):
    list_display = ['id', 'total', 'paid', 'status']

@admin.register(Mymodel)
class MymodelAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'price', 'name', 'password', 'email', 'website', 'phone', 'slug', 'email2', 'id_address_v4', 'id_address_v6']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_time', 'end_time']

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class User4ProfileInline(admin.StackedInline):
    model = User4Profile

@admin.register(User4)
class User4Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    inlines = [User4ProfileInline]
    

    

@admin.register(User4Profile)
class User4ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'user4']
