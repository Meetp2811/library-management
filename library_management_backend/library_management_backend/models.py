from django.db import models
from django.utils import timezone



# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("library_management_backend.Author", on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# Member Model
class Member(models.Model):
    name = models.CharField(max_length=100,default="Unknown Member")
    email = models.EmailField(default="default@email.com")  # Add this line
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


# Loan Model
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"

available_copies = models.IntegerField(default=1)
return_date = models.DateField(null=True, blank=True)  # No default needed for optional fields
