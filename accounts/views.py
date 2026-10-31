from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Вітаємо, {user.username}. Ви успішно зареєструвалися")
            return redirect("menu:menu_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
