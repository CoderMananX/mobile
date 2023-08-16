from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path("", views.index, name="index.html"),
   path("basic", views.basic, name="basic"),
   path("about", views.about, name="about.html"),
   path("product", views.product, name="product.html"),
   path("contact", views.contact, name="contact.html"),
   path("viewdata", views.viewdata, name="viewdata"),
   path("checkuser", views.checklogin, name="checkuser"),
   path("logout", views.logout, name="logout"),
   path("cart", views.Cart, name="Cart"),
   path("payment", views.payment, name="payment"),
   path("verifypayment", views.verifypayment, name="verifypayment"),
   path("order-complete", views.OrderComplete, name="OrderComplete"),
   path("addtocart", views.addtocart, name="addtocart"),
   path("orderplaced", views.orderplaced, name="orderplaced"),
   path("submitreview", views.SubmitReview, name="SubmitReview"),
   path("SubmitContact", views.SubmitContact, name="SubmitContact"),
   path("searchresult", views.SearchResult, name="SearchResult"),
   path("forgotpassword", views.forgotpassword, name="forgotpassword"),
   path("yourorders", views.yourorders, name="yourorders.html"),
   path("completeprofile", views.completeprofile, name="completeprofile"),
   path("yourprofile", views.yourprofile, name="yourprofile"),
   path("single/<int:myid>", views.productView, name="ProductDetail"),
   path("yourordersingle/<int:yoid>", views.yourordersingle, name="yourordersingle"),
   path("cancelorder/<int:coid>", views.cancelorder, name="cancelorder"),
   path("categorywiseproduct/<int:pcid>", views.categorywiseproduct, name="categorywiseproduct"),
   path("removeitem/<int:did>", views.RemoveFromCart, name="RemoveFromCart"),
   path("success",views.success,name="success"),
]