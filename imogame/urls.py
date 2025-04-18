from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('test',views.test,name='test'),
    path('login',views.userlogin,name='login'),
    path('logout',views.userlogout,name='logout'),
    path('sign-up',views.signup,name='signup'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('view-kids',views.view_kids,name='view-kids'),
    path('select-kid',views.selkid,name='select-kid'),
    path('select-kid2',views.selkid2,name='select-kid2'),
    path('training/<int:id>',views.trainkid,name='training-kid'),
    path('select-level/<int:id>',views.gamelevel,name='select-level'),
    path('level1/<int:id>',views.level1,name='level1'),
    path('level2/<int:id>',views.level2,name='level2'),
    path('level3/<int:id>',views.level3,name='level3'),
    path('l1-accuracy',views.level1acc,name='l1acc'),
    path('l2-accuracy',views.level2acc,name='l2acc'),
    path('l3-accuracy',views.level3acc,name='l3acc'),
    path('view-status/<int:id>',views.status_view,name='view-status'),
    path('reset',views.reset,name='reset'),
    path('vids-class',views.vids_class,name='vids-class'),
]