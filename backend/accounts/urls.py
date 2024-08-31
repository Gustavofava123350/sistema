from django.urls import path
from accounts.views.signin import Signin
from accounts.views.signup import Signup
from accounts.views.user import GetUser

urlpatterns = [
    path('signin/', Signin.as_view()),
    path('signup/', Signup.as_view()),
    path('user/', GetUser.as_view()),
]
