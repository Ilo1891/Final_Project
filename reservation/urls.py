from django.urls import path
from reservation.apps import ReservationConfig
from reservation.views import TableTemplateView, TableListView, TableDetailView, TableCreateView, TableDeleteView, \
    TableUpdateView, AboutRestoTemplateView, ReservationCreateView, ContactsTemplateView

app_name = ReservationConfig.name

urlpatterns = [
    path('', TableTemplateView.as_view(), name='base'),
    path('table_list/', TableListView.as_view(), name='table_list'),
    path('reservation/', ReservationCreateView.as_view(), name='reservation'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('about_resto/', AboutRestoTemplateView.as_view(), name='about_resto'),
    path('create/', TableCreateView.as_view(), name='create'),
    path('<int:pk>/', TableDetailView.as_view(), name='view'),
    path('<int:pk>/update/', TableUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', TableDeleteView.as_view(), name='delete'),
]