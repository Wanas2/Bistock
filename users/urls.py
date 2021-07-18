from django.urls import path

from .views import login_page, logout_page, myprofil_page, create_user, modify_user, delete_user, UserListView

urlpatterns = [
    # Auth urls
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),

    # users urls
    path('create_user/', create_user, name='create_user'),
    path('modify_user/<user_id>', modify_user, name='modify_user'),
    path('delete_user/<user_id>', delete_user, name='delete_user'),
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('myprofil/', myprofil_page, name='myprofil'),
]
