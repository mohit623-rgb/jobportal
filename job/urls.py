from django.urls import path,include
from .import views
from .views import contact_view
from .views import signup_view,register_view

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("about/",views.About,name="about"),
    path("joblist/",views.Joblist,name="joblist"),
    path("category/",views.Category,name="category"),
    path("testimonial/",views.Testimonial,name="testimonial"),
    path("login/", signup_view, name="login"),
    path("register/",views.register_view,name="register"),
    path("contact/", contact_view, name="contact"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.Otpverify,name="otp"),
    


]