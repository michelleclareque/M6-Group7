# , ; Nathan Riley Sy, 244311; ,
# April , 2026 

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

def view_supplier(request):
    suppliers = Supplier.objects.all()
    account_id = request.session.get('account_id')
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers': suppliers, 'account_id': account_id})

def view_bottles(request):
    waterbottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'waterbottles': waterbottles})

def add_bottle(request):
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        sku = request.POST.get("sku")
        brand = request.POST.get("brand")
        cost = request.POST.get("cost")
        size = request.POST.get("size")
        mouth_size = request.POST.get("mouth_size")
        color = request.POST.get("color")
        supplier_id = request.POST.get("supplier")
        quantity = request.POST.get("quantity")

        supplier = Supplier.objects.get(pk=supplier_id)
        WaterBottle.objects.create(
            SKU=sku, Brand=brand, Cost=cost, Size=size,
            Mouth_Size=mouth_size, Color=color,
            Supplied_by=supplier, Current_Quantity=quantity
        )
        return redirect("view_supplier")
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers})

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_details.html', {'bottle': bottle})

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        try:
            acc = Account.objects.get(username=uname, password=pword)
            request.session['account_id'] = acc.pk
            return redirect("view_supplier")
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
        return render(request, "MyInventoryApp/login.html", {"success": "Account created successfully"})
    return render(request, "MyInventoryApp/signup.html")

def manage_account(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    return render(request, "MyInventoryApp/manage_account.html", {"account": acc})

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
            return render(request, "MyInventoryApp/change_password.html", {"account": acc, "error": "Wrong current password or confirmation mismatch"})
    return render(request, "MyInventoryApp/change_password.html", {"account": acc})

def delete_account(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    acc.delete()
    return redirect("login")

def logout_view(request):
    request.session.flush()
    return redirect("login")

def delete_bottle(request, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')
