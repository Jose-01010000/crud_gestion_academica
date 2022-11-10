from django.urls import path
from . import views

urlpatterns = [
    # Urls Clases
    path('clases/', views.clases, name='clases'),
    path('guardar_clase/', views.guardar_clase, name='guardar_clase'),
    path('edicion_clases/<int:id>', views.edicion_clase, name='edicion_clase'),
    path('editar_clase/', views.editar_clase, name='editar_clase'),
    path('eliminar_clase/<int:id>', views.eliminar_clase, name='eliminar_clase'),

    # Urls profesores
    path('profesores/', views.profesores, name='profesores'),
    path('edicion_profesor/<int:id>', views.edicion_profesores, name='edicion_profesor'),
    path('editar_profesor/', views.editar_profesor, name='editar_profesor'),

    # Urls asignaturas
    path('', views.asignaturas, name='asignaturas'),
    path('guardar_asignatura/', views.guardar_asignatura, name='guardar_asignatura'), 
    path('edicion_asignatura/<int:id>', views.edicion_asignatura, name='edicion_asignatura'),
    path('editar_asignatura/', views.editar_asignatura, name='editar_asignatura'),
    path('eliminar_asignatura/<int:id>', views.eliminar_asignatura, name='eliminar_asignatura')
]