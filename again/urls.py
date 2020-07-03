from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    #django admin panel
    path('admin/', admin.site.urls),

    path('', views.showRoutes),

    #Index Route
    path('users', views.getUsers),

    # #adding a user
    path('create', views.addUser),

    # #dump delete all users
    path('delete', views.deleteAll),

    # #delete user with id from db
    path('delete/<int:id>', views.delete_user),
    
    # #getting user with id from db
    path('users/<int:userId>', views.getUserByid),
    
    # #getting user with username from db
    path('users/<username>', views.getUserByUsername),

    #getting users list with username from db
]
