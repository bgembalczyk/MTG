import ssl
import certifi

# Wymuszenie użycia certyfikatów z certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(
    cafile=certifi.where()
)

from mtgsdk import Card

if __name__ == "__main__":
    # Get a card by its name
    cards = Card.where(set="M21").all()
    for card in cards:
        print(card.name)
