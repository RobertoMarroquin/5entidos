from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User


from .models import Usuario


def signup_view(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        passwordcon = request.POST['passwordcon']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        if password != passwordcon:
            return render(request,"signup.html",{'error':'Contrasenas no coinciden'})
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save()

            usuario = Usuario.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                usuario=user)


            usuario.save()
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect(reverse_lazy('ventas:catalogo'))

    return render(request,"signup.html")





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect ('ventas:catalogo')
        else:
            return render(request,'login.html',{   'error':'Usuario o contrasena invalidos',
                                                            'User':request.user.is_authenticated})
    return render(request,'login.html',{'User':request.user.is_authenticated})


def logout_func(request):
    logout(request)
    return redirect('usuarios:login')

    