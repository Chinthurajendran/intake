# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

# views.py
from django.shortcuts import render
# from .models import Author

def author_list(request):
    # Using the raw method to execute a raw SQL query
    raw_query = "SELECT * FROM myapp_author WHERE name LIKE %s"
    authors = Author.objects.raw(raw_query, ['%John%'])

    return render(request, 'author_list.html', {'authors': authors})


# Syntax of the raw Method
# Model.objects.raw(raw_query, params=())

