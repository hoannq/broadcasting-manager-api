"""broadcasting_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^users/', include('one_users.urls')),
    url(r'^auth/', include('one_auth.urls')),
    url(r'^me/', include('one_users.urls_me')),
    url(r'^televisions/', include('televisions.urls')),
    url(r'^areas/', include('areas.urls')),
    url(r'^basestations/', include('basestations.urls')),
    url(r'^broadcasts/', include('broadcasts.urls')),
    url(r'^broadcasting-status/', include('broadcastingstatus.urls')),
    url(r'^time-ranges/', include('timeranges.urls')),
    url(r'^contracts/', include('contracts.urls')),
    url(r'^machine-locations/', include('machinelocations.urls')),
    url(r'^unit-prices/', include('unitprices.urls')),

]
