"""
We need webbrowser imported because webbrowser is
used in the instance method.
"""


import webbrowser

"""
We define the Movie class which acts as a blueprint.
It contains both data and a method.
"""


class Movie():
    """
    This class (Movie) provides a way to store movie
    related information.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
