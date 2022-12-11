from django.urls import path

from . import views

urlpatterns = [
    

    path('',views.mostrar_index, name='index'),
    path('login_index', views.login_index, name='logIndex'),
    
    path('mostrar_contact/', views.mostrar_contact, name='Contacto'),
    path('buscar_post/', views.buscar_post, name='buscar'),
    path('crear_post/', views.crear_post, name='crear'),
    path('cursoPost/', views.cursoPost, name='CursoPost'),
    path('buscador/', views.buscador, name='buscar'),
    path('mostrarPost/', views.PosteoList.as_view(), name='mostrarpost'),
    path('PosteoDetail/<pk>', views.PosteoDetail.as_view(), name='Detail'),
    path('base/', views.base, name='base'),
    path('post_confirm_delete/<pk>', views.PosteoDeleteView.as_view(), name='Eliminar'),
    path('modificar_post/<pk>', views.PosteoUpdateView.as_view(), name='Actualizar'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('Login/', views.AdminLoginView.as_view(), name='Login'),
    path('Logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar usuario'),
    path('about/', views.about, name='About'),
    path('cuenta/', views.accountSettings, name='Cuenta'),

]