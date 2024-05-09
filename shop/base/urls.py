from django.urls import path

from .views import AuthView, MarketView, UserView

urlpatterns = [
    path('auth/signup', AuthView.signUp),
    path('auth/signin', AuthView.signIn),
    path('auth/token/<str:token>', AuthView.decodeUserAuthToken),
    path('user/create', UserView.createUser),
    path('user/me/<str:token>', UserView.getMe),
    path('user/market/<int:marketPk>', UserView.getByMarketId),
    path('market/create', MarketView.createMarket),
    path('market/<int:pk>', MarketView.getMarketById),
    path('market/user/<str:token>', MarketView.getUserMarkets),
]
