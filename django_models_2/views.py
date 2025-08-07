from django.shortcuts import render, HttpResponse, get_object_or_404
from django_models_2.models import Book1, Product, Author, Book2, AuthorProfile, Book3, Person, Person2, Product2, Product3, Employee, Order, Enrollment, Student, Course, Product4, Product5,Student2, Teacher, Person3, Student3, Teacher2, Teacher3, User2, AdminUser,Employee2, HighSalaryEmployee, User3, VIPUser3, Product6, Oeder2, Mymodel, Check, Event, Name,User4, User4Profile, User5, User5profile, Post, Post1, Event1, Event2, Event3
from django.db.models import Q, Avg, Max, Min, Sum, Count
from datetime import datetime
# Create your views here.

def home1(req):
    return HttpResponse('hello world')

# def create_view(req):
#     all_objects = Book1.objects.all()
#     new_object = Book1(
#         title = 'value1',
#         author = 'value2',
#         price = 44.55
#     )
    
#     return render(req, 'create_view1.html', {'objects': new_object, 'all_objects': all_objects})

def create_view2(req):
    new_data = Book1.objects.create(title='django 3', author='zubayer', price=43.55)

    return render(req, 'create_view1.html', {'new_data': new_data})



def list_view(req):
    all_objects = Book1.objects.all()

    return render(req, 'list_view1.html', {'all_objects': all_objects})
    

def detail_view(req):
    pass

def filtered_view(req):
    pass

def update_view(req):
    pass

def delete_view(req):
    pass


# def AccessForeignKey(req):
#     # book = Book2.objects.get(id=4)
#     # book = get_object_or_404(Book2, id=4)
#     book = Book2.objects.first()
#     print("📘 Book Title:",book.title)
#     print("👨‍💼 Author Name:",book.author.name)

#     author = Author.objects.get(id=2)
#     books = author.books.all()
#     print(author)
#     for b in books:
#         print("➡️ ",b)

#     return render(req, 'test.html')

def AccessOnToOnField(req):
    profile = AuthorProfile.objects.get(id=2)
    author = profile.author

    print('Profile : ',profile)
    print('Author : ',author)

    author2 = Author.objects.first()
    profile2 = author2.authorprofile.website

    print('AUTHOR 2:', author2 )
    print('PROFILE : ', profile2)

    return render(req, 'test.html')

def AccessManyToManyField(req):
    # author = Author.objects.first()
    # books = author.book3_set.all()

    # print('Author : ', author)
    # for b in books:
    #     print('Books :', b.title)

    book = Book3.objects.get(id=2)
    authors = book.authors.all()
    print('Book : ', book)
    for a in authors:
        print('All author : ', a)

    return render(req, 'test2.html')


def QuerySetView(req):
    if req.method == 'GET':
        all_book1 = Book1.objects.all()
        filtered = Book1.objects.filter(price__gt=50)
        filtered2 = Book2.objects.filter(author__name='hasan')
        filtered3 = Product.objects.filter(price__gt=100,available=True)
        filtered4 = Product.objects.filter(Q(price__lt=101) | Q(available=False))
        current_day = datetime(2025,8,7)
        filtered5 = Product.objects.filter(created_at__gte= current_day)
        filtered6 = Product.objects.filter(name__exact='Mobail')
        filtered7 = Product.objects.filter(name__iexact='mobail')
        filtered8 = Product.objects.filter(name__contains='mob')
        filtered9 = Product.objects.filter(name__icontains='Mo')
        filtered10 = Product.objects.filter(name__startswith='n')
        filtered11 = Product.objects.filter(name__endswith=2)
        filtered12 = Product.objects.filter(price__in=[100,330])
        start_time = datetime(2025,8,6)
        end_time = datetime(2025,8,8)
        filtered13 = Product.objects.filter(created_at__range=(start_time, end_time))
        filtered14 = Product.objects.filter(name__isnull=False)
        filtered15 = Product.objects.filter(name__regex=r'^m.*l$')
        filtered16 = Product.objects.filter(created_at__year=2025)
        filtered17 = Product.objects.filter(created_at__month=8)
        filtered18 = Product.objects.filter(created_at__day=7)
        filtered19 = Book2.objects.filter(author__name__contains='h')
        filtered20 = Product.objects.filter(price__gt=100).order_by('name').exclude(available=True)
        filtered21 = Product.objects.filter(Q(price__gt=100) & Q(name__startswith='m') | Q(available=False))
        filtered22 = Product.objects.filter(price__range=(1, 111)).query
        # print(filtered22)
        exclude1 = Book1.objects.exclude(price__gt=50)
        exclude2 = Book2.objects.exclude(author__name='hasan')
        exclude3 = Product.objects.exclude(price__gt=100,available=True)
        exclude4 = Product.objects.exclude(Q(price__lt=101) | Q(available=False))
        exclude5 = datetime(2025,8,7)
        exclude6 = Product.objects.exclude(created_at__gte= current_day)
        exclude7 = Product.objects.exclude(name__exact='Mobail')
        exclude8 = Product.objects.exclude(name__iexact='mobail')
        exclude9 = Product.objects.exclude(name__contains='mob')
        exclude10 = Product.objects.exclude(name__icontains='Mo')
        exclude11 = Product.objects.exclude(name__startswith='n')
        exclude12 = Product.objects.exclude(name__endswith=2)
        exclude13 = Product.objects.exclude(price__in=[100,330])
        exclude14 = datetime(2025,8,6)
        exclude15 = datetime(2025,8,8)
        exclude16 = Product.objects.exclude(created_at__range=(start_time, end_time))
        exclude17 = Product.objects.exclude(name__isnull=False)
        exclude18 = Product.objects.exclude(name__regex=r'^m.*l$')
        exclude19 = Product.objects.exclude(created_at__year=2025)
        exclude20 = Product.objects.exclude(created_at__month=8)
        exclude21 = Product.objects.exclude(created_at__day=7)
        exclude22 = Book2.objects.exclude(author__name__contains='h')
        exclude23 = Product.objects.exclude(price__gt=100).order_by('name').exclude(available=True)
        exclude24 = Product.objects.exclude(Q(price__gt=100) & Q(name__startswith='m') | Q(available=False))
        exclude25 = Product.objects.exclude(price__range=(1, 111)).query
        book = ''
        try:
            book = Book1.objects.get(id=1)
        except Book1.DoesNotExist:
            print('book does not exists')
        ordered = Product.objects.order_by('-price', '-name')
        values = Product.objects.values('name', 'price')
        values_list = Product.objects.values_list('id', 'name', 'price')
        values_list2 = Product.objects.values_list('name', flat=True)
        values_list3 = Product.objects.values_list('price', 'name').distinct()
        count1 = Product.objects.count()
        exists = Product.objects.filter(id=4).exists()
        result1 = Product.objects.aggregate(total_price=Sum('price'), avarage=Avg('price'), max=Max('price'), main=Min('price'), id=Count('id'))





    # return render(req, 'queryset.html', {'all_book1':exclude6})
    return render(req, 'queryset.html', {'all_book1':values_list3, 'count':count1, 'exists': exists, 'result1': result1})
