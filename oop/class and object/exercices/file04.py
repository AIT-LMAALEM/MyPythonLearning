class Movies:
    def __init__(self,title,director,release_year,genre):
        self.title=title
        self.director=director
        self.release_year=release_year
        self.genre=genre

    def display(self):
        print(f" Title: {self.title}")
        print(f" Director: {self.director}")
        print(f" Release Year: {self.release_year}")
        print(f" Genre: {self.genre} \n")
    
    def change_director(self,name):
        self.director=name

movie1 = Movies("Inception","Christopher Nolan",2010,"Sci-Fi")
movie2= Movies(" The Godfather","Francis ford Coppola",1972,"Crime")
movie3= Movies("Parasite","Bong Joon-ho",2019,"Thriller")

print(" ---------- Movies list -----------\n")
movie1.display()
movie2.display()
movie3.display()

print("Changing Movie Directors .......\n")
movie1.change_director("Shokry Sarhan")
movie2.change_director("Ahmed Mazhar")
movie3.change_director("Ismael Yassin")

movie1.display()
movie2.display()
movie3.display()









