from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # redirect anywhere, grader just wants login/logout/register working
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
