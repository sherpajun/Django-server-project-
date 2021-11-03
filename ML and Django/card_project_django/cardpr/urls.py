"""minipr2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from member import views as MemberView
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('select-data/', views.selectData, name='selectData'),

    # 그래프별 url 설정
    path('chartView/', MemberView.chartView, name='chartView'),
    path('chartView/gender/', MemberView.gender, name='genderChart'),
    path('chartView/car/', MemberView.car, name='carChart'),
    path('chartView/reality/', MemberView.reality, name='realityChart'),
    path('chartView/child_num/', MemberView.child_num, name='child_numChart'),
    path('chartView/edu_type/', MemberView.edu_type, name='edu_typeChart'),
    path('chartView/family_type/', MemberView.family_type, name='family_typeChart'),
    path('chartView/house_type/', MemberView.house_type, name='house_typeChart'),
    path('chartView/occyp_type/', MemberView.occyp_type, name='occyp_typeChart'),
    path('chartView/family_size/', MemberView.family_size, name='family_sizeChart'),
    path('chartView/Decile/', MemberView.Decile, name='DecileChart'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)