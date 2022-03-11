class Movie: #Creating a parent class "Movie" with default attributes
    cast = ('')
    producer = ' '
    writer = ' '
    base_budget = 1,000,000

class Action(Movie): #Child class for "Action" genre of movies with unique attributes
    stunt_doubles = ('')
    exotic_locations = {''}
    safety_team = 'SafeSets'

class History(Movie): #Child class for "History" genre of movies with unique attributes
    historians = ('')
    archive = ' '
    scientists = ('')
    
    
    
    
