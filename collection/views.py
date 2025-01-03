from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deck, Card
from .forms import DeckForm, CardForm

@login_required
def edit_collection(request):
    decks = Deck.objects.filter(user=request.user)
    context = {'decks': decks}
    return render(request, 'collection/edit_collection.html', context)

@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('edit_collection')  # Redirect to the edit collection page
    else:
        form = DeckForm()
    return render(request, 'collection/create_deck.html', {'form': form})


class EditDeckView(LoginRequiredMixin, UpdateView):
    model = Deck
    form_class = DeckForm
    template_name = 'collection/edit_deck.html'
    success_url = reverse_lazy('edit_collection')  # Redirect to the edit collection page


class DeleteDeckView(LoginRequiredMixin, DeleteView):
    model = Deck
    template_name = 'collection/delete_deck.html'
    success_url = reverse_lazy('edit_collection')  # Redirect to the edit collection page


@login_required
def add_card(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id, user=request.user)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            deck.card_set.add(card)  # Add the card to the deck
            return redirect('edit_collection')  # Redirect to the edit collection page
    else:
        form = CardForm()
    return render(request, 'collection/add_card.html', {'form': form, 'deck': deck})


class EditCardView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'collection/edit_card.html'
    success_url = reverse_lazy('edit_collection')  # Redirect to the edit collection page


class DeleteCardView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = 'collection/delete_card.html'
    success_url = reverse_lazy('edit_collection')  # Redirect to the edit collection page

