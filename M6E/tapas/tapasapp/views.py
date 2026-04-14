# Michelle Clare Que, 243687; Nathan Riley Sy, 244311; Andrew Gabriel Zapico, 246798
# April 13, 2026

'''
I hereby attest to the truth of the following facts:

I have not discussed the Python language code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Account
from django.contrib import messages

account_id = 0

def basic_list(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    acc = get_object_or_404(Account, pk=account_id)
    dishes = Dish.objects.all()
    return render(request, "tapasapp/basic_list.html", {
        "account": acc,
        "dishes": dishes
    })

def better_menu(request):
    global account_id
    if account_id == 0:
        return redirect('login')
    dish_objects = Dish.objects.all()
    acc = Account.objects.get(pk=account_id)
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects, 'account':acc})

def change_password(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if acc.password == current_password and new_password == confirm_password:
            acc.password = new_password
            acc.save()
            return redirect("manage_account", pk=pk)
        else:
            return render(request, "tapasapp/change_password.html", {"account": acc, "error": " Wrong Current Password or Confirm Passowed doesn't match"})
    return render(request, "tapasapp/change_password.html", {"account": acc})

def add_menu(request):
    global account_id
    if account_id == 0:
        return redirect('login')
    acc = get_object_or_404(Account, pk=account_id)
    if request.method=="POST":
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu')
    return render(request, 'tapasapp/add_menu.html', {'account': acc})

def view_detail(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    d = get_object_or_404(Dish, pk=pk)
    acc = get_object_or_404(Account, pk=account_id)
    return render(request, 'tapasapp/view_detail.html', {'d': d, 'account': acc})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu')

def update_dish(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    acc = Account.objects.get(pk=account_id)
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d, 'account':acc})

def login_view(request):
    global account_id
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        try:
            account = Account.objects.get(username=uname, password=pword)
            account_id = account.pk
            return redirect("basic_list", pk=account_id)
        except Account.DoesNotExist:
            return render(request, "tapasapp/login.html", {"error": "Invalid login"})
    return render(request, "tapasapp/login.html")

def signup_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        if Account.objects.filter(username=uname).exists():
            return render(request, "tapasapp/signup.html", {"error": "Account already exists"})
        Account.objects.create(username=uname, password=pword)
        messages.success(request, "Account created successfully")
        return redirect("login")
    return render(request, "tapasapp/signup.html")

def logout_view(request):
    global account_id
    account_id = 0
    return redirect("login")

def delete_account(request, pk):
    global account_id
    acc = get_object_or_404(Account, pk=pk)
    acc.delete()
    account_id = 0
    return redirect("login")

def manage_account(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    acc = get_object_or_404(Account, pk=pk)
    return render(request, "tapasapp/manage_account.html", {"account": acc})
