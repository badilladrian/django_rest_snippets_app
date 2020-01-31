from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import extremeview

#The views, apiview, mixin, & extremeview were created
#to explore the different types of views usages

#ONLY THE EXTREMEVIEW SHOULD BE CONSIDER


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', extremeview.SnippetViewSet)
router.register(r'users', extremeview.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

"""from snippets.extremeview import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])"""


"""from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

paths = [ #Views to our list and individual details
    #path('snippets/', views.snippet_list), #using views/templates
    #path('snippets/<int:pk>/', views.snippet_detail),
    #path('snippetsapp/', apiview.snippet_list), #using rest api_view
    #path('snippetsapp/<int:pk>/', apiview.snippet_detail),
    #path('snippetsclass/', viewclass.SnippetList.as_view()), #Using class based Views ApiView
    #path('snippetsclass/<int:pk>/', viewclass.SnippetDetail.as_view()),
    path('snippets/', extremeview.SnippetList.as_view()), #using APIEView Class
    path('snippets/<int:pk>/', extremeview.SnippetDetail.as_view()),
    #for users
    path('users/', extremeview.UserList.as_view()),
    path('users/<int:pk>/', extremeview.UserDetail.as_view()),
    path('snippets/<int:pk>/highlight/', extremeview.SnippetHighlight.as_view()),
    path('', extremeview.api_root),
]"""

"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import extremeview

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', extremeview.api_root),
    path('snippets/',
        extremeview.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        extremeview.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        extremeview.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        extremeview.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        extremeview.UserDetail.as_view(),
        name='user-detail')
])"""



