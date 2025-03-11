from rest_framework import serializers
from .models import Book, Author, Member, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # Includes all fields of Author model

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nesting Author details inside Book

    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields of Book model

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'  # Includes all fields of Member model

class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()

    class Meta:
        model = Loan
        fields = '__all__'  # Includes all fields of Loan model
