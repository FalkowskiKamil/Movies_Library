import random
import datetime
catalog=list()
movies=list()
series_list=list()
day=datetime.date.today().strftime('%d.%m.%Y')

class film:
    def __init__(self, title, year, category, views):
        self.title=title
        self.year=year
        self.category=category
        self.views=views
        catalog.append(self)
        
    def __repr__(self):
        repr=f'Title: "{self.title}", Year of Production: {self.year}, Category: {self.category}, Views: {self.views}'
        return repr

    def __str__(self):
        return f'{self.title} {self.year}'

    def play(self):
        self.views=int(self.views)+1
        return self.views
    
    def views(self):
        return self.views
            
class series(film):
    def __init__(self, episode_number, serial_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number=episode_number
        self.serial_number=serial_number
    
    def __repr__(self):
        repr=super().__repr__()+f', Episode number: {self.episode_number}, Serial Number: {self.serial_number}'
        return repr

    def __str__(self):
        self.episode_number='{:02d}'.format(int(self.episode_number))
        self.serial_number="{:02d}".format(int(self.serial_number))
        return  f'{self.title} S{self.serial_number}E{self.episode_number}'

"""
simpson=film(title="Simpson", year="0", category="Comedy", views='5')
simpson=series(title="Simpson", year="0", category="Comedy", views='10', episode_number="11",serial_number="2")
pulp=film(title="Pulp Fiction", year="0", category="Action", views='4')
parasite=film(title="Parasite", year="0", category="Drama", views='3')
bb=series(title="Breaking Bad", year="0", category="Action", views='11', episode_number="4",serial_number="1")
"""

def get_movies():
    for x in catalog:
        if type(x)==film:
            movies.append(x)
        else:
            pass  
    movies_sorted=list()
    movies_sorted=sorted(movies, key=film.__str__)
    return movies_sorted
"""
print(get_movies())
"""
def get_series():
    for x in catalog:
        if type(x)==series:
            series_list.append(x)
        else:
            pass  
    series_sorted=list()
    series_sorted=sorted(series_list, key=series.__str__)
    return series_sorted
"""
print(get_series())
"""
def search(genre,title):
    if genre=='film':
        for x in get_movies():
            if title in x.__str__():
                return True
    if genre=='series':
        for x in get_series():
            if title in x.__str__():
                return True
"""
print(search("film","Pulp"))
print(search("series","Simpson"))
"""

def generate_views():
    element_number=random.randint(0,len(catalog)-1)
    views_number=random.randint(1,100)
    for x in range(views_number):
        catalog[element_number].play()

def multiple_generate():
    for x in range (10):
        generate_views()

def top_titles(number_of_titles, content_type=False):
    if content_type==False:
        catalog
        catalog_sorted=list()
        catalog_sorted=sorted(catalog, key=film.views(film), reverse=True)
        top_titles=catalog_sorted[:number_of_titles]
        return top_titles
    if content_type=="film":
        get_movies()
        movies_sorted=list()
        movies_sorted=sorted(movies, key=film.views(film), reverse=True)
        top_movies=movies_sorted[:number_of_titles]
        return top_movies
    if content_type=='series':
        get_series()
        series_sorted=list()
        series_sorted=sorted(series_list, key=series.views(series), reverse=True)
        top_series=series_sorted[:number_of_titles]
        return top_series

"""print(top_titles(2, content_type='series'))"""

"""
print(top_titles(3,content_type="film"))
"""

def full_serial(title, year, category, serial_number, number_of_episode):
    for x in range(int(number_of_episode)):
        series(title=title, year=year, category=category, serial_number=int(serial_number), episode_number=x+1, views=0)
"""   
full_serial(title="Simpson", year="0", category="Comedy", number_of_episode="5",serial_number="2")
full_serial(title="Simpson", year="0", category="Comedy", number_of_episode="13",serial_number="1")
"""

def count_of_episode(title):
    number=int()
    for x in get_series():
        if title in x.__str__():
            number=number+1
    return number
"""    
print(count_of_episode('Simpson'))
"""

def movie_library():
    print("Biblioteka filmów")
    full_serial(title="Simpson", year="0", category="Comedy", number_of_episode="2",serial_number="2")
    full_serial(title="Simpson", year="0", category="Comedy", number_of_episode="5",serial_number="1")
    for x in range(10):
        multiple_generate()
    print(f'Najpopularniejsze filmy i seriale dnia {day}')
    print(top_titles(3))
movie_library()