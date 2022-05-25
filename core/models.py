from telnetlib import RCP
from django.db import models
# Create your models here.
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Category(models.Model):
    name  = models.CharField(verbose_name=_('Nom du DAS'), max_length=100)
    title  = models.CharField(verbose_name=_('Petit text'), max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    icon  = models.ImageField(upload_to='images/categories', null=True, blank=True)
    actif = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    class Meta:
        verbose_name ="Catégorie"
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    name        = models.CharField(verbose_name=_('sous catégorie'), max_length=100)
    title       = models.TextField(verbose_name=_('Petit text'),blank=True, null=True)
    description = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    icon        = models.ImageField(upload_to='images/categories', null=True, blank=True)
    actif = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return self.name    
    
 

class Service(models.Model):
    name  = models.CharField(verbose_name=_('Nom du Service'), max_length=100)
    slug = models.SlugField()
    title  = models.TextField(verbose_name=_('Petit text'), blank=True, null=True)
    image = models.FileField( upload_to="images/services",verbose_name=_('img 1'), blank=True, null=True)
    photo  = models.ImageField(upload_to="images/services",verbose_name=_('img 2'),blank=True, null=True)
    description = tinymce_models.HTMLField(verbose_name='Déscription du service', blank=True, null=True)
    pricing = tinymce_models.HTMLField(verbose_name='offres du service', blank=True, null=True)
    icon  = models.CharField(verbose_name=_('nom de l icon du site https://fontawesome.com/icons'), max_length=100, blank=True, null=True)
    section  = models.CharField(verbose_name=_('section to show'), max_length=100,blank=True, null=True)
    to_home_page = models.BooleanField(verbose_name="ajouter a la page d'accueil", default=False)
    priority  = models.IntegerField(verbose_name=_('ordre / priorité'), blank=True, null=True)
    actif  = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:service-detail", kwargs={"slug": self.slug})

 

class Offre(models.Model):
    title        = models.CharField(verbose_name=_('Offre'), max_length=100)
    description  = tinymce_models.HTMLField(blank=True, null=True)
    prix         = models.DecimalField(max_digits=20,  decimal_places=0, blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('id',)
        verbose_name = 'offre'
        verbose_name_plural = 'offres'   


class Fonctionalite(models.Model):
    title        = models.CharField( max_length=100)
    description  = tinymce_models.HTMLField(blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('id',)
        verbose_name = 'fonctionalite'
        verbose_name_plural = 'fonctionalites' 

class Status(models.Model):
    service              = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True, null=True)
    offre                = models.ForeignKey(Offre, verbose_name=_("offre"), on_delete=models.CASCADE,blank=True, null=True)
    fonctionalite        = models.ForeignKey(Fonctionalite, verbose_name=_("fonctionalite"), on_delete=models.CASCADE,blank=True, null=True)
    included             = models.BooleanField(verbose_name="inclu dans l'offre", default=False)
    quantity             = models.CharField(verbose_name=_('quantité'), max_length=100,blank=True, null=True)
    created              = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated              = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return str(self.fonctionalite)

    class Meta:
        ordering = ('id',)
        verbose_name = 'status'
        verbose_name_plural = 'statuss'   


class Demo(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank =True)
    subject    = models.ForeignKey(Service, verbose_name=(_("Sujet")), on_delete=models.CASCADE)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent   = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Demo'
        verbose_name_plural = 'Demo'             

# TYPE_CHOICES = (
#     ('A', 'Une entreprise privée.'),
#     ('B', 'Un artisant / profession libérale.'),
#     ('C', 'Un particulier.'),
#     ('D', 'Un organisme public.'),
#     ('E', 'Une association.'),
#     ('F', 'Un établissement éducatif.'),
#     ('G', 'Autre'),
# )

# SIZE_CHOICES = (
#     ('H', '0 - 10'),
#     ('I', '11 - 100'),
#     ('J', 'plus de 100'),
# )
# GOAL_CHOICES = (
#     ('K', 'Faire connaitre mon entreprise.'),
#     ('L', 'Présentation de mes Produits / Services.'),
#     ('L', 'Vendre mes produits via le site web.'),
#     ('M', 'Site de formation.'),
#     ('N', 'Site d’informations (newsletters, news, vidéos…etc.)'),
# )
# LOGO_CHOICES = (
#     ('O', 'Je conserve ma charte graphique'),
#     ('P', 'Je souhaite Créer/ Modifier charte graphique'),
# )
# TEXT_CHOICES = (
#     ('Q', 'Ils n’existent pas encore.'),
#     ('R', 'Prises de vue à réaliser par le prestataire.'),
#     ('S', 'Elles sont libres de droitPrises de vue à réaliser par le prestataire.'),
#     ('T', 'Elles sont dans un format et dans des dimensions compatibles avec un site internet'),
# )
# LANGUAGE_CHOICES = (
#     ('U', 'ARABE'),
#     ('V', 'FRANÇAIS'),
#     ('W', 'ANGLAIS'),
# )
# FONCTIONALITE_CHOICES = (
#     ('U', 'ARABE'),
#     ('V', 'FRANÇAIS'),
#     ('W', 'ANGLAIS'),
# )
# class Devis(models.Model):
#     name         = models.CharField(verbose_name=_('Nom de la société'), max_length=250)
#     email        = models.EmailField(verbose_name=_("Email"))
#     secteur      = models.CharField(choices=TYPE_CHOICES, max_length=2, blank=True, null=True)
#     size         = models.CharField(choices=SIZE_CHOICES, max_length=2, blank=True, null=True)
#     activity     = models.CharField(verbose_name=_('Activité principale'), max_length=250, blank=True, null=True)
#     goals        = models.CharField(verbose_name=_('Autre') blank=True, null=True)
#     goal         = models.CharField(choices=GOAL_CHOICES, max_length=2, blank=True, null=True)
#     website      = models.CharField(verbose_name=_('Avez vous un site web existant ?'), max_length=250)
#     logo         = models.CharField(choices=LOGO_CHOICES, max_length=2, blank=True, null=True)
#     photo        = models.CharField(choices=PHOTO_CHOICES, max_length=2, blank=True, null=True)
#     texte        = models.CharField(choices=TEXT_CHOICES, max_length=2, blank=True, null=True)
#     languages    = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, null=True)
#     inspiration  = models.CharField(verbose_name=_('Source d’inspiration'), max_length=250, blank=True, null=True)
   

    
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Demo'
#         verbose_name_plural = 'Demo'       

class Contact(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank =True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True,null=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent   = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulaire de contact'
        verbose_name_plural = 'Formulaire de contact'

class Quote(models.Model):
    name = models.TextField(verbose_name=_("la citation"))
    actif = models.BooleanField(default=True)
    author = models.CharField(verbose_name=_("auteur"), max_length=100, blank=True, null=True)
    function = models.CharField(verbose_name=_("Fonction"), max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return str(self.autor)

class Article(models.Model):
    title   = models.CharField( max_length=150, verbose_name='Titre')
    slug    = models.SlugField()
    aperçu  = models.CharField( max_length=300, verbose_name='aperçu', blank=True, null=True)
    chapo   = models.CharField( max_length=300, verbose_name='chapô ',blank=True, null=True)
    quote  = models.CharField( max_length=300, verbose_name='phrase mise en avant ', blank=True, null=True)
    texte_haut   = tinymce_models.HTMLField(verbose_name='texte haut', blank=True, null=True)
    texte_bas   = tinymce_models.HTMLField(verbose_name='texte bas', blank=True, null=True)
    banner  = models.ImageField(upload_to="images/")
    publish = models.BooleanField(default=True)
    actif   = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse("core:service-detail", kwargs={"slug": self.slug})


class Portfolio(models.Model):
    title        = models.CharField(max_length=100)
    description   = tinymce_models.HTMLField(verbose_name='description ', blank=True, null=True)
    texte_haut   = tinymce_models.HTMLField(verbose_name='what we did for ghe client ', blank=True, null=True)
    website      = models.CharField(verbose_name=_('site du client'), max_length=100)
    image         = models.ImageField( upload_to="images/prtfolio")
    actif        = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('id',)
        verbose_name = 'portfolio'
        verbose_name_plural = 'portfolios'



class Client(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField( upload_to="images/clients")
    website = models.CharField(verbose_name=_('site du client'), max_length=100)
    actif = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return self.name

class Pagetitle(models.Model):
    title        = models.CharField(max_length=100)
    actif        = models.BooleanField(default=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return self.title

class Invoice(models.Model):
    client          = models.CharField(max_length=300,verbose_name='Client')
    client_rc       = models.CharField(max_length=300,verbose_name='RC Client')
    client_nif      = models.CharField(max_length=300,verbose_name='Nif Client')
    client_art      = models.CharField(max_length=300,verbose_name="Numéro d'article du client")
    client_adresse  = models.CharField(max_length=300,verbose_name='Adresse Client')
    client_phone    = models.CharField(max_length=300,verbose_name='Téléphone Client')
    client_email    = models.EmailField(max_length=300,verbose_name='Email Client')
    invoice_number  = models.IntegerField(verbose_name='Numéro de facture')
    invioce_date    = models.DateField(verbose_name=_("Date "), blank = True, null = True) 
    created       = models.DateTimeField(auto_now_add=True, verbose_name=_("Crée"))
    updated       = models.DateTimeField(auto_now=True, verbose_name=_("Modifié"))
    note          = models.TextField(blank=True, null=True, verbose_name=_("Note"))
    paid          = models.BooleanField(default=False, verbose_name=_("Payé"))
    discount      = models.DecimalField( max_digits=10, decimal_places=2, default=0, verbose_name="Réduction")

    def __str__(self):
        return f'facture N°:  {self.invoice_number} doit {self.client}'

    # def save(self, *args, **kwargs):
    #     try:
    #         last_num = Invoice.objects.last().invoice_number
    #         self.invoice_number = last_num =+ 1
    #     except:
    #         self.invoice_number = 1
    #     super().save(*args, **kwargs) 
    #     return sum(item.get_cost() for item in self.items.all())


    def get_total_cost(self):
        items_cost = sum(item.get_cost() for item in self.items.all())
        total_cost = items_cost - self.discount
        # if total_cost < 0:
        #     total_cost = 0

        return total_cost




class InvoiceItem(models.Model):
    invoice    = models.ForeignKey(Invoice,related_name='items', verbose_name=(_("Facture")), on_delete=models.CASCADE)
    description = models.CharField(max_length=300,verbose_name='Description')
    price    = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=_("Prix"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantité"))

    def __str__(self):
        return str(self.description)
    def get_cost(self):
        return self.price * self.quantity

