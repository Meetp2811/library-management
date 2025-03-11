from django.urls import path
from .views import (
    BookListCreateView, BookDetailView,
    AuthorListCreateView, AuthorDetailView,
    MemberListCreateView, MemberDetailView,
    LoanListCreateView, LoanDetailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import get_books

urlpatterns = [
    # 📚 Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('books/', get_books, name='book-list'),

    # ✍️ Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # 👤 Member URLs
    path('members/', MemberListCreateView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),

    # 🔄 Loan URLs
    path('loans/', LoanListCreateView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),

    # JWT Auth Routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
