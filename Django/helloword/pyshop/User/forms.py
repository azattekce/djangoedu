from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

# Kullanıcı Kayıt Formu
class RegisterForm(forms.Form):
    username = forms.CharField(label="Soyad",max_length=25,min_length=3)
    password =forms.CharField(label="Şifre",widget=forms.PasswordInput)
    confirm = forms.CharField(label="Şifreyi doğrula",max_length=25,min_length=3,widget=forms.PasswordInput)
    
    def clean(self):# custom valition yazmak için kulalnılır.
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if(password and confirm and password!=confirm):
            raise forms.ValidationError("Parola eşleşmiyor")
        
        values={
        "username":username,
        "password":password
        }

        return values