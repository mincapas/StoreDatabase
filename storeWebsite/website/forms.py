from storeDatabase.models import Review
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'phone_number', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-box'}),
            'email': forms.TextInput(attrs={'class': 'email-box'}),
            'phone_number': forms.TextInput(attrs={'class': 'phone-number-box'}),
            'content': forms.Textarea(attrs={'class': 'content-box'}),
        }

    # name = forms.CharField(label="Jūsų vardas")
    # email = forms.CharField(label="Elektroninis paštas", required=False)
    # phone_number = forms.CharField(label='Telefono numeris', required=False)
    # subject = forms.CharField(label="Tema", required=False)
    # message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
