from django.shortcuts import render, HttpResponse, get_object_or_404
from django_models_2.models import Book1, Book2, Author, AuthorProfile, Book3
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
