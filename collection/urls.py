from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_collection, name='edit_collection'),
    path('create/', views.create_deck, name='create_deck'),
    path('<int:pk>/edit/', views.EditDeckView.as_view(), name='edit_deck'),
    path('<int:pk>/delete/', views.DeleteDeckView.as_view(), name='delete_deck'),
    path('<int:deck_id>/add_card/', views.add_card, name='add_card'),
    path('card/<int:pk>/edit/', views.EditCardView.as_view(), name='edit_card'),
    path('card/<int:pk>/delete/', views.DeleteCardView.as_view(), name='delete_card'),
]
