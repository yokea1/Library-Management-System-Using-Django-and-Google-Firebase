from django import forms

GENRE_CHOICES = [
    ('Fiction', 'Fiction'),
    ('Non-fiction', 'Non-fiction'),
    ('Science', 'Science'),
    ('History', 'History'),
]

class BookForm(forms.Form):
    id = forms.IntegerField(label="ID")
    book_title = forms.CharField(label="Book Title", max_length=100)
    author_name = forms.CharField(label="Author Name", max_length=100)
    genre = forms.ChoiceField(label="Genre", choices=GENRE_CHOICES)
