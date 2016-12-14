from django.conf.urls import url


from views import ItemCreationView,ItemEditView,ItemDetailView,UserLogView
from views import VariantCreationView,VariantDetailView,VariantEditView,HomePage
from views import RegistrationView,LoginView,LogoutView

urlpatterns = [
    url(r'^$', HomePage.as_view(), name="homepage"),
    url(r'^user-log/$', UserLogView.as_view(), name="log"),
    url(r'^create-item/', ItemCreationView.as_view(), name="create-item"),
    url(r'^edit-item/(?P<pk>\w{0,50})/', ItemEditView.as_view(), name="edit-item"),
    url(r'^create-variant/', VariantCreationView.as_view(), name="create-variant"),
    url(r'^view-variant/(?P<pk>\w{0,50})/', VariantDetailView.as_view(), name="view-variant"),
    url(r'^view-item/(?P<pk>\w{0,50})/', ItemDetailView.as_view(), name="view-variant"),
    url(r'^edit-variant/(?P<pk>\w{0,50})/', VariantEditView.as_view(), name="edit-variant"),
    url(r'^register/', RegistrationView.as_view(), name="register-user"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
]
