import random

class Review:
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text
    
    def print_review(self):
        print (f"Rating:", {self.rating})
        print (f"Review:", {self.text})
        print()

class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []
    
    def add_review (self, review):
        self.reviews.append(review)

    def average_rating(self):
        if not self.reviews:
            return 0
        
        total = 0
        for r in self.reviews:
            total =+ r.rating
        
        return total / len(self.reviews)

    def show_reviews(self):
        print (f"Reviews for", {self.title})
        print()

        for r in self.reviews:
            r.print_review()

    def best_review (self):
        best = self.reviews [0]
        
        for r in self.reviews:
            if r.rating > best.rating:
                best = r
            elif r.rating == best.rating:
                if random.randint(0,1) == 1:
                    best = r

        return best

    def worst_review(self):
        worst = self.reviews[0]

        for r in self.reviews:
            if r.rating < worst.rating:
                worst = r
            elif r.rating == worst.rating:
                if random.randint(0,1) == 1:
                    worst = r
        return worst

movie = Movie("Batman: The Dark Knight")

r1 = Review (5, "Best move of all time!")
r2 = Review (4, "My favorit movie.")
r3 = Review (5, "Loved this movie!")
r4 = Review (3, "Not a big superhero movie fan, but it was good.")

movie.add_review(r1)
movie.add_review(r2)
movie.add_review(r3)
movie.add_review(r4)

movie.show_reviews()

print("Average Rating:", movie.average_rating())

print("Best Review:" )
movie.best_review().print_review()

print("Worst Review:" )
movie.worst_review().print_review()
