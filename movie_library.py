import json


class MovieNotFoundError(Exception):
    '''
    Esercizio 18: Creo un'eccezione personalizzata per
    segnalare che un film non è stato trovato, da inserire nei
    metodi 'remove_movie' e 'update_movie'.
    '''

    def __init__(self):
        super().__init__("Movie was not found")


class MovieLibrary:
    '''
    Creo una classe che gestisce una collezione di film costituita dal
    file movies.json.
    '''

    def __init__(self, json_file):
        '''
        Inizializza una nuova istanza della classe MovieLibrary.

        :param json_file: Percorso assoluto del file JSON che contiene
        la collezione dei film.
        '''
        self.json_file = json_file
        self.movies = []

        # Assegna all'attributo "movies" i dati all'interno del file JSON
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.movies = json.load(file)
        # Esericizio 17: sollevo l'eccezione FileNotFoundError se nel
        # percorso 'json_file' non viene trovato alcun file.
        except FileNotFoundError:
            print(f"File not found: {self.json_file}")

    def __update_json_file(self):
        '''
        Creo un metodo privato per aggiornare il file JSON ogni volta che
        vengono effettuate modifiche alla collezione di film.
        '''
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.movies, file)

    def get_movies(self) -> list:
        '''
        Esercizio 1: Creo un metodo che restituisce l'intera
        collezione dei film.
        '''
        return self.movies

    def add_movie(self, title, director, year, genres):
        '''
        Esercizio 2: Creo un metodo che aggiunge un film alla collezione
        e aggiorna il file JSON.

        :param title: Titolo del film (stringa).
        :param director: Regista del film (stringa).
        :param year: Anno di uscita del film (intero).
        :param genres: Generi del film (lista di stringhe).
        '''
        # Controllo se il film è già esistente
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return "Il film è già esistente all'interno della libreria"
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genre": genres
        }
        self.movies.append(new_movie)
        self.__update_json_file()
        return {f"Il film {title} è stato aggiunto."}

    def remove_movie(self, title):
        '''
        Esercizio 3: Creo un metodo che rimuove un film dalla collezione
        che ha titolo corrispondente al parametro "title" (NON case sensitive),
        e aggiorna il file JSON.
        '''
        if title not in self.movies:
            raise MovieNotFoundError
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return (f"Il film {title} è stato rimosso.")

    def update_movie(self, title, director=None, year=None, genres=None):
        '''
        Esercizio 4: Creo un metodo per ricercare un film nella collezione
        che ha titolo corrispondente al parametro "title" (NON case sensitive),
        per poi poterne modificare i parametri specificati.
        '''
        if title not in self.movies:
            raise MovieNotFoundError
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director is not None:
                    self.director = director
                if year is not None:
                    self.year = year
                if genres is not None:
                    self.genres = genres
                self.__update_json_file()
                return (f"Il film {title} è stato modificato.")
            else:
                return ("Nessun film trovato con questo titolo, ritenta.")

    def get_movies_title(self) -> list:
        '''
        Esercizio 5: Creo un metodo che restituisce una lista
        contenente tutti i titoli dei film nella collezione.
        '''
        if not self.movies:
            return "The movie library is empty."
        return [movie["title"] for movie in self.movies]

    def count_movies(self) -> int:
        '''
        Esercizio 6: Creo un metodo che restituisce il numero totale
        dei film nella collezione.
        '''
        return len(self.movies)

    def get_movie_by_title(self, title) -> dict:
        '''
        Esercizio 7: Creo un metodo che restituisce il film
        che ha titolo corrispondente (NON case sensitive) a "title".
        '''
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie

    def get_movies_by_title_substring(self, substring) -> list:
        '''
        Esercizio 8: Creo un metodo che restituisce una lista di
        tutti i film che contengono, nel titolo,
        una sottostringa corrispondente (case sensitive) a "substring".
        '''
        return [movie for movie in self.movies if substring in movie["title"]]

    def get_movies_by_year(self, year) -> list:
        '''
        Esercizio 9: Creo un metodo che restituisce una lista di
        tutti i film con anno corrispondente a "year".
        '''
        return [movie for movie in self.movies if year == movie["year"]]

    def count_movies_by_director(self, director) -> int:
        '''
        Esercizio 10: Creo un metodo che restituisce un numero intero
        che rappresenta, quanti film del director scelto sono presenti nella
        collezione (NON case sensitive).
        '''
        return sum(1 for movie in self.movies if
                   movie["director"].lower() == director.lower())

    def get_movies_by_genre(self, genre) -> list:
        '''
        Esercizio 11: Creo un metodo che restituisce una lista di
        tutti i film che hanno genere corrispondente a
        "genre" (NON case sensitive).
        '''
        return [movie for movie in self.movies if genre.lower() in
                (genre.lower() for genre in movie["genres"])]

    def get_oldest_movie_title(self) -> str:
        '''
        Esercizio 12: Creo un metodo che restituisce il titolo del
        film più datato della collezione.
        '''
        if not self.movies:
            return "The movie library is empty."
        oldest_movie = min(self.movies, key=lambda movie: movie["year"])
        return oldest_movie["title"]

    def get_average_release_year(self) -> float:
        '''
        Esercizio 13: Creo un metodo che restituisce
        un float rappresentante la media aritmetica degli anni di pubblicazione
        dei film della collezione.
        '''
        if not self.movies:
            return "The movie library is empty."
        total_year = sum(movie["year"] for movie in self.movies)
        return total_year / len(self.movies)

    def get_longest_title(self) -> str:
        '''
        Esercizio 14: Creo un metodo che restituisce il film con
        il titolo più lungo della collezione.
        '''
        longest_movie_title = max(self.movies,
                                  key=lambda movie: len(movie["title"]))
        return longest_movie_title["title"]

    def get_title_between_years(self, start_year, end_year) -> list:
        '''
        Esercizio 15: Creo un metodo che restituisce una lista contenente
        i titoli dei film pubblicati dall’anno "start_year" fino all’anno
        "end_year" (estremi compresi).
        '''
        if not self.movies:
            return "The movie library is empty."
        return [movie["title"] for movie in self.movies if
                start_year <= movie["year"] <= end_year]

    def get_most_common_year(self) -> int:
        '''
        Esercizio 16: Creo un metodo che restituisce l’anno che
        si ripete più spesso fra i film della collezione.
        '''
        if not self.movies:
            return "The movie library is empty."
        year_counts = {}
        for movie in self.movies:
            year = movie["year"]
            if year in year_counts:
                year_counts[year] += 1
            else:
                year_counts[year] = 1

        most_common_year = max(year_counts, key=year_counts.get)
        return most_common_year
