
from django.urls import path, re_path
from .views import IndexView, AboutView, ContactView, create_contact, ServiceDetailView, ServicesListView, ArticleListView, ArticleDetailView, PortfoliolView, DemoView
app_name = 'core'

urlpatterns = [
    # path('admin/core/invoice/<int:invoice_id>/', admin_order_detail, name='admin_order_detail'),
    # path('admin/core/invoice/hii/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

    path('', IndexView.as_view(), name='index'),
    path('demo/', DemoView.as_view(), name='demo'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesListView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('realisations/', PortfoliolView.as_view(), name='realisations'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/', create_contact, name='contact'),


]
