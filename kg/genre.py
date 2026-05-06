from rdflib import Graph, URIRef, Namespace, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL, XSD
import os


class Genre:
    def __init__(self):
        self.g = Graph()
        self.n = Namespace('https://koncordantlab.com/TTEXTS/')
        self.genre = Namespace('https://koncordantlab.com/TTEXTS/genre/')

        self.g.bind('TTEXTS',self.n)
        self.g.bind('genre', self.genre)

        self.Genre = URIRef(self.n.Genre)
        self.Fiction = URIRef(self.genre.Fiction)
        self.Historical = URIRef(self.genre.Historical)
        self.Realistic = URIRef(self.genre.Realistic)
        self.Autobiographical_Fiction = URIRef(self.genre.Autobiographical_Fiction)
        self.Psychological = URIRef(self.genre.Psychological)
        self.Dystopian = URIRef(self.genre.Dystopian)
        self.Adventure = URIRef(self.genre.Adventure)
        self.Gothic = URIRef(self.genre.Gothic)
        self.Dark_Romanticism = URIRef(self.genre.Dark_Romanticism)
        self.Frame_Narrative = URIRef(self.genre.Frame_Narrative)
        self.Satire = URIRef(self.genre.Satire)
        self.Fable = URIRef(self.genre.Fable)
        self.Bildungsroman = URIRef(self.genre.Bildungsroman)
        self.Vignette = URIRef(self.genre.Vignette)
        self.Science = URIRef(self.genre.Science)
        self.Crime = URIRef(self.genre.Crime)
        self.Horror = URIRef(self.genre.Horror)
        self.Fantasy = URIRef(self.genre.Fantasy)
        self.Portal_Fantasy = URIRef(self.genre.Portal_Fantasy)
        self.Religious = URIRef(self.genre.Religious)
        self.Humorous = URIRef(self.genre.Humorous)
        self.Classic = URIRef(self.genre.Classic)
        self.Drama = URIRef(self.genre.Drama)
        self.Realistic_Drama = URIRef(self.genre.Realistic_Drama)
        self.Poetry = URIRef(self.genre.Poetry)
        self.Lyric = URIRef(self.genre.Lyric)
        self.Narrative_Poetry = URIRef(self.genre.Narrative_Poetry)
        self.Epic = URIRef(self.genre.Epic)
        self.Nonfiction_Genre = URIRef(self.genre.Nonfiction)
        self.Autobiography = URIRef(self.genre.Autobiography)
        self.Memoir = URIRef(self.genre.Memoir)
        self.Political_Rhetoric = URIRef(self.genre.Political_Rhetoric)
        self.Self_help = URIRef(self.genre.Self_help)
        self.Childrens_Literature = URIRef(self.genre.Childrens_Literature)

        self.genre_mapping = {
            "genre": self.Genre,
            "fiction": self.Fiction,
            "historical": self.Historical,
            "historical fiction": self.Historical,
            "realistic" : self.Realistic,
            "realistic fiction": self.Realistic,
            "autobiographical fiction": self.Autobiographical_Fiction,
            "psychological" : self.Psychological,
            "psychological fiction": self.Psychological,
            "dystopian" : self.Dystopian,
            "dystopian fiction": self.Dystopian,
            "adventure"  : self.Adventure,
            "adventure fiction": self.Adventure,
            "gothic" : self.Gothic,
            "gothic fiction": self.Gothic,
            "dark romanticism" : self.Dark_Romanticism,
            "frame narrative" : self.Frame_Narrative,
            "narrative": self.Frame_Narrative,
            "satire" : self.Satire,
            "fable" : self.Fable,
            "bildungsroman" : self.Bildungsroman,
            "vignette" : self.Vignette,
            "science" : self.Science,
            "science fiction": self.Science,
            "crime" : self.Crime,
            "crime fiction": self.Crime,
            "horror" : self.Horror,
            "horror fiction": self.Horror,
            "fantasy": self.Fantasy,
            "fantasy fiction": self.Fantasy,
            "portal fantasy": self.Portal_Fantasy,
            "religious": self.Religious,
            "religious fiction": self.Religious,
            "humorous": self.Humorous,
            "humorous fiction": self.Humorous,
            "classic" : self.Classic,
            "drama" : self.Drama,
            "realistic drama": self.Realistic_Drama,
            "poetry": self.Poetry,
            "epic" : self.Epic,
            "epic poem" : self.Epic,
            "lyric" : self.Lyric,
            "lyric poetry" : self.Lyric,
            "narrative poetry" : self.Narrative_Poetry,
            "nonfiction" : self.Nonfiction_Genre,
            "autobiography" : self.Autobiography,
            "autobiographical" : self.Autobiography,
            "biography" : self.Autobiography,
            "memoir": self.Memoir,
            "political rhetoric" : self.Political_Rhetoric,
            "self help": self.Self_help,
            "children's literature" : self.Childrens_Literature
        }

    def create_genre_ontology(self):
        self.g.add((self.Genre, RDF.type, OWL.Class))
        self.g.add((self.Fiction, RDF.type, OWL.Class))
        self.g.add((self.Historical, RDF.type, OWL.Class))
        self.g.add((self.Realistic, RDF.type, OWL.Class))
        self.g.add((self.Autobiographical_Fiction, RDF.type, OWL.Class))
        self.g.add((self.Psychological, RDF.type, OWL.Class))
        self.g.add((self.Dystopian, RDF.type, OWL.Class))
        self.g.add((self.Adventure, RDF.type, OWL.Class))
        self.g.add((self.Gothic, RDF.type, OWL.Class))
        self.g.add((self.Dark_Romanticism, RDF.type, OWL.Class))
        self.g.add((self.Frame_Narrative, RDF.type, OWL.Class))
        self.g.add((self.Satire, RDF.type, OWL.Class))
        self.g.add((self.Fable, RDF.type, OWL.Class))
        self.g.add((self.Bildungsroman, RDF.type, OWL.Class))
        self.g.add((self.Vignette, RDF.type, OWL.Class))
        self.g.add((self.Science, RDF.type, OWL.Class))
        self.g.add((self.Crime, RDF.type, OWL.Class))
        self.g.add((self.Horror, RDF.type, OWL.Class))
        self.g.add((self.Fantasy, RDF.type, OWL.Class))
        self.g.add((self.Portal_Fantasy, RDF.type, OWL.Class))
        self.g.add((self.Religious, RDF.type, OWL.Class))
        self.g.add((self.Humorous, RDF.type, OWL.Class))
        self.g.add((self.Classic, RDF.type, OWL.Class))
        self.g.add((self.Drama, RDF.type, OWL.Class))
        self.g.add((self.Realistic_Drama, RDF.type, OWL.Class))
        self.g.add((self.Poetry, RDF.type, OWL.Class))
        self.g.add((self.Epic, RDF.type, OWL.Class))
        self.g.add((self.Lyric, RDF.type, OWL.Class))
        self.g.add((self.Narrative_Poetry, RDF.type, OWL.Class))
        self.g.add((self.Nonfiction_Genre, RDF.type, OWL.Class))
        self.g.add((self.Autobiography, RDF.type, OWL.Class))
        self.g.add((self.Memoir, RDF.type, OWL.Class))
        self.g.add((self.Political_Rhetoric, RDF.type, OWL.Class))
        self.g.add((self.Self_help, RDF.type, OWL.Class))
        self.g.add((self.Childrens_Literature, RDF.type, OWL.Class))

        self.g.add((self.Fiction, RDFS.subClassOf, self.Genre))
        self.g.add((self.Historical, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Realistic, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Autobiographical_Fiction, RDFS.subClassOf, self.Realistic))
        self.g.add((self.Psychological, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Dystopian, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Adventure, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Gothic, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Dark_Romanticism, RDFS.subClassOf, self.Gothic))
        self.g.add((self.Frame_Narrative, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Satire, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Fable, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Bildungsroman, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Vignette, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Science, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Crime, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Horror, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Fantasy, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Portal_Fantasy, RDFS.subClassOf, self.Fantasy))
        self.g.add((self.Religious, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Humorous, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Classic, RDFS.subClassOf, self.Genre))
        self.g.add((self.Drama, RDFS.subClassOf, self.Classic))
        self.g.add((self.Realistic_Drama, RDFS.subClassOf, self.Drama))
        self.g.add((self.Poetry, RDFS.subClassOf, self.Genre))
        self.g.add((self.Lyric, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Narrative_Poetry, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Epic, RDFS.subClassOf, self.Narrative_Poetry))
        self.g.add((self.Nonfiction_Genre, RDFS.subClassOf, self.Genre))
        self.g.add((self.Autobiography, RDFS.subClassOf, self.Nonfiction_Genre))
        self.g.add((self.Memoir, RDFS.subClassOf, self.Autobiography))
        self.g.add((self.Political_Rhetoric, RDFS.subClassOf, self.Nonfiction_Genre))
        self.g.add((self.Self_help, RDFS.subClassOf, self.Nonfiction_Genre))
        self.g.add((self.Childrens_Literature, RDFS.subClassOf, self.Genre))

    def get_genre_mapping(self, key):
        return self.genre_mapping.get(key)

    def get_graph(self):
        return self.g
    
    def save_ontology(self, output_path='data/owls/genre.owl'):
        self.g.serialize(output_path, format='xml')
        print(f'Genre ontology saved to {output_path}')

if __name__ == '__main__':
    genre_ontology = Genre()
    genre_ontology.create_genre_ontology()
    genre_ontology.save_ontology()