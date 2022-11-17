from django.urls import path
from .views import notaEntradaList, notaEntradaNew, notaEntradaUpdate, notaEntradaDelete

app_name = 'notaEntrada'

urlpatterns = [
    path('notaEntradaList/', notaEntradaList, name='notaEntradaList'),
    path('notaEntradaNew/', notaEntradaNew, name='notaEntradaNew'),
    path('notaEntradaUpdate/<int:pk>/', notaEntradaUpdate, name='notaEntradaUpdate'),
    path('notaEntradaDelete/<int:pk>/', notaEntradaDelete, name='notaEntradaDelete')
]