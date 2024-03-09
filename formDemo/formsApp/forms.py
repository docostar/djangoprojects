from django import forms

class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField(required=True)
    gender = forms.CharField(widget=forms.Select(choices=GENDER), required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()


    def clean_firstName(self):
        inputFirstName=self.cleaned_data['firstName']
        if(len(inputFirstName)>=5):
            raise forms.ValidationError("Max length for firstname should be 5")
        return inputFirstName