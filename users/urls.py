from django.urls import path

from users import views
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('users_cart/', views.users_cart, name='users_cart'),

    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
 
]
