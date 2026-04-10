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

# Create your views here.
def view_bottles(request, pk):
    supplier_objects = get_object_or_404(Supplier, pk=pk)
    waterbottle_objects = WaterBottle.objects.filter(supplier=supplier_objects)
    return render(request, 'MyInventoryApp/view_bottles.html', {'waterbottles':waterbottle_objects, 'supplier':supplier_objects})

def view_supplier(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', 
                  {
                      'suppliers':supplier_objects,
                      'account': acc
                    })

def add_bottle(request):
    if request.method=="POST":
        suppliers = Supplier.objects.all()
        name = request.POST.get('name')
        volume = request.POST.get('volume')
        supplier_id = request.POST.get('supplier')
        supplier = Supplier.objects.get(pk=supplier_id)
        WaterBottle.objects.create(name=name, volume=volume, supplier=supplier)
        return redirect('view_supplier')
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers})

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        try:
            acc = Account.objects.get(username=uname, password=pword)
            return redirect("view_supplier", pk=acc.pk)
        except Account.DoesNotExist:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    return render(request, "MyInventoryApp/login.html")

def signup_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")

        if Account.objects.filter(username=uname).exists():
            return render(request, "MyInventoryApp/signup.html", {"error": "Account already exists"})
        else:
            Account.objects.create(username=uname, password=pword)
            return render(request, "MyInventoryApp/login.html", {"success": "Account created successfully"})
        
    return render(request, "MyInventoryApp/signup.html")

def view_detail(request, pk):
    d = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_detail.html', {'d': d})

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
            return render(request, "MyInventoryApp/change_password.html", {"account": acc, "error": " Wrong Current Password or Confirm Passowed doesn't match"})
    return render(request, "MyInventoryApp/change_password.html", {"account": acc})

def delete_account(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    acc.delete()
    return redirect("login")

def logout_view(request):
    return redirect("login")

def delete_bottle(request, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')