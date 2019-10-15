from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userForm
from .models import users
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.


def user_form(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application successfully submitted")
            return redirect('user_form')

    else:
        form = userForm()
    return render(request, 'user_info.html', {'form': form})

@login_required
def user(request):
    user_list= users.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        user = paginator.page(1)
    except EmptyPage:
        user = paginator.page(paginator.num_pages)
    return render(request, 'users.html',{'users': user})
