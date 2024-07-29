from django.shortcuts import render
from .models import Games, Buyer
from .forms import UserRegister


# Create your views here.
def index(request):
      pagename = "Главна страница"
      context = {'pagename': pagename}
      return render(request, 'task1/index.html', context)

def shop(request):
      goods = Games.objects.all()
      pagename = "Магазин"        
      context = {'goods':goods, 'pagename':pagename}

      return render(request, 'task1/shop.html', context)

def cart(request):
      pagename = "Корзина"
      cart_goods = {'Atomic':'1 400'}
      return render(request, 'task1/cart.html', {'cart_goods':cart_goods,
                                                       'pagename':pagename})

def sign_up_by_django(request):
      users = Buyer.objects.all()
      user_name = users.values_list('name', flat=True)
      context = {}
      info = {}
      if request.method == 'POST':
            form =  UserRegister(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']
                  password2 = form.cleaned_data['repeat_password']
                  age = int(form.cleaned_data['age'])

                  
                  if username in user_name:
                        info['error'] = "Такой пользователь уже существует"
                  elif password != password2:
                        info['error'] = "Пароли не совпрадают"
                  else:
                        info['info'] = "Приветствуем тебя {}".format(username)
                        Buyer.objects.create(name=username,balance=0.0 , age=age)

                  context = {"form":form.cleaned_data,
                             }
      else:
            form = UserRegister()
      
      context = {"info":info,}
      return render(request, 'task1/registration_page.html', context)