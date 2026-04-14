# Michelle Clare Que, 243687; Nathan Riley Sy, 244311; ,
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
from .models import Supplier, WaterBottle, Account
from django.contrib import messages

account_id = 0

def view_supplier(request):
    global account_id
    if account_id == 0:
        return redirect('login')
    suppliers = Supplier.objects.all()
    account = Account.objects.get(pk=account_id)
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers': suppliers, 'account': account})

def view_bottles(request):
    global account_id
    if account_id == 0:
        return redirect('login')
    waterbottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'waterbottles': waterbottles})

def add_bottle(request):
    global account_id
    if account_id == 0:
        return redirect('login')
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        sku = request.POST.get("add_sku")
        brand = request.POST.get("add_brand")
        cost = request.POST.get("add_cost")
        size = request.POST.get("add_size")
        mouth_size = request.POST.get("add_mouth_size")
        color = request.POST.get("add_color")
        supplier_id = request.POST.get("supplier")
        quantity = request.POST.get("add_current_quantity")

        supplier = Supplier.objects.get(pk=supplier_id)
        WaterBottle.objects.create(
            SKU=sku, Brand=brand, Cost=cost, Size=size,
            Mouth_Size=mouth_size, Color=color,
            Supplied_by=supplier, Current_Quantity=quantity
        )
        return redirect("view_supplier")
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers})

def view_bottle_details(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_details.html', {'bottle': bottle})

def login_view(request):
    global account_id
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        try:
            account_id = Account.objects.get(username=uname, password=pword)
            account_id = account_id.pk
            return redirect('view_supplier')
        except Account.DoesNotExist:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    return render(request, "MyInventoryApp/login.html")

def signup_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        if Account.objects.filter(username=uname).exists():
            return render(request, "MyInventoryApp/signup.html", {"error": "Account already exists"})
        Account.objects.create(username=uname, password=pword)
        messages.success(request, "Account created successfully")
        return redirect("login")
    return render(request, "MyInventoryApp/signup.html")

def manage_account(request, pk):
    global account_id
    if account_id == 0:
        return redirect('login')
    account = get_object_or_404(Account, pk=pk)
    return render(request, "MyInventoryApp/manage_account.html", {"account": account})

def change_password(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if account.password == current_password and new_password == confirm_password:
            account.password = new_password
            account.save()
            return redirect("manage_account", pk=pk)
        else:
            return render(request, "MyInventoryApp/change_password.html", {"account": account, "error": "Wrong current password or confirmation mismatch"})
    return render(request, "MyInventoryApp/change_password.html", {"account": account})

def delete_account(request, pk):
    global account_id
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    account_id = 0
    return redirect("login")

def logout_view(request):
    global account_id
    account_id = 0
    return redirect("login")

def delete_bottle(request, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')

#def view_bottles_by_supplier(request, pk):
#    supplier = get_object_or_404(Supplier, pk=pk)
#    waterbottles = WaterBottle.objects.filter(Supplied_by_id=pk)
#    return render(request, "MyInventoryApp/view_bottles.html", {"supplier": supplier,"waterbottles": waterbottles})

def dropdown(request):
    suppliers = Supplier.objects.all()
    return render(request, "MyInventoryApp/add_bottle.html", {"suppliers": suppliers})