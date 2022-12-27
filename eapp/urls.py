from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login', views.login_page,name='login'),
    path('logout', views.logout_page,name='logout'),
    path('register', views.register,name='register'),
    path('products', views.products,name='products'),
    path('collections <str:name>', views.collection_view,name='collections'),
    path('collectionsdetailes <str:cname> <str:pname>', views.collection_detailes,name='collection_detailes'),




    

    

]
