from django import forms
from .models import User, Lesson, Transfer
import datetime

class GenericSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

    def save(self):
        super().save(commit=False)

class StudentSignUpForm(GenericSignUpForm):
    def save(self):
        super().save()
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('new_password'), 
            user_type = 1
        )
        return user

class AdultSignUpForm(GenericSignUpForm):
    def save(self):
        super().save()
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('new_password'), 
            user_type = 2
        )
        return user

class TeacherSignUpForm(GenericSignUpForm):
    def save(self):
        super().save()
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('new_password'), 
            user_type = 3
        )
        return user

class LogInForm(forms.Form):

    username = forms.CharField(label="Username")
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class LessonRequestForm(forms.ModelForm):
    """Form for the user to request lessons.

    The lesson author must be by the lesson requestor.
    """

    class Meta:
        """Form options."""

        model = Lesson
        fields = ['number_of_lessons', 'lesson_duration', 'teacher']
        number_of_lesson = forms.IntegerField(label='Number of lessons')
        lesson_duration = forms.IntegerField(label='Lesson duration')
        teacher = forms.CharField(label='Teacher')
        

class RecordTransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['amount-paid', 'invoice_number', 'date']
   
    amount_paid = forms.CharField(label='Amount Paid by Student')
    invoice_number = forms.ChoiceField(label='Invoice Number')
    date = datetime.date.today()

    def clean(self):
        super().clean()

    def save(self):
        super().save(commit=False)

        transfer = Transfer.objects.create(
            invoice_number = self.invoice_number,
            amount = self.amount,
            date = self.date
        )
        
        return transfer

            
