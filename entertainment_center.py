import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story','A story of a boy and his toys that come to life','https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg','https://www.youtube.com/watch?v=KYz2wyBy3kc')

#print toy_story.storyline
avatar= media.Movie('Avatar','A marine on an alien planet','https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg','https://www.youtube.com/watch?v=d1_JBMrrYw8')
#print avatar.storyline
#avatar.show_trailer()
fast_and_furious=media.Movie('Fast and Furious 7','Seeking the revenge','https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg','https://www.youtube.com/watch?v=yISKeT6sDOg')
#fast_and_furious.show_trailer()
chennai_express=media.Movie('Chennai Express','A journey to Chennai','https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Chennai_Express.jpg/220px-Chennai_Express.jpg','https://www.youtube.com/watch?v=rARol7Dk2zo')
the_karate_kid=media.Movie('The Karate Kid','Inspirational Story of a kid to learn karate','https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Karate_kid_ver2.jpg/220px-Karate_kid_ver2.jpg','https://www.youtube.com/watch?v=2SmmxvHLsKk')
never_back_down=media.Movie('Never Back Down','A journey of a fighter','https://upload.wikimedia.org/wikipedia/en/thumb/3/39/Never_back_down.jpg/220px-Never_back_down.jpg','https://www.youtube.com/watch?v=2tc-RPjZRm8')
movies=[toy_story, avatar, fast_and_furious, chennai_express, the_karate_kid, never_back_down]
fresh_tomatoes.open_movies_page(movies)
