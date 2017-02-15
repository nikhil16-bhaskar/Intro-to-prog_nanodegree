
import fresh_tomatoes#it will import fresh tomatoes in this program so that it can be used
import media# media file is imported to this program



ms_dhoni=media.Movie("M.S DHONI","2016","https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg"," https://www.youtube.com/watch?v=6L6XqWoS8tw")#ms_dhoni has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 


dangal=media.Movie("DANGAL","2016","https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg","https://www.youtube.com/watch?v=x_7YlGv9u1g")#dangal has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 



captain_america=media.Movie("CAPTAIN AMERICA","2011","https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg","https://www.youtube.com/watch?v=JerVrbLldXw")#captain_america has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 


kungfu_panda=media.Movie("KUNGFU PANDA","2008","https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg","https://www.youtube.com/watch?v=PXi3Mv6KMzY")#kungfu_panda has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 



never_back_down=media.Movie("NEVER BACK DOWN","2008","https://upload.wikimedia.org/wikipedia/en/3/39/Never_back_down.jpg","https://www.youtube.com/watch?v=s8aGqjNM0k4")#never_back_down has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 


wolf_of_wall_street=media.Movie("WOLF OF WALL STREET","2014","https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg","https://www.youtube.com/watch?v=idAVRvQeYAE")#wolf_of_wall_street has the arguments as title of movie,year of release,poster of movie and youtube link to play movie's trailer 


movies=[ms_dhoni,dangal,captain_america,never_back_down,kungfu_panda,wolf_of_wall_street]#movies contains the list of all the name of movies
fresh_tomatoes.open_movies_page(movies)#it will open an html page on which the movies with poster,title,storyline and youtube trailer will be available
