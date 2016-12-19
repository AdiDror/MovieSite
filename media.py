import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, 
    			 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ Function to bring up the trailer of a specific movie when the user
     selects it. Trailer will get the URL from Entertainemnt_Center"""
     
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
