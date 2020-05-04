from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class UserFormView(View):
    form_class=UserForm
    template_name='myuser/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(email=email,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('myuser:login')
        
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    #use formset and refer sibtc
    form_class=LoginForm
    template_name='myuser/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        user_type_input=request.POST['user_type']
        user=authenticate(email=email,password=password)
        user_details=Myuser.objects.get(pk=request.user.id)
        user_type=user_details.user_type
        print(user_type)
        if user is not None:
            if user.is_active:
                login(request,user)
                if user_type=="HSP" and user_type==user_type_input:
                    return HttpResponse("<html>Welcome to Hospital</html>")
                    #return redirect('Attendance_manager:index_student')
                elif user_type=="AMB" and user_type==user_type_input:
                    return HttpResponse("<html>Welcome to Ambulance</html>")
                    #return redirect('Attendance_manager:index_student')
                elif user_type=="BLB" and user_type==user_type_input:
                    return HttpResponse("<html>Welcome to BLoodBank</html>")
                    #return redirect('Attendance_manager:index_student')
                elif user_type=="MST" and user_type==user_type_input:
                    return HttpResponse("<html>Welcome to Medical Store</html>")
                    #return redirect('Attendance_manager:index_student')
                else :
                    return HttpResponse("</html>Not Selected valid user type</html>")
                   # return redirect('Attendance_manager:mark_attendance')
                #messages.info(request, 'Your have successfully loged in!')
                #return redirect('myuser:login')
            else:
                return render(request, 'myuser/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'myuser/login.html', {'form':form,'error_message': 'Invalid login'})
        return render(request,self.template_name,{'form':form})

class LogoutView(View):
    form_class=LoginForm
    template_name='myuser/login.html'
    def get(self,request):
        form=self.form_class(None)
        logout(request)
        return redirect(reverse('myuser:login_user'))

