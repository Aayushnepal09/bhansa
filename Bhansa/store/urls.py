from django.conf import settings
from django.urls import path
from store import views
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login ,name='login'),
    path('register',views.register ,name='register'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('kitchen',views.kitchen,name='kitchen'),
    path('adminn',views.admin,name='adminn'),
    path('product',views.product,name='product'),
    path('catering',views.catering,name='customer'),
    path('customersdetail',views.customersdetail),
    path('orders',views.orders),
    path('messagess',views.messagess),
    path('logout',LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name="logout")

]