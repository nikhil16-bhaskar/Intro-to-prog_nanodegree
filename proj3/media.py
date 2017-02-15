import webbrowser #it imports the file webbrowser from standard library of python.

class Movie():#this is a class named Movie which has two procedures/functons named __init__ and show_trailer
    def __init__(self,movie_title,movie_year,poster_image,trailer_youtube):#this function takes 5 arguments in which self is instance of Movie class 
        self.title=movie_title#value of movie_title is assigned to self.title
        self.year=movie_year#value of movie_year is assigned to self.year
        self.poster_image_url=poster_image#value of poster_image is assigned to self.poster_image_url
        self.trailer_youtube_url=trailer_youtube#value of trailer_youtube is assigned to self.trailer_youtube_url

    def show_trailer(self):#this function passes one argument called self which an instance of class Movie  
        webbrowser.open(self.trailer_youtube_url)#it will oen web browser with the selected you tube video
