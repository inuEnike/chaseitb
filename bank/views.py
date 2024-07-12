from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from .forms import UserRegistrationForm, UserLoginForm, SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')



# def activateEmail(request, user, to_email):
#     mail_subject = "Activate your user account."
#     message = render_to_string("bank/template_activate_account.html", {
#         'user': user.username,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         "protocol": 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     if email.send():
#         messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
#                 received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
#     else:
#         messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def activateEmail(request, user, to_email):
    try:
        mail_subject = "Activate your user account."
        message = render_to_string("bank/template_activate_account.html", {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            "protocol": 'https' if request.is_secure() else 'http'
        })
        email = EmailMessage(mail_subject, message, to=[to_email])
        
        if email.send():
            messages.success(request, f'Dear <b>{user.username}</b>, please go to your email <b>{to_email}</b> inbox and click on the received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
        else:
            messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')
    except Exception as e:
        messages.error(request, f'An error occurred while sending the activation email: {str(e)}')
    return redirect('bank/template_activate_account.html')  # Replace 'some_view_name' with the actual view name where you want to redirect

def template_activate_account(request):
    context = {}
    return render (request, "bank/template-activate-account.html", context)

def home( request):
    return render (request, 'bank/home.html') 

def about( request):
    return render (request, 'bank/about.html') 


def contact( request):
    return render (request, 'bank/contact.html') 

def account_details( request):
    return render (request, 'bank/account-details.html') 

def account( request):
    return render (request, 'bank/account.html') 

@login_required (login_url = "login")
def bill( request):
    return render (request, 'bank/bill.html') 

def business_loan( request):
    return render (request, 'bank/business-loan.html') 

def car_loan( request):
    return render (request, 'bank/car-loan.html') 

def card( request):
    return render (request, 'bank/card.html') 

@login_required (login_url = "login")
def cards( request):
    card = request.user.card
    form = CardForm (instance = card)

    if request.method == 'POST':
        form = CardForm (request.POST, request.FILES, instance = card)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'bank/cards.html', context) 

def career_single( request):
    return render (request, 'bank/career-single.html') 

 
@login_required (login_url = "login")
def change_password( request):
    return render (request, 'bank/change-password.html') 

@login_required (login_url = "login")
def coin_details( request):
    return render (request, 'bank/coin-details.html') 

@login_required (login_url = "login")
def pin_validation( request):
    pin = request.user.pin
    form = PinForm (instance = pin)

    if request.method == 'POST':
        form = PinForm (request.POST, request.FILES, instance = pin)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'bank/pin-validation.html', context) 

@login_required (login_url = "login")
def crypto_send( request):
    return render (request, 'bank/crypto-send.html') 

@login_required (login_url = "login")
def crypto_transaction( request):
    return render (request, 'bank/crypto-transaction.html') 

@login_required (login_url = "login")
def crypto_view_transaction( request):
    return render (request, 'bank/crypto-view-transaction.html') 

@login_required (login_url = "login")
def crypto_withdraw( request):
    return render (request, 'bank/crypto-withdraw.html') 

@login_required (login_url = "login")
def crypto( request):
    return render (request, 'bank/crypto.html') 

@login_required (login_url = "login")
def dashboard( request):
    return render (request, 'bank/dashboard.html') 

def educations_loan( request):
    return render (request, 'bank/educations-loan.html') 

@login_required (login_url = "login")
def forgot_password( request):
    return render (request, 'bank/forgot-password.html') 

@login_required (login_url = "login")
def help( request):
    return render (request, 'bank/help.html') 

def home_loan( request):
    return render (request, 'bank/home-loan.html') 

def home( request):
    return render (request, 'bank/home.html') 

def insight( request):
    return render (request, 'bank/insight.html') 

@login_required (login_url = "login")
def make_payment( request):
    return render (request, 'bank/make-payment.html') 

@login_required (login_url = "login")
def my_account( request):
    profile = request.user.profile
    form = ProfileForm (instance = profile)

    if request.method == 'POST':
        form = ProfileForm (request.POST, request.FILES, instance = profile)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'bank/my-account.html', context)

@login_required (login_url = "login")
def my_portfolio( request):
    return render (request, 'bank/my-portfolio.html') 

@login_required (login_url = "login")
def news_update_details( request):
    return render (request, 'bank/news-update-details.html') 

@login_required (login_url = "login")
def news_update( request):
    return render (request, 'bank/news-update.html') 

@login_required (login_url = "login")
def notification( request):
    return render (request, 'bank/notification.html') 

@login_required (login_url = "login")
def otp( request):
    return render (request, 'bank/otp.html') 

@login_required (login_url = "login")
def pay_successfully( request):
    return render (request, 'bank/pay-successfully.html') 


def personal_identity( request):

    return render (request, 'bank/personal-identity.html') 

def personal_loan( request):
    return render (request, 'bank/personal-loan.html') 

def preloader( request):
    return render (request, 'bank/preloader.html') 

def privacy_policy( request):
    return render (request, 'bank/privacy-policy.html') 

def product( request):
    return render (request, 'bank/product.html') 

@login_required (login_url = "login")
def profile( request):
    return render (request, 'bank/profile.html') 

@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="bank/register.html",
        context={"form": form}
        )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("dashboard")

@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("signin-successfully")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="bank/login.html",
        context={"form": form}
        )

@login_required (login_url = "login")
def reset_password( request):
    return render (request, 'bank/reset-password.html') 

def secure( request):
    return render (request, 'bank/secure.html') 


def service( request):
    return render (request, 'bank/service.html') 

@login_required (login_url = "login")
def setting( request):
    return render (request, 'bank/setting.html') 

@login_required (login_url = "login")
def signin_successfully( request):
    return render (request, 'bank/signin-successfully.html') 

@login_required (login_url = "login")
def successfully_signin( request):
    return render (request, 'bank/successfully-signin.html') 

@login_required (login_url = "login")
def successfully_signup( request):
    return render (request, 'bank/successfully-signup.html') 

def terms_conditions( request):
    return render (request, 'bank/terms-conditions.html') 

@login_required (login_url = "login")
def transaction_history( request):
   # Assuming you have a way to determine the current user's account
    current_account = request.user.accountnumber  # Adjust this according to your actual model structure

    transactions = Transaction.objects.filter(From=current_account)

    context = {'transactions': transactions}
    return render (request, 'bank/transaction-history.html', context) 

@login_required (login_url = "login")
def transfer( request):
    transfer = request.user.transfer
    form = TransferForm (instance = transfer)

    if request.method == 'POST':
        form = TransferForm (request.POST, request.FILES, instance = transfer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'bank/transfer.html', context) 

@login_required (login_url = "login")
def withdraw( request):
    withdraw = request.user.withdraw
    form = WithdrawForm (instance = withdraw)

    if request.method == 'POST':
        form = WithdrawForm (request.POST, request.FILES, instance = withdraw)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'bank/withdraw.html', context) 

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'bank/change-password.html', {'form': form})


@user_not_authenticated
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("bank/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('login')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="bank/reset-password.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'bank/change-password.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("login")


@login_required (login_url = "login")
def pin(request):
    context = {}
    return render (request, "bank/pin.html", context)