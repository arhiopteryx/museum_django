from django.shortcuts import render, get_object_or_404, redirect
from .models import Exhibit
from .forms import ExhibitForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Эта функция для входа в систему
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('exhibit_list')  # Перенаправляем на список экспонатов
        else:
            return render(request, 'exhibits/login.html', {'error': 'Неверные учетные данные.'})
    return render(request, 'exhibits/login.html')

# Эта функция для регистрации нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'exhibits/register.html', {'form': form})

# Эта функция для списка экспонатов
@login_required
def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, 'exhibits/exhibit_list.html', {'exhibits': exhibits})

# Эта функция для детализации экспоната
@login_required
def exhibit_detail(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    return render(request, 'exhibits/exhibit_detail.html', {'exhibit': exhibit})


# Эта функция для создания нового экспоната (доступ только для администраторов)
@login_required
def exhibit_create(request):
    if request.user.is_superuser:  # Проверка на суперпользователя
        if request.method == "POST":
            form = ExhibitForm(request.POST)
            if form.is_valid():
                exhibit = form.save()
                return redirect('exhibit_detail', pk=exhibit.pk)
        else:
            form = ExhibitForm()
        return render(request, 'exhibits/exhibit_form.html', {'form': form})
    else:
        return redirect('exhibit_list')  # Перенаправляем обычного пользователя на список

# Эта функция для редактирования существующего экспоната (доступ только для администраторов)
@login_required
def exhibit_edit(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    if request.user.is_superuser:  # Проверка на суперпользователя
        if request.method == "POST":
            form = ExhibitForm(request.POST, instance=exhibit)
            if form.is_valid():
                exhibit = form.save()
                return redirect('exhibit_detail', pk=exhibit.pk)
        else:
            form = ExhibitForm(instance=exhibit)
        return render(request, 'exhibits/exhibit_form.html', {'form': form})
    else:
        return redirect('exhibit_list')  # Перенаправляем обычного пользователя на список

# Эта функция для удаления экспоната (доступ только для администраторов)
@login_required
def exhibit_delete(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    if request.user.is_superuser:  # Проверка на суперпользователя
        if request.method == "POST":
            exhibit.delete()
            return redirect('exhibit_list')
        return render(request, 'exhibits/exhibit_confirm_delete.html', {'exhibit': exhibit})
    else:
        return redirect('exhibit_list')  # Перенаправляем обычного пользователя на список