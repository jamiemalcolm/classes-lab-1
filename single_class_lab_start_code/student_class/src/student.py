class Student:
    def __init__(self, name, cohort, favorite_laguage, commute_time_mins):
        self.name = name
        self.cohort = cohort
        self.fav_language = favorite_laguage
        self.commute = commute_time_mins

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self):
        return "I love " + self.fav_language


# add morew properties and test for them

    def get_commute_time(self, name):
        if self.name == name:
            return "It takes me " + str(self.commute) + " minutes to get to CodeClan"
