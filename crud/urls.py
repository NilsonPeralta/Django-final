from django.urls import path
from .views import home,sobrenosotros,contacto,login,productos,despacho,agregar_producto,login1,modificar_producto

urlpatterns = [
    path('home/', home , name='home'),
    path('sobrenosotros/', sobrenosotros, name='sobrenosotros'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    path('productos/', productos, name='productos'),
    path('despacho/', despacho, name='despacho'),
    path('agregar-producto/', agregar_producto,name="agregar_product"),
    path('login1/', login1, name='login1'),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
]