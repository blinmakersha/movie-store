from app import app, db
from models import Movies

movies = [
    {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
        "genre": "Drama",
        "kind": "Movie",
        "duration": 142,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "poster_url": "https://theposterdb.com/api/assets/20890",
        "trailer_url": "https://www.youtube.com/embed/PLl99DlL6b4?si=1RNMx7V92qsdhqgv",
        "price": 9.99
    },
    {
        "title": "The Matrix",
        "director": "The Wachowski Brothers",
        "year": 1999,
        "genre": "Action, Sci-Fi",
        "kind": "Movie",
        "duration": 136,
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "poster_url": "https://theposterdb.com/api/assets/16566",
        "trailer_url": "https://www.youtube.com/embed/vKQi3bBA1y8?si=mVPfwqmnL2v9NscU",
        "price": 9.99
    },
    {
        "title": "Star Wars: Episode V - The Empire Strikes Back",
        "director": "Irvin Kershner",
        "year": 1980,
        "genre": "Action, Adventure, Fantasy",
        "kind": "Movie",
        "duration": 124,
        "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy.",
        "poster_url": "https://theposterdb.com/api/assets/4450",
        "trailer_url": "https://www.youtube.com/embed/JNwNXF9Y6kY?si=NOrZx5kkmIo9p-82",
        "price": 9.99
    },
    {
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "year": 2014,
        "genre": "Adventure, Drama, Sci-Fi",
        "kind": "Movie",
        "duration": 169,
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "poster_url": "https://theposterdb.com/api/assets/9308",
        "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E?si=91yt8Qlyfvw30Cm4",
        "price": 9.99
    },
    {
        "title": "Avatar: The Way of Water",
        "director": "James Cameron",
        "year": 2022,
        "genre": "Action, Adventure, Fantasy, Sci-Fi",
        "kind": "Movie",
        "duration": 162,
        "description": "Jake Sully, a paralyzed former Marine, is recruited by a company to be a body for an Avatar AI, which is used to control a remotely operated vehicle to extract a valuable mineral from an alien planet. However, when the Avatar is attacked, Jake takes control and becomes stranded on the planet. As Jake explores the planet and its people, he uncovers a conspiracy that threatens the entire alien civilization.",
        "poster_url": "https://theposterdb.com/api/assets/303877",
        "trailer_url": "https://www.youtube.com/embed/a8Gx8wiNbs8?si=G0H29GEx-eM9_vtO",
        "price": 9.99
    },
    {
        "title": "Onward",
        "director": "Dan Scanlon",
        "year": 2020,
        "genre": "Animation, Adventure, Comedy, Family, Fantasy",
        "kind": "Cartoon",
        "duration": 103,
        "description": "Two elf brothers embark on an extraordinary journey to discover if there is still a little magic left out there.",
        "poster_url": "https://theposterdb.com/api/assets/57201",
        "trailer_url": "https://www.youtube.com/embed/x8DKg_fsacM?si=HtPRA2VukX4FOatF",
        "price": 7.99
    },
    {
        "title": "Spider-Man: Across the Spider-Verse",
        "director": "Joaquim Dos Santos",
        "year": 2023,
        "genre": "Animation, Action, Adventure",
        "kind": "Cartoon",
        "duration": 120,
        "description": "After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse’s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.",
        "poster_url": "https://theposterdb.com/api/assets/369437",
        "trailer_url": "https://www.youtube.com/embed/cqGjhVJWtEg?si=1pNwsJ4oYO9oDfuN",
        "price": 7.99
    },
    {
        "title": "Buzz Lightyear",
        "director": "Andrew Stanton",
        "year": 2022,
        "genre": "Animation, Adventure, Comedy, Family, Sci-Fi",
        "kind": "Cartoon",
        "duration": 102,
        "description": "Buzz Lightyear, a space-faring toy, embarks on an interstellar journey to Earth, where he must learn to become a hero and save the world from an intergalactic threat.",
        "poster_url": "https://theposterdb.com/api/assets/242268",
        "trailer_url": "https://www.youtube.com/embed/BwZs3H_UN3k?si=0cH3PVYoN6r2dTZp",
        "price": 7.99
    },
    {
        "title": "Turning Red",
        "director": "Domee Shi",
        "year": 2021,
        "genre": "Animation, Adventure, Comedy, Family",
        "kind": "Cartoon",
        "duration": 95,
        "description": "Thirteen-year-old Mei is experiencing the awkwardness of being a teenager with a twist – when she gets too excited, she transforms into a giant red panda.",
        "poster_url": "https://theposterdb.com/api/assets/281639",
        "trailer_url": "https://www.youtube.com/embed/XdKzUbAiswE?si=Ac0Od9fj-JXJNc16",
        "price": 7.99
    },
    {
        "title": "Soul",
        "director": "Pete Docter and Kemp Powers",
        "year": 2020,
        "genre": "Animation, Drama, Fantasy, Music",
        "kind": "Cartoon",
        "duration": 100,
        "description": "After landing the gig of his dreams, a jazz musician finds himself trapped in a strange land between Earth and the afterlife. When he is unexpectedly chosen to play a crucial role in the lives of the inhabitants, he must journey to find his way back home.",
        "poster_url": "https://theposterdb.com/api/assets/111173",
        "trailer_url": "https://www.youtube.com/embed/xOsLIiBStEs?si=SnOLCncqNzT3v2Rk",
        "price": 7.99
    },
    {
        "title": "Loki",
        "director": "Dan Deleeuw",
        "year": 2021,
        "genre": "Action, Adventure, Fantasy",
        "kind": "TV Series",
                "duration": 40,
                "description": "The mercurial villain Loki resumes his role as the God of Mischief in a new series that takes place after the events of “Avengers: Endgame.”",
                "poster_url": "https://theposterdb.com/api/assets/157410",
                "trailer_url": "https://www.youtube.com/embed/nW948Va-l10?si=tcLUhnEuwanJ8Hz-",
                "price": 19.99
    },
    {
        "title": "Supernatural",
        "director": "Jensen Ackles",
        "year": 2005,
        "genre": "Drama, Fantasy, Horror, Mystery, Thriller",
        "kind": "TV Series",
                "duration": 60,
                "description": "Two brothers follow their father's footsteps as hunters, fighting evil supernatural beings of many kinds, including monsters, demons and gods that roam the earth.",
                "poster_url": "https://theposterdb.com/api/assets/274004",
                "trailer_url": "https://www.youtube.com/embed/HPKiZaEzMko?si=-cnbkdvRTrRIElFG",
                "price": 19.99
    },
    {
        "title": "H2O: Just Add Water",
        "director": "Jonathan M. Shiff",
        "year": 2006,
        "genre": "Adventure, Comedy, Drama, Family, Fantasy",
        "kind": "TV Series",
                "duration": 30,
                "description": "A group of five ordinary teenagers discover they have special abilities when they come into contact with a mysterious boy in a comic book.",
                "poster_url": "https://theposterdb.com/api/assets/96620",
                "trailer_url": "https://www.youtube.com/embed/wqHED34TcwU?si=JsTzQFbbsKf0y3eg",
                "price": 19.99
    },
    {
        "title": "Gossip Girl",
        "director": "Mark Piznarski",
        "year": 2007,
        "genre": "Drama, Romance",
        "kind": "TV Series",
                "duration": 40,
                "description": "Privileged teenager Jordyn Jones and her friends are depicted as they navigate the treacherous world of upper-class Manhattan teen life, school, love and betrayal.",
                "poster_url": "https://theposterdb.com/api/assets/390553",
                "trailer_url": "https://www.youtube.com/embed/eCg1RN-dyQk?si=26vdKU2JBkBYUvzQ",
                "price": 19.99
    },
    {
        "title": "Superman & Lois",
        "director": "Todd Helbing",
        "year": 2021,
        "genre": "Action, Adventure, Drama",
        "kind": "TV Series",
                "duration": 40,
                "description": "The world's most famous superhero and comic books' most famous journalist face the pressures and complexities that come with balancing work, justice, and parenthood in today's society.",
                "poster_url": "https://theposterdb.com/api/assets/134550",
                "trailer_url": "https://www.youtube.com/embed/SJPJPUpNvDw?si=slIToSe3_XB2LIoB",
                "price": 19.99
    },
    {
        "title": "John Wick",
        "director": "Chad Stahelski",
        "year": 2014,
        "genre": "Action, Mystery, Thriller",
        "kind": "Movie",
                "duration": 101,
                "description": "Keanu Reeves stars as John Wick, a legendary hitman who comes out of retirement to seek revenge against the men who killed his puppy, a final gift from his recently deceased wife.",
                "poster_url": "https://theposterdb.com/api/assets/17551",
                "trailer_url": "https://www.youtube.com/embed/C0BMx-qxsP4?si=AYK56ly0QnVWhskS",
                "price": 9.99
    },
]

with app.app_context():
    for movie in movies:
        new_movie = Movies(**movie)
        db.session.add(new_movie)
        db.session.commit()
