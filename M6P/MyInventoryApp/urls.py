# , ; Nathan Riley Sy, 244311; ,
# April , 2026 

'''
I hereby attest to the truth of the following facts:

I have not discussed the Python language code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('delete_bottle/<int:pk>/', views.delete_bottle, name='delete_bottle'),
    path('add_bottle/', views.add_bottle, name='add_bottle'),
    path('view_bottles/<int:pk>/', views.view_bottles, name='view_bottles'),
    path('view_supplier/<int:pk>/', views.view_supplier, name='view_supplier'),
]
