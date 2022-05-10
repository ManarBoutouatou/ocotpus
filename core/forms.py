from django import forms
from .models import Contact, Invoice
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','email','subject','message']
 

def must_be_empty(value):
    if value:
        raise forms.ValidationError('ce champs doit etre vide')

class ContactForm(forms.Form):
    name = forms.CharField(required = True, max_length=150) 
    email = forms.CharField(max_length=254)
    phone = forms.CharField(max_length=25)
    subject = forms.CharField(max_length=300) 
    honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])
    message = forms.CharField()    

        
class ContactForm(forms.ModelForm) :
    class Meta: 
        model = Contact 
        fields = '__all__' 
    def get_info(self):
        
        cleaned_data = super().clean()

        name = cleaned_data.get('name').strip()
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        msg = f'Bonjour {name},'
        msg += f'Octopus-consultung vous remercie de l&#8216;intérêt que vous portez à ses services, nous vous contacterons prochainement avec un e-mail détaillé concernant votre demande.'
        msg += f'Merci de votre temps,'
        msg += f'Bien à vous, '
        return subject, msg, email

    def send_email(self):

        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email= EMAIL_HOST_USER,
            recipient_list=[email],
        )


class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('client', 'client_rc', 'client_nif', 'client_art', 'client_adresse', 'invoice_number', 'invioce_date', 'note', 'discount',)
        required = ('client',)
       
