from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# Importar servicos consumir API
from .services import get_profesores
# Importar modelos
from .models import Profesor, Asignatura, Clase

# Consumir API profesores
def obtener_profesores():
    if not Profesor.objects.all():
        for profesor in get_profesores():
            profesor_modelo = Profesor(
                nombre=profesor['Nomb_Prof'], correo=profesor['Corr_Prof'], telefono=profesor['Tele_Prof'])
            profesor_modelo.save()
        return True

# Crud clases
def clases(request):
    clases = Clase.objects.all()
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()

    data = {'clase': clases, 'asignaturas': asignaturas,
            'profesores': profesores}
    return render(request, 'clases/listar_clases.html', data)


def guardar_clase(request):
    clase_salon = request.POST['clase_salon']
    clase_horario = request.POST['clase_horario']
    profesor = request.POST['profesor']
    asignatura = request.POST['asignatura']

    Clase.objects.create(salon=clase_salon, horario=clase_horario, profesor_id=profesor, asignatura_id=asignatura)
    return redirect('clases')


def edicion_clase(request, id):
    clase = Clase.objects.get(id=id)
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()
    data = {'clase': clase, 'asignaturas': asignaturas,
            'profesores': profesores}
    return render(request, 'clases/editar_clases.html', data)


def editar_clase(request):
    clase_id = request.POST['clase_id']
    clase_salon = request.POST['clase_salon']
    clase_horario = request.POST['clase_horario']
    profesor = request.POST['profesor']
    asignatura = request.POST['asignatura']

    clase_modelo = Clase.objects.get(id=clase_id)
    clase_modelo.salon = clase_salon
    clase_modelo.horario = clase_horario
    clase_modelo.profesor_id = profesor
    clase_modelo.asignatura_id = asignatura
    clase_modelo.save()
    return redirect('clases')


def eliminar_clase(request, id):
    clase = Clase.objects.get(id=id)
    clase.delete()
    return redirect('clases')


# Crud profesores
def profesores(request):
    mensaje = ''
    if obtener_profesores():
        mensaje = 'Datos de los profesores obtenidos'
    profesores = Profesor.objects.all()
    data = {'mensaje': mensaje, 'profesores': profesores}
    return render(request, 'profesores/listar_profesores.html', data)


def edicion_profesores(request, id):
    profesor = Profesor.objects.get(id=id)
    return render(request, 'profesores/editar_profesor.html', {'profesor': profesor})


def editar_profesor(request):
    pro_id = request.POST['pro_id']
    pro_nombre = request.POST['pro_nombre']
    pro_correo = request.POST['pro_correo']
    pro_telefono = request.POST['pro_telefono']

    profesor_modelo = Profesor.objects.get(id=pro_id)
    profesor_modelo.nombre = pro_nombre
    profesor_modelo.correo = pro_correo
    profesor_modelo.telefono = pro_telefono
    profesor_modelo.save()
    return redirect('profesores')


# Crud asignaturas
def asignaturas(request):
    mensaje = ''
    if obtener_profesores():
        mensaje = 'Datos de los profesores obtenidos'
    asignaturas = Asignatura.objects.all()
    data = {'mensaje': mensaje, 'asignaturas': asignaturas}
    print(mensaje)
    return render(request, 'asignaturas/listar_asignaturas.html', data)


def guardar_asignatura(request):
    asig_codigo = request.POST['asig_codigo']
    asig_nombre = request.POST['asig_nombre']

    Asignatura.objects.create(nombre=asig_nombre, codigo=asig_codigo)
    return redirect('/')


def edicion_asignatura(request, id):
    asignatura = Asignatura.objects.get(id=id)
    return render(request, 'asignaturas/editar_asignaturas.html', {'asignatura': asignatura})


def editar_asignatura(request):
    asig_id = request.POST['asig_id']
    asig_codigo = request.POST['asig_codigo']
    asig_nombre = request.POST['asig_nombre']

    asignatura_modelo = Asignatura.objects.get(id=asig_id)
    asignatura_modelo.nombre = asig_nombre
    asignatura_modelo.codigo = asig_codigo
    asignatura_modelo.save()
    return redirect('/')


def eliminar_asignatura(request, id):
    asignatura = Asignatura.objects.get(id=id)
    asignatura.delete()
    return redirect('/')
