from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView
from .models import User
from django.contrib import messages
from .forms import UserForm
# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth import logout as auth_logout

class LoginView(TemplateView):
	template_name = "login.html"





class RegisterView(View):
	def get(self,request):
		return render(request, "registration.html")

class ViewProfileView(TemplateView):
	template_name = "viewProfile.html"
	def get_context_data(self,**kwargs):
		context={}
		u_id=1
		context['u_obj'] = User.objects.get(pk=u_id)
		return context
		
		
class EditProfileView(FormView):
	template_name="editProfile.html"
	form_class=UserForm
	def get_context_data(self,**kwargs):
		context={}
		u_id=1
		context['u_obj'] = User.objects.get(pk=u_id)
		return context
	def form_valid(self, form):
		form.save(self.request.user)
		return super(EditProfileView, self).form_valid(form)
	def get_success_url(self, *args, **kwargs):
		return reverse("some url name")

class SaveProfileView(View):
	def post(self,request):
		u_obj=User.objects.get(pk=request.POST.get('u_id'))
		u_obj.u_name=request.POST.get('u_name')
		u_obj.mobile_num=request.POST.get('u_mobile')
		u_obj.alternate_mobile_num=request.POST.get('u_alt_mobile')
		u_obj.save()
		profile=1
		return render(request,'viewProfile.html',{'profile':profile,'u_obj':u_obj})




