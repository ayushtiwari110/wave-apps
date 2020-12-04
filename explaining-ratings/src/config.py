import pandas as pd


class Configuration:
    """
    Configuration file for Explain Ratings
    """

    def __init__(self):
        self.color = "#00A8E0"
        self.image_path = "static/icon.png"
        self.title = "Hotel Reviews"
        self.subtitle = "Explains the hotel reviews"
        self.icon = "ReviewSolid"

        self.training_path = "data/Hotel_Reviews.csv"
        self.default_model = "explain_rating_model"

        self.dataset = None

        self.boxes = {
            'banner': '1 1 12 1',
            'left_panel': '1 2 3 9',
            'middle_panel': '4 2 4 9',
            'right_panel': '8 2 5 9',
        }

    def get_dataset(self, refresh=False):
        if refresh or self.dataset is None:
            df = pd.read_csv(self.training_path).head(40)
            df['reviews.rating'] = df['reviews.rating'].astype(int)
            self.dataset = df

        return self.dataset
