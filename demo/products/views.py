from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,FormView
from .models import Brand,Product,Cart
from .serializers import Brand_Serializer
from django.db.models import Q
from .forms import CartForm
from account.models import *
from django.http import JsonResponse
from django.contrib import messages
from .tasks import send_email_task
# Create your views here.


class IndexView(TemplateView):
	template_name = "index.html"
	def get_context_data(self,**kwargs):
		context={}
		product_obj=Product.objects.all()[:20]
		context['product_obj']=product_obj
		return context


class HomeView(View):
	def get(self,request):
		product_obj=Product.objects.all()[:20]
		return render(request,'index.html',{'product_obj':product_obj})
	def post(self,request):
		u_name=request.POST.get('u_name')
		u_pass=request.POST.get('u_pass')
		u_obj=User.objects.filter(u_name=u_name).filter(u_password=u_pass)
		if len(u_obj)==0:
			messages.error(request, 'User credentials are incorrect.')
			return render(request,'login.html')

		else:
			product_obj=Product.objects.all()[:20]
			return render(request,'index.html',{'product_obj':product_obj})

class CategoryView(ListView):
	model=Brand
	template_name='category.html'
	def get_queryset(self):
		brand_obj=Brand.objects.first()
		queryset={"Brand":Brand.objects.all(),"Product":Product.objects.all(),"product_obj":Product.objects.filter(brand_id=brand_obj.pk)}
		return queryset
	context_object_name = "Shop_Obj"


class ProductDetail(TemplateView):
	template_name='productDetail.html'
	def get_context_data(self,**kwargs):
		product_id=kwargs['id']
		product_obj=Product.objects.get(pk=product_id)
		similar_products=Product.objects.filter(brand_id=product_obj.brand_id)
		context={}
		context['product_obj']=product_obj
		context['similar_products']=similar_products
		return context


class ListProducts(ListView):
	model=Product
	template_name='category.html'
	def get_queryset(self,*args,**kwargs):
		URL=self.request.META['PATH_INFO']
		brand_id=URL.split('/')[2]
		product_obj=Product.objects.filter(brand_id=brand_id)
		queryset={"Brand":Brand.objects.all(),"product_obj":product_obj}
		return queryset
	context_object_name = "Shop_Obj"

class SearchView(View):
	def get(self,request,process):
		search_text=request.GET.get('q')
		brand_search_obj=Brand.objects.filter(brand_name__contains=search_text).values_list('brand_id',flat=True)
		pro_search_obj=Product.objects.filter(product_name__contains=search_text) | Product.objects.filter(brand_id__in=brand_search_obj)
		return render(request,'index.html',{"product_obj":pro_search_obj})

class ProductSearchView(View):
	def get(self,request,process):
		search_text=request.GET.get('q')
		brand_search_obj=Brand.objects.filter(brand_name__contains=search_text).values_list('brand_id',flat=True)
		pro_search_obj=Product.objects.filter(product_name__contains=search_text) | Product.objects.filter(brand_id__in=brand_search_obj)
		search_flag=1
		return render(request,'category.html',{"product_obj":pro_search_obj,"search_flag":search_flag,"Brand":Brand.objects.all()})



class AddCartView(FormView):
	form_class=CartForm
	def get(self,request,*args,**kwargs):
		if request.user.pk!=None:
			product_id=request.GET.get('product_id')
			product_obj=Product.objects.get(pk=product_id)
			user_obj=User.objects.get(pk=request.user.pk)
			total_cart_obj=Cart.objects.all().values_list('product_id',flat=True)
			if int(product_id) in total_cart_obj:
				cart_obj=Cart.objects.get(product_id=product_id)
				count=cart_obj.product_qnt
				price=cart_obj.product_price
				price=price+int(product_obj.product_price)
				count+=1
				cart_obj.product_qnt=count
				cart_obj.product_price=price
				cart_obj.save()
			else:
				cart_obj=Cart(product_id=product_obj,product_qnt=1,product_price=product_obj.product_price,user_id=user_obj)
				cart_obj.save()
			status=1
			return JsonResponse({'status':status},safe=False)
		else:
			profile=0

			return render(request,'login.html',{'profile':profile})
class CheckoutView(View):
	def get(self,request):
		user_id=request.user.pk
		cart_obj=Cart.objects.filter(user_id=1)
		total_price=0
		for i in cart_obj:
			total_price=total_price+i.product_price
		return render(request,'cart.html',{'cart_obj':cart_obj,'total_price':total_price})


class SendMailView(View):
	def get(self,request):
		mail_message=[]
		user_obj=User.objects.get(user_id=1)
		mail_message.append('Name : ' + user_obj.u_name)
		mail_message.append('Mobile Number : ' + user_obj.mobile_num)
		cart_obj=Cart.objects.filter(user_id=request.user.pk)
		for i in cart_obj:
			qnt=i.product_qnt
			if qnt>=i.product_id.product_qnt:
				i.product_status=False
				i.save()
				mail_message.append('Product ' + i.product_id.product_name +' is out of stock ')
			else:
				mail_message.append('Product '+ i.product_id.product_name + ' is ready for dispatch.')
		mail_message='\n'.join(mail_message)
		message=send_email_task.delay('About your order',mail_message,[user_obj.email_id])
		messages.success(request, 'Checkout details sent to mail successfully.')

		product_obj=Product.objects.all()[:20]
		return render(request,'index.html',{'product_obj':product_obj})
