import random



suite_deck = ["clubs", "diamonds", "hearts", "spades"]
face_deck = ["2", "3", "4", "5", "6","7", "8", "9", "10", "J", "Q", "K", "A"]

random_suite = random.choice(suite_deck)
random_face = random.choice(face_deck)

print("your randomly generated card is", random_face,"of", random_suite)