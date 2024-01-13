class movie:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration
    
    def display(self):
        print(f'Name: {self.name} - Genre: {self.genre} - Duration(min): {self.duration} \n')

list_of_movies = []

while True:
    name = input("Enter movie's name: ")
    genre = input("Enter movie's genre: ")
    duration = input("Enter movie's duration(min): ")
    obj_movie = movie(name, genre, duration)
    list_of_movies.append(obj_movie)
    print("\nMovie's information added in the list:")
    print('........................................................\n')
    
    yes_no = input('Do you want to add another movie(y/n): ')
    if yes_no == 'n':
        print()
        break

print('........................................................\n')
for obj in list_of_movies:
    obj.display()
print('........................................................\n')
