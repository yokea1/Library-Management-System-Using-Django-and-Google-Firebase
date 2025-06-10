from django.shortcuts import render, redirect
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, db

# 只初始化一次 Firebase Admin
if not firebase_admin._apps:
    cred = credentials.Certificate("library-system-9735d-firebase-adminsdk-fbsvc-3e3ee532ca.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://library-system-9735d-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# 主页，显示所有书籍
def index(request):
    ref = db.reference("books")
    books = ref.get() or {}  # 确保返回的是 dict
    return render(request, "library/index.html", {"books": books})

# 添加书籍
def add_book(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        title = request.POST.get("title")
        author_name = request.POST.get("author_name")
        genre = request.POST.get("genre")

        if not book_id.isdigit():
            return HttpResponse("Error: ID must be numbers only.")

        book_data = {
            "title": title,
            "author_name": author_name,
            "genre": genre,
        }

        db.reference(f"books/{book_id}").set(book_data)
        return redirect("index")

    genres = ["Fiction", "Non-fiction", "Mystery", "Romance", "Sci-fi", "Biography"]
    return render(request, "library/add_book.html", {"genres": genres})

# 编辑书籍
def edit_book(request, book_id):
    book_ref = db.reference(f"books/{book_id}")
    if request.method == "POST":
        title = request.POST.get("title")
        author_name = request.POST.get("author_name")
        genre = request.POST.get("genre")

        book_data = {
            "title": title,
            "author_name": author_name,
            "genre": genre,
        }

        book_ref.update(book_data)
        return redirect("index")

    book = book_ref.get()
    genres = ["Fiction", "Non-fiction", "Mystery", "Romance", "Sci-fi", "Biography"]
    return render(request, "library/edit_book.html", {"book": book, "book_id": book_id, "genres": genres})

# 删除书籍
def delete_book(request, book_id):
    db.reference(f"books/{book_id}").delete()
    return redirect("index")
