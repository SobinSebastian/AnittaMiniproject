from django.shortcuts import render,redirect
from .models import CustomUser,UserProfile
from .models import CustomerProfile  # Import the correct model
from django.contrib.auth.decorators import login_required
# from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate ,login as auth_login,logout 
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import CustomUser
from .models import WatchProduct


 
@never_cache
def index(request):
    return render(request, 'index.html')
def service(request):
    return render(request, 'service.html')
def repair(request):
    return render(request, 'repair.html')


def about(request):
    
    return render(request, 'about.html')

@never_cache
def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm', None)
        # role = CustomUser.CUSTOMER
        if name and username and email and phone and password:
            if CustomUser.objects.filter(email=email).exists():
                messages.success(request,("Email is already registered."))
                return redirect('register_user')
            elif  CustomUser.objects.filter(username=username).exists():
                messages.success(request,("Username is already registered."))
                return redirect('register_user')

            
            elif password!=confirm_password:
                messages.success(request,("Password's Don't Match, Enter correct Password"))
            else:
                user = CustomUser(name=name,username=username, email=email, phone=phone)
                user.set_password(password)  # Set the password securely
                user.is_active=True
                user.save()
                user_profile = UserProfile(user=user)
                user_profile.save()

                # activateEmail(request, user, email)
                return redirect('login')  
            
    return render(request, 'register_user.html')

@never_cache
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        

        if username and password:
            user = authenticate(request, username =username , password=password)
            if user is not None:
                auth_login(request,user)
            
                if request.user.user_types==CustomUser.CUSTOMER:
                    request.session['is_authenticated'] = True
                
                    return redirect('/')
                # elif request.user.user_typ == CustomUser.VENDOR:
                #     print("user is therapist")
                #     return redirect(reverse('therapist'))
                elif request.user.user_types == CustomUser.ADMIN:
                    print("user is admin")                   
                    return redirect('adminpanel')
                # else:
                #     print("user is normal")
                #     return redirect('')

            else:
                messages.success(request,("Invalid credentials."))
        else:
            messages.success(request,("Please fill out all fields."))
        
    return render(request, 'login.html')



def Customer_Profile(request):
    # Ensure that the user is authenticated
    if not request.user.is_authenticated:
        # Handle the case where the user is not authenticated, e.g., redirect to the login page.
        return redirect('login')  # Replace 'login' with the name of your login view.

    # Get or create the user's profile
    user_profile, created = CustomerProfile.objects.get_or_create(customer=request.user)

    if request.method == 'POST':
        # Handle the POST request for updating user profile fields
        name = request.POST.get('name')
        street_address=request.POST.get('street_address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        #last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')

        # Update the user profile fields
        user_profile.name = name
        user_profile.street_address=street_address
        user_profile.country=country
        user_profile.state=state
        user_profile.pincode=pincode
        
        user_profile.phone= phone
        user_profile.save()

        messages.success(request, 'Profile updated successfully')  # Display a success message
        return redirect('Customer_Profile')  # Redirect to the same page or another page after update

    # Handle the GET request for displaying the user profile form
    context = {
        'user_profile': user_profile,
        'form_submitted': False,
    }
    return render(request, 'Customer_Profile.html', context)

# def forgotpassword(request):
#     return render(request, 'forgotpassword.html')

@login_required(login_url='login')
def custom_logout(request):
     if request.session.get('is_authenticated'):
        del request.session['is_authenticated'] 
        logout(request)
        return redirect('index')
@login_required
def adminpanel(request):
    return render(request, 'adminpanel.html')


@never_cache
def view_products(request):
    products = WatchProduct.objects.all()  # Retrieve all products from the database
    return render(request, 'view_products.html', {'products': products})


@login_required
def customer_product_view(request):
    products = WatchProduct.objects.all()
    return render(request, 'customer_product.html', {'products': products})

# Django view to delete the product
from django.shortcuts import render, redirect





from django.shortcuts import get_object_or_404

def delete_product(request, product_id):
    product = get_object_or_404(WatchProduct, pk=product_id)
    product.status = 'disabled'  # Mark the product as deactivated
    product.save()
    return redirect('view_products')


# views.py

from django.shortcuts import render, get_object_or_404, redirect

def edit_product(request, product_id):
    # Get the existing product object
    product = get_object_or_404(WatchProduct, id=product_id)

    if request.method == 'POST':
        # Retrieve the data from the form
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_sale_price = request.POST['product_sale_price']
        discount = request.POST['discount']
        watch_description = request.POST['watch_description']

        # Update the fields of the existing product object
        product.product_name = product_name
        product.product_price = product_price
        product.product_sale_price = product_sale_price
        product.discount = discount
        product.watch_description = watch_description

        # Save the changes
        product.save()

        return redirect('view_products')

    return render(request, 'edit_product.html', {'product': product})




@never_cache
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['productName']
        product_price = request.POST['productPrice']
        product_sale_price = request.POST['productSalePrice']
        discount = request.POST['discount']
        watch_description = request.POST['watchDescription']
        watch_image = request.FILES['watchImage']
        category = request.POST['category']  # Get the category field from the form

        # Check if a product with the same name and category already exists
        if WatchProduct.objects.filter(product_name=product_name, category=category).exists():
            messages.error(request, f"A product with the name '{product_name}' in the category '{category}' already exists.")
        else:
            try:
                # Ensure the numerical fields are valid numbers before saving
                product_price = float(product_price)
                product_sale_price = float(product_sale_price)
                discount = float(discount)
                
                # Create a new WatchProduct instance and save it
                WatchProduct.objects.create(
                    product_name=product_name,
                    product_price=product_price,
                    product_sale_price=product_sale_price,
                    discount=discount,
                    watch_description=watch_description,
                    watch_image=watch_image,
                    category=category  # Set the category field
                )
                messages.success(request, "Product added successfully.")
            except (ValueError, TypeError):
                messages.error(request, "Invalid numerical input.")

        return redirect('view_products')
    
    return render(request, 'add_product.html')


from django.shortcuts import render, get_object_or_404, redirect


def edit_product(request, product_id):
    # Retrieve the product you want to edit (you need to fetch it from your database)
    product = WatchProduct.objects.get(pk=product_id)

    if request.method == 'POST':
        product_name = request.POST['product_name']
        category = request.POST['category']  # Retrieve the category field
        product_price = request.POST['product_price']
        product_sale_price = request.POST['product_sale_price']
        discount = request.POST['discount']
        watch_description = request.POST['watch_description']
        watch_image = request.FILES.get('product_image')  # Use get() to avoid errors

        # Update the product fields
        product.product_name = product_name
        product.category = category  # Update the category
        product.product_price = product_price
        product.product_sale_price = product_sale_price
        product.discount = discount
        product.watch_description = watch_description

        if watch_image:
            product.watch_image = watch_image

        product.save()  # Save the updated product

        # Redirect to the view product page or wherever you want
        return redirect('view_products')

    return render(request, 'edit_product.html', {'product': product})


from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def activate_user(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.is_active = True  # Activate the user
        user.save()
        send_activation_email(user)  # Send activation email
        return redirect('adminpanel')  # Redirect to a suitable page
    except CustomUser.DoesNotExist:
        return redirect('adminpanel')

def deactivate_user(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.is_active = False  # Deactivate the user
        user.save()
        send_deactivation_email(user)  
        return redirect('adminpanel') 
    except CustomUser.DoesNotExist:
        return redirect('adminpanel')







from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WatchProduct  # Import your WatchProduct model
from .models import AddToCart

def add_to_cart(request, product_id):
    product = get_object_or_404(WatchProduct, id=product_id)
    
    # Check if the product is in stock
    if product.stock <= 0:
        messages.warning(request, f"{product.product_name} is out of stock.")
    else:
        # Get or create a cart item for the user and the selected product
        cart_item, created = AddToCart.objects.get_or_create(user=request.user, product=product)
        
        if not created:
            # If the cart item already exists, update its quantity and set it as active
            cart_item.is_active = True
            cart_item.quantity += 1
            cart_item.save()
        else:
            # If it's a new item, set it as active
            cart_item.is_active = True
            cart_item.save()
    
    return redirect('view_cart')  

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import AddToCart, WatchProduct

from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    cart_items = AddToCart.objects.filter(user=request.user, is_active=True)
    # Your view logic goes here

    
    # Calculate order summary
    subtotal = sum(item.product.product_price * item.quantity for item in cart_items)
    shipping = 10  # Adjust this value as needed
    total = subtotal + shipping
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    }
    return render(request, 'view_cart.html', context)

# View to remove an item from the cart
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(AddToCart, id=item_id)
    
    # Check if the item belongs to the current user
    if cart_item.user == request.user:
        cart_item.is_active = False
        cart_item.save()
        messages.success(request, f"{cart_item.product.product_name} has been removed from your cart.")
    else:
        messages.error(request, "You don't have permission to remove this item from your cart.")
    
    return redirect('view_cart')

# View to place an order
def place_order(request):
    # Here, you can implement the logic to create an order based on the items in the cart.
    # For example, create an Order model and related logic to finalize the order.
    
    # After creating the order, you can clear the cart.
    AddToCart.objects.filter(user=request.user, is_active=True).update(is_active=False)
    
    messages.success(request, "Your order has been placed successfully.")
    return redirect('view_cart')

from django.http import HttpResponse

def update_cart(request, item_id):
    # Your view logic here
    return HttpResponse("Update Cart View")