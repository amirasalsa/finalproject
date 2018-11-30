from django.urls import path
from .views import (
	MembershipSelectView, 
	PaymentView, 
	updateTransactionRecords,
	profile_view,
	cancelSubscription
	)

app_name = 'users'

urlpatterns = [
	path('', MembershipSelectView.as_view(), name='select'),
	path('payment/', PaymentView, name='payment'),
	path('update-transactions/<subscription_id>/', updateTransactionRecords, name='update-transactions'),
	path('profiles/', profile_view, name='profiles'),
    path('cancel/', cancelSubscription, name='cancel')
]