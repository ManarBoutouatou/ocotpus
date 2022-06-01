from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin
from business.models import Business
from .models import Invoice, Quote, Service, Contact, Client, Article, Pagetitle, Portfolio, Demo, Status, Fonctionalite, Offre
from .forms  import ContactForm, InvoiceCreateForm, DemoForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from config.decorators import user_created_order
from django.core.mail import send_mail



class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(priority__range=[1,6])
        context["quotes"] = Quote.objects.all()
        context["clients"] = Client.objects.all()
        return context



class ServiceDetailView(DetailView):
    model = Service
    template_name = "service-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service= self.get_object()
        # functions = service.fonctionalite_set.all()
        context["fonctionalities"] = Fonctionalite.objects.filter(service=service, priority__range=[1,100])
        context["offers"] = Offre.objects.filter(service=service)
        return context

class ServicesListView(ListView):
    model = Service
    context_object_name = "services"
    template_name = "services.html"
    


class PortfoliolView(ListView):
    model = Portfolio
    template_name = "realisations.html"
    context_object_name = "portfolios"


class AboutView(TemplateView):
    template_name = "about.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog_detail.html"

class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog.html"

class DemoView(SuccessMessageMixin, CreateView):
    template_name= "demo.html"
    form_class= DemoForm
    model = Contact 
    success_message = "Votre message a été envoyé avec succès."
    success_url = reverse_lazy('core:demo')
   
    def form_valid(self, form):
        form.send_email() 
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,form.errors)
        return redirect('business:recruiting')

# class ContactView(SuccessMessageMixin, CreateView):
#     template_name= "contact.html"
#     form_class= ContactForm
#     model = Contact 
#     success_message = "Votre message a été envoyé avec succès."
#     success_url = reverse_lazy('core:contact')
   
#     def form_valid(self, form):
#         form.send_email() 
#         return super().form_valid(form)
        
#     def form_invalid(self, form):
#         messages.error(self.request,form.errors)
#         return super().form_invalid(form)

class ContactView(SuccessMessageMixin, CreateView):
    template_name= "contact.html"
    form_class= ContactForm
    model = Contact 
    success_message = "Votre message a été envoyé avec succès, Nous vous contacterons prochainement avec un appel téléphonique ou un e-mail."
    success_url = reverse_lazy('core:contact')
    def form_valid(self, form):
        form.send_email() 
        return super().form_valid(form)

def create_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.send_email() 
        form.save()
    messages.success(request, f'Votre message a été envoyé avec succès.')
    if request.htmx:
        return render(request, 'snippets/message.html', {response : " RAHO YEMCHIIIIIIII"} )
    return render(request, 'contact.html',)



# def create_contact(request):
#     print('raho yemchi')
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.send_email() 
#             form.save()
#         messages.success(request, f'Votre message a été envoyé avec succès.')
#         if request.htmx:
#             return render(request, 'snippets/message.html', {response : " RAHO YEMCHIIIIIIII"} )
#     return render(request, 'contact.html',)

# @staff_member_required
# def admin_order_detail(request, invoice_id):
#     print('admin_order_detail ')
#     order = get_object_or_404(Invoice, id=invoice_id)
#     return render(request, 'order_detail.html', {'order': order})

# @staff_member_required
# def admin_order_pdf(request, invoice_id):
#     print('admin_order_pdf ')

#     invoice = get_object_or_404(Invoice, id=invoice_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename=order_{invoice.id}.pdf'
#     try :
#         business = Business.objects.first().name
#     except: 
#         business = "Octopus Consulting"
#     html = render_to_string('order_pdf.html' , {'invoice' : invoice, 'business': business})
#     # stylesheets=[weasyprint.CSS(str(configs.STATIC_ROOT) + 'css/pdf.css' )]
#     weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
#     return response

# @user_created_order
# def invoice_pdf(request, invoice_id):
#     print('invoice_pdf ')
#     order = get_object_or_404(Invoice, id=invoice_id)
#     if request.user == order.user:
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
#         try :
#             business   = Business.objects.first().name
#         except: 
#             business = " Octopus Consulting"
#         # generate pdf
#         html = render_to_string('order_pdf.html' , {'order' : order, 'business': business})
#         # stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
#         weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
#         return response
#     return redirect('admin:index')