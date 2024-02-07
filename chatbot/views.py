from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from .forms import LoginForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'chatbot/login.html' 
    fields = '__all__'
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, self.template_name, {'error_message': 'Invalid credentials'})

 




# class CustomLoginView(LoginView):
#     template_name = 'chatbot/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('index')


    
class RegisterPage(FormView):
    template_name = 'chatbot/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)
    
    
    


def index(request):
    return render(request, 'chatbot/index.html')


# def article(request,article_id):
#     return render(request, 'chatbot/index.html', {'article_id':article_id})

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)