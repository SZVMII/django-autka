from django.db.models import ExpressionWrapper, FloatField, F
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from .models import Part, Favorite, Comment, Rating
from .serializer import PartSerializer, PartLocationFilterSerializer, FavoriteSerializer, CommentSerializer, RatingSerializer
from samochod.filters import AutoFilter

"""Formularz tworzenia"""
class CreateView(generics.CreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_added=self.request.user, )

"""Wypisywanie zawartosci tabeli"""
class PartList(generics.ListAPIView):
    queryset = Part.objects.filter(status='zaakceptowane')
    serializer_class = PartSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    #filter_class = AutoFilter
    search_fields = ('model', 'mark')

    def display(self):
        return super().get_queryset()

    def get_queryset(self):
        queryset = super().get_queryset()
        print(str(queryset.query))
        return queryset

"""Dodawanie do ulubionych"""
class FavoriteAdd(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""Wyświetlanie ulubionych"""
class FavoriteListCreateView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""Dodawanie komentarzy"""
class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_added=self.request.user, )

"""Wyswietlanie komentearzy"""
class CommentListVeiw(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def display(self):
        return super().get_queryset()

"""Wyswietlanie komentarzy dla danego pola"""
class CommentSoloList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(part=self.kwargs.get('pk'))

"""Dodanie oceny"""
class RatingAdd(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""Wyswietlanie ocen"""
class RatingList(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def display(self):
        return super().get_queryset()

"""Wyswietlanie ocen dla danego pola"""
class RatingSoloList(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(part=self.kwargs.get('pk'))
