
from django.urls import path

from .views import *

urlpatterns = [
    # path('', User.as_view(), name='new_user'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', Signout.as_view(), name='logout'),
    path('signin/', Signin.as_view(), name='signin'),
]
