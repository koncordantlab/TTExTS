from rdflib import Graph, URIRef, Namespace, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL, XSD
import os

class Subtheme:
    def __init__(self):
        self.g = Graph()

        self.n = Namespace('https://koncordantlab.com/TTEXTS/')
        self.subtheme = Namespace('https://koncordantlab.com/TTEXTS/subtheme/')

        self.g.bind('TTEXTS',self.n)
        self.g.bind('subtheme', self.subtheme)

        self.Subtheme = URIRef(self.n.Subtheme)
        # Section 1: Emotions
        self.Emotion = URIRef(self.subtheme.Emotion)
        self.Negative = URIRef(self.subtheme.Negative)
        self.Positive = URIRef(self.subtheme.Positive)
        self.Disturbing = URIRef(self.subtheme.Disturbing)
        self.Surreal = URIRef(self.subtheme.Surreal)
        self.Discomfort = URIRef(self.subtheme.Discomfort)
        self.Fear = URIRef(self.subtheme.Fear)
        self.Madness = URIRef(self.subtheme.Madness)
        self.Disillusionment = URIRef(self.subtheme.Disillusionment)
        self.Bewildering = URIRef(self.subtheme.Bewildering)
        self.Surprise = URIRef(self.subtheme.Surprise)
        self.Somber = URIRef(self.subtheme.Somber)
        self.Tragic = URIRef(self.subtheme.Tragic)
        self.Tear_jerker = URIRef(self.subtheme.Tear_jerker)
        self.Grief = URIRef(self.subtheme.Grief)
        self.Bittersweet = URIRef(self.subtheme.Bittersweet)
        self.Melancholy = URIRef(self.subtheme.Melancholy)
        self.Emotional = URIRef(self.subtheme.Emotional)
        self.Bleak = URIRef(self.subtheme.Bleak)
        self.Doubt = URIRef(self.subtheme.Doubt)
        self.Guilt = URIRef(self.subtheme.Guilt)
        self.Frank = URIRef(self.subtheme.Frank)
        self.Isolation = URIRef(self.subtheme.Isolation)
        self.Pride = URIRef(self.subtheme.Pride)
        self.Regret = URIRef(self.subtheme.Regret)

        # Section 2: Ideals / Themes
        self.Ideals = URIRef(self.subtheme.Ideals)
        self.Acceptance = URIRef(self.subtheme.Acceptance)
        self.Hopeful = URIRef(self.subtheme.Hopeful)
        self.Moving = URIRef(self.subtheme.Moving)
        self.Inspiring = URIRef(self.subtheme.Inspiring)
        self.Thought_provoking = URIRef(self.subtheme.Thought_provoking)
        self.Romantic = URIRef(self.subtheme.Romantic)
        self.Atmospheric = URIRef(self.subtheme.Atmospheric)
        self.Chemistry = URIRef(self.subtheme.Chemistry)
        self.Empathy = URIRef(self.subtheme.Empathy)
        self.Kindness = URIRef(self.subtheme.Kindness)
        self.Compassion = URIRef(self.subtheme.Compassion)
        self.Empowerment = URIRef(self.subtheme.Empowerment)
        self.Courage = URIRef(self.subtheme.Courage)
        self.Generosity = URIRef(self.subtheme.Generosity)
        self.Pleasure = URIRef(self.subtheme.Pleasure)
        self.Nostalgic = URIRef(self.subtheme.Nostalgic)
        self.Sensational = URIRef(self.subtheme.Sensational)

        # Section 2.a: Revolution & Subthemes
        self.Revolution = URIRef(self.subtheme.Revolution)
        self.Politics = URIRef(self.subtheme.Politics)
        self.Government = URIRef(self.subtheme.Government)
        self.Totalitarian_society = URIRef(self.subtheme.Totalitarian_society)
        self.Oppression = URIRef(self.subtheme.Oppression)
        self.Exploitation = URIRef(self.subtheme.Exploitation)
        self.Individuality = URIRef(self.subtheme.Individuality)
        self.Free_Will = URIRef(self.subtheme.Free_Will)
        self.Colonialism = URIRef(self.subtheme.Colonialism)
        self.Theocracy = URIRef(self.subtheme.Theocracy)
        self.Knowledge = URIRef(self.subtheme.Knowledge)
        self.Civic_Responsibility = URIRef(self.subtheme.Civic_Responsibility)
        self.Dealing_with_Conflict = URIRef(self.subtheme.Dealing_with_Conflict)
        self.Negotiation = URIRef(self.subtheme.Negotiation)
        self.Social_Awareness = URIRef(self.subtheme.Social_Awareness)
        self.Greed = URIRef(self.subtheme.Greed)
        self.Reliance_on_Technology = URIRef(self.subtheme.Reliance_on_Technology)
        self.Surveillance = URIRef(self.subtheme.Surveillance)
        self.Influence_of_mass_media = URIRef(self.subtheme.Influence_of_mass_media)
        self.Naturalism = URIRef(self.subtheme.Naturalism)
        self.fads = URIRef(self.subtheme.fads)
        self.Nature_subtheme = URIRef(self.subtheme.Nature)
        self.Survival = URIRef(self.subtheme.Survival)
        self.Stoicism = URIRef(self.subtheme.Stoicism)
        self.Picaresque = URIRef(self.subtheme.Picaresque)
        self.Nautical = URIRef(self.subtheme.Nautical)
        self.Realism = URIRef(self.subtheme.Realism)
        self.Rural = URIRef(self.subtheme.Rural)
        self.American_Dream = URIRef(self.subtheme.American_Dream)
        self.Hardship = URIRef(self.subtheme.Hardship)
        self.Perserverance = URIRef(self.subtheme.Perserverance)
        self.Resilience = URIRef(self.subtheme.Resilience)
        self.Sacrifice = URIRef(self.subtheme.Sacrifice)
        self.Immigrant_experience = URIRef(self.subtheme.Immigrant_experience)
        self.Border_policy = URIRef(self.subtheme.Border_policy)
        self.Refugee_experience = URIRef(self.subtheme.Refugee_experience)
        self.Pioneer_life = URIRef(self.subtheme.Pioneer_life)
        self.Friendship = URIRef(self.subtheme.Friendship)
        self.Flawed_friendship = URIRef(self.subtheme.Flawed_friendship)
        self.Racism = URIRef(self.subtheme.Racism)
        self.Race = URIRef(self.subtheme.Race)
        self.Slavery = URIRef(self.subtheme.Slavery)
        self.Whitewashing = URIRef(self.subtheme.Whitewashing)
        self.Social_Change = URIRef(self.subtheme.Social_Change)
        self.Abolitionist = URIRef(self.subtheme.Abolitionist)
        self.Trauma = URIRef(self.subtheme.Trauma)
        self.Dehumanization = URIRef(self.subtheme.Dehumanization)
        self.Injustice = URIRef(self.subtheme.Injustice)
        self.Intersectionality = URIRef(self.subtheme.Intersectionality)
        self.Family_Feuds = URIRef(self.subtheme.Family_Feuds)
        self.Vendetta = URIRef(self.subtheme.Vendetta)
        self.Rivalry = URIRef(self.subtheme.Rivalry)
        self.Deception = URIRef(self.subtheme.Deception)
        self.Manipulation = URIRef(self.subtheme.Manipulation)
        self.Mischief = URIRef(self.subtheme.Mischief)
        self.Gender_Roles = URIRef(self.subtheme.Gender_Roles)
        self.Social_Change_Gender = URIRef(self.subtheme.Social_Change_Gender)
        self.Family = URIRef(self.subtheme.Family)
        self.Father_daughter_relationships = URIRef(self.subtheme.Father_daughter_relationships)
        self.Father_son_relationships = URIRef(self.subtheme.Father_son_relationships)
        self.Mother_daughter_relationship = URIRef(self.subtheme.Mother_daughter_relationship)
        self.Sibling_rivalry = URIRef(self.subtheme.Sibling_rivalry)
        self.Found_family = URIRef(self.subtheme.Found_family)
        self.Gender = URIRef(self.subtheme.Gender)
        self.Morality = URIRef(self.subtheme.Morality)
        self.Feminist = URIRef(self.subtheme.Feminist)
        self.Femininity = URIRef(self.subtheme.Femininity)
        self.Female_agency = URIRef(self.subtheme.Female_agency)
        self.Reproductive_rights = URIRef(self.subtheme.Reproductive_rights)
        self.Moral_ambiguity = URIRef(self.subtheme.Moral_ambiguity)
        self.Christian_values = URIRef(self.subtheme.Christian_values)
        self.Biblical = URIRef(self.subtheme.Biblical)
        self.Personal_growth = URIRef(self.subtheme.Personal_growth)
        self.Identity = URIRef(self.subtheme.Identity)
        self.Self_discovery = URIRef(self.subtheme.Self_discovery)
        self.Coming_out = URIRef(self.subtheme.Coming_out)
        self.Self_expression = URIRef(self.subtheme.Self_expression)
        self.Queer = URIRef(self.subtheme.Queer)
        self.Transformation = URIRef(self.subtheme.Transformation)
        self.Human_potential = URIRef(self.subtheme.Human_potential)
        self.Belonging = URIRef(self.subtheme.Belonging)
        self.Conformity_in_society = URIRef(self.subtheme.Conformity_in_society)
        self.Community = URIRef(self.subtheme.Community)
        self.Interdependence = URIRef(self.subtheme.Interdependence)
        self.Unspoken_understanding = URIRef(self.subtheme.Unspoken_understanding)
        self.Revenge = URIRef(self.subtheme.Revenge)
        self.Misjudgment = URIRef(self.subtheme.Misjudgment)
        self.Social_Justice = URIRef(self.subtheme.Social_Justice)
        self.Political = URIRef(self.subtheme.Political)
        self.Activist = URIRef(self.subtheme.Activist)
        self.Resistance = URIRef(self.subtheme.Resistance)
        self.Activism = URIRef(self.subtheme.Activism)
        self.Social_commentary = URIRef(self.subtheme.Social_commentary)
        self.Social_satire = URIRef(self.subtheme.Social_satire)
        self.Social_prejudice = URIRef(self.subtheme.Social_prejudice)
        self.Justice = URIRef(self.subtheme.Justice)
        self.Privilege = URIRef(self.subtheme.Privilege)
        self.Alternate_realities = URIRef(self.subtheme.Alternate_realities)
        self.Time_travel = URIRef(self.subtheme.Time_travel)
        self.Fate = URIRef(self.subtheme.Fate)
        self.Humanism = URIRef(self.subtheme.Humanism)
        self.Human_nature = URIRef(self.subtheme.Human_nature)
        self.Curiosity = URIRef(self.subtheme.Curiosity)
        self.Culture = URIRef(self.subtheme.Culture)
        self.Family_and_Grief = URIRef(self.subtheme.Family_and_Grief)
        self.Loss = URIRef(self.subtheme.Loss)
        self.Accidents = URIRef(self.subtheme.Accidents)
        self.Existential = URIRef(self.subtheme.Existential)
        self.Ability_and_disability = URIRef(self.subtheme.Ability_and_disability)
        self.Physical_handicaps = URIRef(self.subtheme.Physical_handicaps)
        self.Mistreatment = URIRef(self.subtheme.Mistreatment)
        self.Mental_health = URIRef(self.subtheme.Mental_health)
        self.Mental_illness = URIRef(self.subtheme.Mental_illness)
        self.Suicide = URIRef(self.subtheme.Suicide)
        self.Suicide_attempts = URIRef(self.subtheme.Suicide_attempts)
        self.Gossip = URIRef(self.subtheme.Gossip)
        self.Rumors = URIRef(self.subtheme.Rumors)
        self.Descriptions_of_sexual_abuse = URIRef(self.subtheme.Descriptions_of_sexual_abuse)
        self.Social_expectations = URIRef(self.subtheme.Social_expectations)
        self.Redemption = URIRef(self.subtheme.Redemption)
        self.Storytelling = URIRef(self.subtheme.Storytelling)
        self.Imagination_and_escapism = URIRef(self.subtheme.Imagination_and_escapism)
        self.Simplicity = URIRef(self.subtheme.Simplicity)
        self.Reflective = URIRef(self.subtheme.Reflective)
        self.Observation_and_inference = URIRef(self.subtheme.Observation_and_inference)
        self.Social_Darwinism = URIRef(self.subtheme.Social_Darwinism)
        self.Importance_of_language = URIRef(self.subtheme.Importance_of_language)

        # Section 3: Subgenres
        self.Subgenres = URIRef(self.subtheme.Subgenres)
        self.Literature = URIRef(self.subtheme.Literature)
        self.Fiction = URIRef(self.subtheme.Fiction)
        self.Historical_fiction = URIRef(self.subtheme.Historical_fiction)
        self.War = URIRef(self.subtheme.War)
        self.Violence = URIRef(self.subtheme.Violence)
        self.Homecoming = URIRef(self.subtheme.Homecoming)
        self.Heroism = URIRef(self.subtheme.Heroism)
        self.Heroic = URIRef(self.subtheme.Heroic)
        self.Medieval = URIRef(self.subtheme.Medieval)
        self.Mock_heroic = URIRef(self.subtheme.Mock_heroic)
        self.Heros_journey = URIRef(self.subtheme.Heros_journey)
        self.Soviet_Union = URIRef(self.subtheme.Soviet_Union)
        self.Space_Race = URIRef(self.subtheme.Space_Race)
        self.African = URIRef(self.subtheme.African)
        self.Indigenous = URIRef(self.subtheme.Indigenous)
        self.European = URIRef(self.subtheme.European)
        self.British = URIRef(self.subtheme.British)
        self.Roman = URIRef(self.subtheme.Roman)
        self.English = URIRef(self.subtheme.English)
        self.World_War_II = URIRef(self.subtheme.World_War_II)
        self.American_South = URIRef(self.subtheme.American_South)
        self.Civil_Rights_Movement = URIRef(self.subtheme.Civil_Rights_Movement)
        self.Reconstruction_Era = URIRef(self.subtheme.Reconstruction_Era)
        self.World_War_I = URIRef(self.subtheme.World_War_I)
        self.The_Lost_Generation = URIRef(self.subtheme.The_Lost_Generation)
        self.Kansas = URIRef(self.subtheme.Kansas)
        self.French_and_Indian_War = URIRef(self.subtheme.French_and_Indian_War)
        self.Post_9_11 = URIRef(self.subtheme.Post_9_11)
        self._1920s = URIRef(self.subtheme._1920s)
        self.Adventure = URIRef(self.subtheme.Adventure)
        self.Exploration = URIRef(self.subtheme.Exploration)
        self.Fable = URIRef(self.subtheme.Fable)
        self.Folklore = URIRef(self.subtheme.Folklore)
        self.Fairytale = URIRef(self.subtheme.Fairytale)
        self.Coming_of_Age = URIRef(self.subtheme.Coming_of_Age)
        self.Teen_Drama = URIRef(self.subtheme.Teen_Drama)
        self.Young_adult_literature = URIRef(self.subtheme.Young_adult_literature)
        self.Bildungsroman = URIRef(self.subtheme.Bildungsroman)
        self.Horror = URIRef(self.subtheme.Horror)
        self.Gothic = URIRef(self.subtheme.Gothic)
        self.Superstitions = URIRef(self.subtheme.Superstitions)
        self.Haunting = URIRef(self.subtheme.Haunting)
        self.Dark = URIRef(self.subtheme.Dark)
        self.Dark_comedy = URIRef(self.subtheme.Dark_comedy)
        self.Dark_romanticism = URIRef(self.subtheme.Dark_romanticism)
        self.Fantasy = URIRef(self.subtheme.Fantasy)
        self.Supernatural = URIRef(self.subtheme.Supernatural)
        self.Mythology = URIRef(self.subtheme.Mythology)
        self.Dark_fantasy = URIRef(self.subtheme.Dark_fantasy)
        self.Dystopian_fiction = URIRef(self.subtheme.Dystopian_fiction)
        self.Apocalyptic = URIRef(self.subtheme.Apocalyptic)
        self.Post_apocalyptic = URIRef(self.subtheme.Post_apocalyptic)
        self.Realistic_fiction = URIRef(self.subtheme.Realistic_fiction)
        self.Dark_realism = URIRef(self.subtheme.Dark_realism)
        self.Urban = URIRef(self.subtheme.Urban)
        self.Magical_realism = URIRef(self.subtheme.Magical_realism)
        self.Psychological_fiction = URIRef(self.subtheme.Psychological_fiction)
        self.Thriller = URIRef(self.subtheme.Thriller)
        self.Suspense = URIRef(self.subtheme.Suspense)
        self.Mystery = URIRef(self.subtheme.Mystery)
        self.Whodunnit = URIRef(self.subtheme.Whodunnit)
        self.Locked_room_mystery = URIRef(self.subtheme.Locked_room_mystery)
        self.Speculative = URIRef(self.subtheme.Speculative)
        self.Classic = URIRef(self.subtheme.Classic)
        self.Modern_classic = URIRef(self.subtheme.Modern_classic)
        self.Drama = URIRef(self.subtheme.Drama)
        self.Historical = URIRef(self.subtheme.Historical)
        self.Science_Fiction = URIRef(self.subtheme.Science_Fiction)
        self.Space = URIRef(self.subtheme.Space)
        self.Space_Opera = URIRef(self.subtheme.Space_Opera)
        self.Romance = URIRef(self.subtheme.Romance)
        self.Revenge_Love = URIRef(self.subtheme.Revenge_Love)
        self.Forbidden_Love = URIRef(self.subtheme.Forbidden_Love)
        self.Tragedy_subgenre = URIRef(self.subtheme.Tragedy_subgenre)
        self.Dramatic = URIRef(self.subtheme.Dramatic)
        self.Humor = URIRef(self.subtheme.Humor)
        self.Multicultural = URIRef(self.subtheme.Multicultural)
        self.Harlem_Renaissance = URIRef(self.subtheme.Harlem_Renaissance)
        self.Eye_Dialect = URIRef(self.subtheme.Eye_Dialect)
        self.Contemporary = URIRef(self.subtheme.Contemporary)
        self.Short_fiction = URIRef(self.subtheme.Short_fiction)
        self.Novella = URIRef(self.subtheme.Novella)
        self.Short_stories = URIRef(self.subtheme.Short_stories)
        self.Flash_fiction = URIRef(self.subtheme.Flash_fiction)
        self.Postmodern = URIRef(self.subtheme.Postmodern)
        self.Sports = URIRef(self.subtheme.Sports)
        self.Nonsensical = URIRef(self.subtheme.Nonsensical)
        self.Epistolary = URIRef(self.subtheme.Epistolary)
        self.Non_fiction = URIRef(self.subtheme.Non_fiction)
        self.Memoir = URIRef(self.subtheme.Memoir)
        self.Autobiography = URIRef(self.subtheme.Autobiography)
        self.Narrative = URIRef(self.subtheme.Narrative)
        self.Social_Science = URIRef(self.subtheme.Social_Science)
        self.Business_and_Economics = URIRef(self.subtheme.Business_and_Economics)
        self.Travel_Writing = URIRef(self.subtheme.Travel_Writing)
        self.Nature_writing = URIRef(self.subtheme.Nature_writing)
        self.True_Crime = URIRef(self.subtheme.True_Crime)
        self.Investigative_reporting = URIRef(self.subtheme.Investigative_reporting)
        self.Speechcraft = URIRef(self.subtheme.Speechcraft)
        self.Poetry = URIRef(self.subtheme.Poetry)
        self.Debate = URIRef(self.subtheme.Debate)
        self.Elegy = URIRef(self.subtheme.Elegy)
        self.Rondeau = URIRef(self.subtheme.Rondeau)
        self.Imagism = URIRef(self.subtheme.Imagism)
        self.Confessional_poetry = URIRef(self.subtheme.Confessional_poetry)
        self.Spoken_word = URIRef(self.subtheme.Spoken_word)
        self.Allegory = URIRef(self.subtheme.Allegory)
        self.Satire = URIRef(self.subtheme.Satire)
        self.Sardonic = URIRef(self.subtheme.Sardonic)
        self.Irony = URIRef(self.subtheme.Irony)
        self.American = URIRef(self.subtheme.American)
        self.Presidental = URIRef(self.subtheme.Presidental)
        self.Transcendentalism = URIRef(self.subtheme.Transcendentalism)
        self.Unreliable_Narrator = URIRef(self.subtheme.Unreliable_Narrator)
        self.Persuasive = URIRef(self.subtheme.Persuasive)
        self.Philosophical = URIRef(self.subtheme.Philosophical)
        self.Inspirational = URIRef(self.subtheme.Inspirational)
        self.Foreshadowing = URIRef(self.subtheme.Foreshadowing)
        self.Graphic_Novel = URIRef(self.subtheme.Graphic_Novel)
        self.Imagery = URIRef(self.subtheme.Imagery)
        self.Metaphorical = URIRef(self.subtheme.Metaphorical)
        self.Symbolism = URIRef(self.subtheme.Symbolism)
        self.Childrens = URIRef(self.subtheme.Childrens)
        self.Animal_story = URIRef(self.subtheme.Animal_story)
        self.Anthropomorphism = URIRef(self.subtheme.Anthropomorphism)
        self.Literary_reimagining = URIRef(self.subtheme.Literary_reimagining)
        self.Film_analysis = URIRef(self.subtheme.Film_analysis)
        self.Circular_Reporting = URIRef(self.subtheme.Circular_Reporting)

        self.subtheme_mapping = {
            "emotions": self.Emotion,
            "negative": self.Negative,
            "positive": self.Positive,
            "disturbing": self.Disturbing,
            "surreal": self.Surreal,
            "discomfort": self.Discomfort,
            "fear": self.Fear,
            "madness": self.Madness,
            "disillusionment": self.Disillusionment,
            "bewildering": self.Bewildering,
            "surprise": self.Surprise,
            "somber": self.Somber,
            "tragic": self.Tragic,
            "tear jerker": self.Tear_jerker,
            "grief": self.Grief,
            "bittersweet": self.Bittersweet,
            "melancholy": self.Melancholy,
            "emotional": self.Emotional,
            "bleak": self.Bleak,
            "doubt": self.Doubt,
            "guilt": self.Guilt,
            "frank": self.Frank,
            "isolation": self.Isolation,
            "pride": self.Pride,
            "regret": self.Regret,
            "ideals": self.Ideals,
            "acceptance": self.Acceptance,
            "hopeful": self.Hopeful,
            "moving": self.Moving,
            "inspiring": self.Inspiring,
            "thought provoking": self.Thought_provoking,
            "romantic": self.Romantic,
            "atmospheric": self.Atmospheric,
            "chemistry": self.Chemistry,
            "empathy": self.Empathy,
            "kindness": self.Kindness,
            "compassion": self.Compassion,
            "empowerment": self.Empowerment,
            "courage": self.Courage,
            "generosity": self.Generosity,
            "pleasure": self.Pleasure,
            "nostalgic": self.Nostalgic,
            "sensational": self.Sensational,
            "revolution": self.Revolution,
            "politics": self.Politics,
            "government": self.Government,
            "totalitarian society": self.Totalitarian_society,
            "oppression": self.Oppression,
            "exploitation": self.Exploitation,
            "individuality": self.Individuality,
            "free will": self.Free_Will,
            "colonialism": self.Colonialism,
            "theocracy": self.Theocracy,
            "knowledge": self.Knowledge,
            "civic responsibility": self.Civic_Responsibility,
            "dealing with conflict": self.Dealing_with_Conflict,
            "negotiation": self.Negotiation,
            "social awareness": self.Social_Awareness,
            "greed": self.Greed,
            "reliance on technology": self.Reliance_on_Technology,
            "technology": self.Reliance_on_Technology,
            "surveillance": self.Surveillance,
            "influence of mass media": self.Influence_of_mass_media,
            "naturalism": self.Naturalism,
            "fads": self.fads,
            "nature": self.Nature_subtheme,
            "survival": self.Survival,
            "stoicism": self.Stoicism,
            "picaresque": self.Picaresque,
            "nautical": self.Nautical,
            "realism": self.Realism,
            "rural": self.Rural,
            "american dream": self.American_Dream,
            "hardship": self.Hardship,
            "perserverance": self.Perserverance,
            "resilience": self.Resilience,
            "sacrifice": self.Sacrifice,
            "immigrant experience": self.Immigrant_experience,
            "border policy": self.Border_policy,
            "refugee experience": self.Refugee_experience,
            "pioneer life": self.Pioneer_life,
            "friendship": self.Friendship,
            "flawed friendship": self.Flawed_friendship,
            "racism": self.Racism,
            "race": self.Race,
            "slavery": self.Slavery,
            "whitewashing": self.Whitewashing,
            "social change": self.Social_Change,
            "abolitionist": self.Abolitionist,
            "trauma": self.Trauma,
            "dehumanization": self.Dehumanization,
            "injustice": self.Injustice,
            "intersectionality": self.Intersectionality,
            "family feuds": self.Family_Feuds,
            "vendetta": self.Vendetta,
            "rivalry": self.Rivalry,
            "deception": self.Deception,
            "manipulation": self.Manipulation,
            "mischief": self.Mischief,
            "gender roles": self.Gender_Roles,
            "family": self.Family,
            "family drama": self.Family,
            "father daughter relationships": self.Father_daughter_relationships,
            "father son relationships": self.Father_son_relationships,
            "mother daughter relationship": self.Mother_daughter_relationship,
            "sibling rivalry": self.Sibling_rivalry,
            "found family": self.Found_family,
            "gender": self.Gender,
            "morality": self.Morality,
            "moral responsibility": self.Morality,
            "feminist": self.Feminist,
            "femininity": self.Femininity,
            "female agency": self.Female_agency,
            "reproductive rights": self.Reproductive_rights,
            "moral ambiguity": self.Moral_ambiguity,
            "christian values": self.Christian_values,
            "biblical": self.Biblical,
            "personal growth": self.Personal_growth,
            "identity": self.Identity,
            "self discovery": self.Self_discovery,
            "coming out": self.Coming_out,
            "self expression": self.Self_expression,
            "queer": self.Queer,
            "transformation": self.Transformation,
            "human potential": self.Human_potential,
            "belonging": self.Belonging,
            "conformity in society": self.Conformity_in_society,
            "community": self.Community,
            "interdependence": self.Interdependence,
            "unspoken understanding": self.Unspoken_understanding,
            "revenge": self.Revenge,
            "misjudgment": self.Misjudgment,
            "social justice": self.Social_Justice,
            "political": self.Political,
            "activist": self.Activist,
            "resistance": self.Resistance,
            "activism": self.Activism,
            "social commentary": self.Social_commentary,
            "social satire": self.Social_satire,
            "social prejudice": self.Social_prejudice,
            "justice": self.Justice,
            "privilege": self.Privilege,
            "alternate realities": self.Alternate_realities,
            "time travel": self.Time_travel,
            "fate": self.Fate,
            "humanism": self.Humanism,
            "human nature": self.Human_nature,
            "curiosity": self.Curiosity,
            "culture": self.Culture,
            "family and grief": self.Family_and_Grief,
            "loss": self.Loss,
            "accidents": self.Accidents,
            "existential": self.Existential,
            "ability and disability": self.Ability_and_disability,
            "physical handicaps": self.Physical_handicaps,
            "mistreatment": self.Mistreatment,
            "mental health": self.Mental_health,
            "mental illness": self.Mental_illness,
            "suicide": self.Suicide,
            "suicide attempts": self.Suicide_attempts,
            "gossip": self.Gossip,
            "rumors": self.Rumors,
            "descriptions of sexual abuse": self.Descriptions_of_sexual_abuse,
            "social expectations": self.Social_expectations,
            "redemption": self.Redemption,
            "storytelling": self.Storytelling,
            "imagination and escapism": self.Imagination_and_escapism,
            "simplicity": self.Simplicity,
            "reflective": self.Reflective,
            "observation and inference": self.Observation_and_inference,
            "social darwinism": self.Social_Darwinism,
            "importance of language": self.Importance_of_language,
            "subgenres": self.Subgenres,
            "literature": self.Literature,
            "fiction": self.Fiction,
            "historical fiction": self.Historical_fiction,
            "war": self.War,
            "violence": self.Violence,
            "homecoming": self.Homecoming,
            "heroism": self.Heroism,
            "heroic": self.Heroic,
            "medieval": self.Medieval,
            "mock heroic": self.Mock_heroic,
            "heros journey": self.Heros_journey,
            "soviet union": self.Soviet_Union,
            "space race": self.Space_Race,
            "african": self.African,
            "indigenous": self.Indigenous,
            "european": self.European,
            "british": self.British,
            "roman": self.Roman,
            "english": self.English,
            "world war ii": self.World_War_II,
            "american south": self.American_South,
            "civil rights movement": self.Civil_Rights_Movement,
            "reconstruction era": self.Reconstruction_Era,
            "world war i": self.World_War_I,
            "the lost generation": self.The_Lost_Generation,
            "kansas": self.Kansas,
            "french and indian war": self.French_and_Indian_War,
            "post 9 11": self.Post_9_11,
            "1920s": self._1920s,
            "adventure": self.Adventure,
            "exploration": self.Exploration,
            "fable": self.Fable,
            "folklore": self.Folklore,
            "fairytale": self.Fairytale,
            "coming of age": self.Coming_of_Age,
            "teen drama": self.Teen_Drama,
            "young adult literature": self.Young_adult_literature,
            "bildungsroman": self.Bildungsroman,
            "young adult": self.Young_adult_literature,
            "horror": self.Horror,
            "gothic": self.Gothic,
            "superstitions": self.Superstitions,
            "haunting": self.Haunting,
            "dark": self.Dark,
            "dark comedy": self.Dark_comedy,
            "dark romanticism": self.Dark_romanticism,
            "fantasy": self.Fantasy,
            "supernatural": self.Supernatural,
            "mythology": self.Mythology,
            "dark fantasy": self.Dark_fantasy,
            "dystopian fiction": self.Dystopian_fiction,
            "dystopian": self.Dystopian_fiction,
            "apocalyptic": self.Apocalyptic,
            "post apocalyptic": self.Post_apocalyptic,
            "realistic fiction": self.Realistic_fiction,
            "realistic": self.Realistic_fiction,
            "dark realism": self.Dark_realism,
            "urban": self.Urban,
            "magical realism": self.Magical_realism,
            "psychological fiction": self.Psychological_fiction,
            "psychological": self.Psychological_fiction,
            "psychology": self.Psychological_fiction,
            "thriller": self.Thriller,
            "suspense": self.Suspense,
            "mystery": self.Mystery,
            "whodunnit": self.Whodunnit,
            "locked room mystery": self.Locked_room_mystery,
            "speculative": self.Speculative,
            "classic": self.Classic,
            "modern classic": self.Modern_classic,
            "modernism": self.Modern_classic,
            "modern": self.Modern_classic,
            "drama": self.Drama,
            "historical": self.Historical,
            "history": self.Historical,
            "science fiction": self.Science_Fiction,
            "science": self.Science_Fiction,
            "space": self.Space,
            "space opera": self.Space_Opera,
            "romance": self.Romance,
            "love": self.Romance,
            "revenge love": self.Revenge_Love,
            "forbidden love": self.Forbidden_Love,
            "tragedy": self.Tragedy_subgenre,
            "dramatic": self.Dramatic,
            "humor": self.Humor,
            "multicultural": self.Multicultural,
            "harlem renaissance": self.Harlem_Renaissance,
            "eye dialect": self.Eye_Dialect,
            "contemporary": self.Contemporary,
            "short fiction": self.Short_fiction,
            "novella": self.Novella,
            "short stories": self.Short_stories,
            "flash fiction": self.Flash_fiction,
            "postmodern": self.Postmodern,
            "sports": self.Sports,
            "nonsensical": self.Nonsensical,
            "epistolary": self.Epistolary,
            "non fiction": self.Non_fiction,
            "memoir": self.Memoir,
            "autobiography": self.Autobiography,
            "narrative": self.Narrative,
            "narrative nonfiction": self.Narrative,
            "social science": self.Social_Science,
            "business and economics": self.Business_and_Economics,
            "travel writing": self.Travel_Writing,
            "nature writing": self.Nature_writing,
            "true crime": self.True_Crime,
            "investigative reporting": self.Investigative_reporting,
            "speechcraft": self.Speechcraft,
            "poetry": self.Poetry,
            "debate": self.Debate,
            "elegy": self.Elegy,
            "rondeau": self.Rondeau,
            "imagism": self.Imagism,
            "confessional poetry": self.Confessional_poetry,
            "spoken word": self.Spoken_word,
            "spoken word poetry": self.Spoken_word,
            "allegory": self.Allegory,
            "satire": self.Satire,
            "sardonic": self.Sardonic,
            "irony": self.Irony,
            "american": self.American,
            "presidental": self.Presidental,
            "transcendentalism": self.Transcendentalism,
            "unreliable narrator": self.Unreliable_Narrator,
            "persuasive": self.Persuasive,
            "philosophical": self.Philosophical,
            "inspirational": self.Inspirational,
            "foreshadowing": self.Foreshadowing,
            "graphic novel": self.Graphic_Novel,
            "imagery": self.Imagery,
            "metaphorical": self.Metaphorical,
            "symbolism": self.Symbolism,
            "childrens": self.Childrens,
            "childrens literature": self.Childrens,
            "animal story": self.Animal_story,
            "anthropomorphism": self.Anthropomorphism,
            "literary reimagining": self.Literary_reimagining,
            "film analysis": self.Film_analysis,
            "circular reporting": self.Circular_Reporting
        }



    def create_subtheme_ontology(self):
        self.all_keywords = [
            self.Subtheme, self.Emotion, self.Negative, self.Positive, self.Disturbing, self.Surreal, self.Discomfort, self.Fear, self.Madness, self.Disillusionment, 
            self.Bewildering, self.Surprise, self.Somber, self.Tragic, self.Tear_jerker, self.Grief, self.Bittersweet, self.Melancholy, self.Emotional, 
            self.Bleak, self.Doubt, self.Guilt, self.Frank, self.Isolation, self.Pride, self.Regret, self.Ideals, self.Acceptance, self.Hopeful, self.Moving, 
            self.Inspiring, self.Thought_provoking, self.Romantic, self.Atmospheric, self.Chemistry, self.Empathy, self.Kindness, self.Compassion, 
            self.Empowerment, self.Courage, self.Generosity, self.Pleasure, self.Nostalgic, self.Sensational, self.Revolution, self.Politics, self.Government, 
            self.Totalitarian_society, self.Oppression, self.Exploitation, self.Individuality, self.Free_Will, self.Colonialism, self.Theocracy, self.Knowledge, 
            self.Civic_Responsibility, self.Dealing_with_Conflict, self.Negotiation, self.Social_Awareness, self.Greed, self.Reliance_on_Technology, 
            self.Surveillance, self.Influence_of_mass_media, self.Naturalism, self.fads, self.Nature_subtheme, self.Survival, self.Stoicism, self.Picaresque, 
            self.Nautical, self.Realism, self.Rural, self.American_Dream, self.Hardship, self.Perserverance, self.Resilience, self.Sacrifice, 
            self.Immigrant_experience, self.Border_policy, self.Refugee_experience, self.Pioneer_life, self.Friendship, self.Flawed_friendship, self.Racism, 
            self.Race, self.Slavery, self.Whitewashing, self.Social_Change, self.Abolitionist, self.Trauma, self.Dehumanization, self.Injustice, 
            self.Intersectionality, self.Family_Feuds, self.Vendetta, self.Rivalry, self.Deception, self.Manipulation, self.Mischief, self.Gender_Roles, 
            self.Social_Change_Gender, self.Family, self.Father_daughter_relationships, self.Father_son_relationships, self.Mother_daughter_relationship, 
            self.Sibling_rivalry, self.Found_family, self.Gender, self.Morality, self.Feminist, self.Femininity, self.Female_agency, self.Reproductive_rights, 
            self.Moral_ambiguity, self.Christian_values, self.Biblical, self.Personal_growth, self.Identity, self.Self_discovery, self.Coming_out, self.Self_expression, 
            self.Queer, self.Transformation, self.Human_potential, self.Belonging, self.Conformity_in_society, self.Community, self.Interdependence, 
            self.Unspoken_understanding, self.Revenge, self.Misjudgment, self.Social_Justice, self.Political, self.Activist, self.Resistance, self.Activism, 
            self.Social_commentary, self.Social_satire, self.Social_prejudice, self.Justice, self.Privilege, self.Alternate_realities, self.Time_travel, 
            self.Fate, self.Humanism, self.Human_nature, self.Curiosity, self.Culture, self.Family_and_Grief, self.Loss, self.Accidents, self.Existential, 
            self.Ability_and_disability, self.Physical_handicaps, self.Mistreatment, self.Mental_health, self.Mental_illness, self.Suicide, 
            self.Suicide_attempts, self.Gossip, self.Rumors, self.Descriptions_of_sexual_abuse, self.Social_expectations, self.Redemption, self.Storytelling, 
            self.Imagination_and_escapism, self.Simplicity, self.Reflective, self.Observation_and_inference, self.Social_Darwinism, 
            self.Importance_of_language, self.Subgenres, self.Literature, self.Fiction, self.Historical_fiction, self.War, self.Violence, self.Homecoming, 
            self.Heroism, self.Heroic, self.Medieval, self.Mock_heroic, self.Heros_journey, self.Soviet_Union, self.Space_Race, self.African, 
            self.Indigenous, self.European, self.British, self.Roman, self.English, self.World_War_II, self.American_South, self.Civil_Rights_Movement, 
            self.Reconstruction_Era, self.World_War_I, self.The_Lost_Generation, self.Kansas, self.French_and_Indian_War, self.Post_9_11, self._1920s, 
            self.Adventure, self.Exploration, self.Fable, self.Folklore, self.Fairytale, self.Coming_of_Age, self.Teen_Drama, self.Young_adult_literature, 
            self.Bildungsroman, self.Horror, self.Gothic, self.Superstitions, self.Haunting, self.Dark, self.Dark_comedy, self.Dark_romanticism, 
            self.Fantasy, self.Supernatural, self.Mythology, self.Dark_fantasy, self.Dystopian_fiction, self.Apocalyptic, self.Post_apocalyptic, 
            self.Realistic_fiction, self.Dark_realism, self.Urban, self.Magical_realism, self.Psychological_fiction, self.Thriller, self.Suspense, 
            self.Mystery, self.Whodunnit, self.Locked_room_mystery, self.Speculative, self.Classic, self.Modern_classic, self.Drama, self.Historical, 
            self.Science_Fiction, self.Space, self.Space_Opera, self.Romance, self.Revenge_Love, self.Forbidden_Love, self.Tragedy_subgenre, 
            self.Dramatic, self.Humor, self.Multicultural, self.Harlem_Renaissance, self.Eye_Dialect, self.Contemporary, self.Short_fiction, 
            self.Novella, self.Short_stories, self.Flash_fiction, self.Postmodern, self.Sports, self.Nonsensical, self.Epistolary, self.Non_fiction, 
            self.Memoir, self.Autobiography, self.Narrative, self.Social_Science, self.Business_and_Economics, self.Travel_Writing, self.Nature_writing, 
            self.True_Crime, self.Investigative_reporting, self.Speechcraft, self.Poetry, self.Debate, self.Elegy, self.Rondeau, self.Imagism, 
            self.Confessional_poetry, self.Spoken_word, self.Allegory, self.Satire, self.Sardonic, self.Irony, self.American, self.Presidental, 
            self.Transcendentalism, self.Unreliable_Narrator, self.Persuasive, self.Philosophical, self.Inspirational, self.Foreshadowing, 
            self.Graphic_Novel, self.Imagery, self.Metaphorical, self.Symbolism, self.Childrens, self.Animal_story, self.Anthropomorphism, 
            self.Literary_reimagining, self.Film_analysis, self.Circular_Reporting
        ]

        for keyword in self.all_keywords:
            self.g.add((keyword, RDF.type, OWL.Class))

        self.g.add((self.Emotion, RDFS.subClassOf, self.Subtheme))

        # 1. Emotions Hierarchy
        self.g.add((self.Negative, RDFS.subClassOf, self.Emotion))
        self.g.add((self.Positive, RDFS.subClassOf, self.Emotion))

        # 1.a. Negative Hierarchy
        self.g.add((self.Disturbing, RDFS.subClassOf, self.Negative))
        self.g.add((self.Madness, RDFS.subClassOf, self.Negative))
        self.g.add((self.Somber, RDFS.subClassOf, self.Negative))
        self.g.add((self.Bleak, RDFS.subClassOf, self.Negative))
        self.g.add((self.Pride, RDFS.subClassOf, self.Negative))
        self.g.add((self.Regret, RDFS.subClassOf, self.Negative))

        # 1.a.i. Disturbing
        self.g.add((self.Surreal, RDFS.subClassOf, self.Disturbing))
        self.g.add((self.Discomfort, RDFS.subClassOf, self.Disturbing))
        self.g.add((self.Fear, RDFS.subClassOf, self.Disturbing))

        # 1.a.ii. Madness
        self.g.add((self.Disillusionment, RDFS.subClassOf, self.Madness))
        self.g.add((self.Bewildering, RDFS.subClassOf, self.Madness))
        self.g.add((self.Surprise, RDFS.subClassOf, self.Madness))

        # 1.a.iii. Somber
        self.g.add((self.Tragic, RDFS.subClassOf, self.Somber))
        self.g.add((self.Grief, RDFS.subClassOf, self.Somber))
        self.g.add((self.Bittersweet, RDFS.subClassOf, self.Somber))
        self.g.add((self.Melancholy, RDFS.subClassOf, self.Somber))
        self.g.add((self.Emotional, RDFS.subClassOf, self.Somber))
        self.g.add((self.Tear_jerker, RDFS.subClassOf, self.Tragic))

        # 1.a.iv. Bleak
        self.g.add((self.Doubt, RDFS.subClassOf, self.Bleak))
        self.g.add((self.Guilt, RDFS.subClassOf, self.Bleak))
        self.g.add((self.Frank, RDFS.subClassOf, self.Bleak))
        self.g.add((self.Isolation, RDFS.subClassOf, self.Bleak))

        # 1.a.vi. Regret
        self.g.add((self.Acceptance, RDFS.subClassOf, self.Regret))

        # 1.b. Positive Hierarchy
        self.g.add((self.Hopeful, RDFS.subClassOf, self.Positive))
        self.g.add((self.Thought_provoking, RDFS.subClassOf, self.Positive))
        self.g.add((self.Romantic, RDFS.subClassOf, self.Positive))
        self.g.add((self.Empathy, RDFS.subClassOf, self.Positive))
        self.g.add((self.Empowerment, RDFS.subClassOf, self.Positive))
        self.g.add((self.Generosity, RDFS.subClassOf, self.Positive))
        self.g.add((self.Pleasure, RDFS.subClassOf, self.Positive))
        self.g.add((self.Sensational, RDFS.subClassOf, self.Positive))

        # 1.b.i. Hopeful
        self.g.add((self.Moving, RDFS.subClassOf, self.Hopeful))
        self.g.add((self.Inspiring, RDFS.subClassOf, self.Hopeful))

        #1.b.iii. Romantic
        self.g.add((self.Atmospheric, RDFS.subClassOf, self.Romantic))
        self.g.add((self.Chemistry, RDFS.subClassOf, self.Romantic))

        #1.b.iv. Empathy
        self.g.add((self.Kindness, RDFS.subClassOf, self.Empathy))
        self.g.add((self.Compassion, RDFS.subClassOf, self.Empathy))

        #1.b.v. Empowerment
        self.g.add((self.Courage, RDFS.subClassOf, self.Empowerment))

        #1.b.vii. Pleasure
        self.g.add((self.Nostalgic, RDFS.subClassOf, self.Pleasure))



        # 2. Ideals Hierarchy
        self.g.add((self.Ideals, RDFS.subClassOf, self.Subtheme))

        self.g.add((self.Revolution, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Reliance_on_Technology, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Naturalism, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Realism, RDFS.subClassOf, self.Ideals))
        self.g.add((self.American_Dream, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Friendship, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Racism, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Family_Feuds, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Gender_Roles, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Morality, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Personal_growth, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Belonging, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Revenge, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Social_Justice, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Justice, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Alternate_realities, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Time_travel, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Fate, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Humanism, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Mental_health, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Social_expectations, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Redemption, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Storytelling, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Reflective, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Observation_and_inference, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Social_Darwinism, RDFS.subClassOf, self.Ideals))
        self.g.add((self.Importance_of_language, RDFS.subClassOf, self.Ideals))

        # 2.a. Revolution Hierarchy
        self.g.add((self.Politics, RDFS.subClassOf, self.Revolution))

        # 2.a.i. Politics Hierarchy
        self.g.add((self.Government, RDFS.subClassOf, self.Politics))
        self.g.add((self.Civic_Responsibility, RDFS.subClassOf, self.Politics))
        self.g.add((self.Dealing_with_Conflict, RDFS.subClassOf, self.Politics))
        self.g.add((self.Negotiation, RDFS.subClassOf, self.Dealing_with_Conflict))
        self.g.add((self.Social_Awareness, RDFS.subClassOf, self.Politics))
        self.g.add((self.Greed, RDFS.subClassOf, self.Politics))

        # 2.a.i.1. Government Hierarchy
        self.g.add((self.Totalitarian_society, RDFS.subClassOf, self.Government))
        self.g.add((self.Colonialism, RDFS.subClassOf, self.Government))
        self.g.add((self.Theocracy, RDFS.subClassOf, self.Government))

        # 2.a.i.1.i. Totalitarian_society Hierarchy
        self.g.add((self.Oppression, RDFS.subClassOf, self.Totalitarian_society))
        self.g.add((self.Exploitation, RDFS.subClassOf, self.Oppression))
        self.g.add((self.Individuality, RDFS.subClassOf, self.Totalitarian_society))
        self.g.add((self.Free_Will, RDFS.subClassOf, self.Totalitarian_society))
        self.g.add((self.Knowledge, RDFS.subClassOf, self.Free_Will))


        # 2.b Sub-hierarchy of Reliance on Technology
        self.g.add((self.Surveillance, RDFS.subClassOf, self.Reliance_on_Technology))
        self.g.add((self.Influence_of_mass_media, RDFS.subClassOf, self.Reliance_on_Technology))
        self.g.add((self.fads, RDFS.subClassOf, self.Naturalism))

        # 2.c. Sub-hierarchy of Naturalism
        self.g.add((self.Nature_subtheme, RDFS.subClassOf, self.Naturalism))
        self.g.add((self.Survival, RDFS.subClassOf, self.Nature_subtheme))
        self.g.add((self.Stoicism, RDFS.subClassOf, self.Nature_subtheme))
        self.g.add((self.Picaresque, RDFS.subClassOf, self.Naturalism))
        self.g.add((self.Nautical, RDFS.subClassOf, self.Naturalism))

        # 2.d. Sub-hierarchy of Realism
        self.g.add((self.Rural, RDFS.subClassOf, self.Realism))

        # 2.e. Sub-hierarchy of American Dream
        self.g.add((self.Hardship, RDFS.subClassOf, self.American_Dream))
        self.g.add((self.Immigrant_experience, RDFS.subClassOf, self.American_Dream))
        self.g.add((self.Refugee_experience, RDFS.subClassOf, self.American_Dream))
        self.g.add((self.Pioneer_life, RDFS.subClassOf, self.American_Dream))
        self.g.add((self.Perserverance, RDFS.subClassOf, self.Hardship))
        self.g.add((self.Resilience, RDFS.subClassOf, self.Hardship))
        self.g.add((self.Sacrifice, RDFS.subClassOf, self.Hardship))
        self.g.add((self.Border_policy, RDFS.subClassOf, self.Immigrant_experience))

        # 2.f. Sub-hierarchy of Friendship
        self.g.add((self.Flawed_friendship, RDFS.subClassOf, self.Friendship))

        # 2.g. Sub-hierarchy of Racism
        self.g.add((self.Race, RDFS.subClassOf, self.Racism))
        self.g.add((self.Social_Change, RDFS.subClassOf, self.Racism))
        self.g.add((self.Trauma, RDFS.subClassOf, self.Racism))
        self.g.add((self.Injustice, RDFS.subClassOf, self.Racism))
        self.g.add((self.Intersectionality, RDFS.subClassOf, self.Racism))
        self.g.add((self.Slavery, RDFS.subClassOf, self.Race))
        self.g.add((self.Whitewashing, RDFS.subClassOf, self.Race))
        self.g.add((self.Abolitionist, RDFS.subClassOf, self.Social_Change))
        self.g.add((self.Dehumanization, RDFS.subClassOf, self.Trauma))

        # 2.h. Sub-hierarchy of Family Feuds
        self.g.add((self.Vendetta, RDFS.subClassOf, self.Family_Feuds))
        self.g.add((self.Rivalry, RDFS.subClassOf, self.Family_Feuds))
        self.g.add((self.Deception, RDFS.subClassOf, self.Family_Feuds))
        self.g.add((self.Manipulation, RDFS.subClassOf, self.Deception))
        self.g.add((self.Mischief, RDFS.subClassOf, self.Deception))

        # 2.i. Sub-hierarchy of Gender Roles
        self.g.add((self.Social_Change_Gender, RDFS.subClassOf, self.Gender_Roles))
        self.g.add((self.Family, RDFS.subClassOf, self.Gender_Roles))
        self.g.add((self.Gender, RDFS.subClassOf, self.Gender_Roles))
        self.g.add((self.Father_daughter_relationships, RDFS.subClassOf, self.Family))
        self.g.add((self.Father_son_relationships, RDFS.subClassOf, self.Family))
        self.g.add((self.Mother_daughter_relationship, RDFS.subClassOf, self.Family))
        self.g.add((self.Sibling_rivalry, RDFS.subClassOf, self.Family))
        self.g.add((self.Found_family, RDFS.subClassOf, self.Family))
        self.g.add((self.Feminist, RDFS.subClassOf, self.Gender))
        self.g.add((self.Reproductive_rights, RDFS.subClassOf, self.Gender))
        self.g.add((self.Femininity, RDFS.subClassOf, self.Feminist))
        self.g.add((self.Female_agency, RDFS.subClassOf, self.Feminist))

        # 2.j. Sub-hierarchy of Morality
        self.g.add((self.Moral_ambiguity, RDFS.subClassOf, self.Morality))
        self.g.add((self.Christian_values, RDFS.subClassOf, self.Morality))
        self.g.add((self.Biblical, RDFS.subClassOf, self.Christian_values))

        # 2.k. Sub-hierarchy of Personal growth
        self.g.add((self.Identity, RDFS.subClassOf, self.Personal_growth))
        self.g.add((self.Self_discovery, RDFS.subClassOf, self.Personal_growth))
        self.g.add((self.Self_expression, RDFS.subClassOf, self.Personal_growth))
        self.g.add((self.Transformation, RDFS.subClassOf, self.Personal_growth))
        self.g.add((self.Human_potential, RDFS.subClassOf, self.Personal_growth))
        self.g.add((self.Coming_out, RDFS.subClassOf, self.Self_discovery))
        self.g.add((self.Queer, RDFS.subClassOf, self.Self_expression))

        # 2.l. Sub-hierarchy of Belonging
        self.g.add((self.Conformity_in_society, RDFS.subClassOf, self.Belonging))
        self.g.add((self.Community, RDFS.subClassOf, self.Belonging))
        self.g.add((self.Unspoken_understanding, RDFS.subClassOf, self.Belonging))
        self.g.add((self.Interdependence, RDFS.subClassOf, self.Community))

        # 2.m. Sub-hierarchy of Revenge
        self.g.add((self.Misjudgment, RDFS.subClassOf, self.Revenge))

        # 2.n. Sub-hierarchy of Social Justice
        self.g.add((self.Political, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Activist, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Resistance, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Activism, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Social_commentary, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Social_satire, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Social_prejudice, RDFS.subClassOf, self.Social_Justice))
        self.g.add((self.Privilege, RDFS.subClassOf, self.Social_Justice))

        # 2.s. Sub-hierarchy of Humanism
        self.g.add((self.Human_nature, RDFS.subClassOf, self.Humanism))
        self.g.add((self.Curiosity, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Culture, RDFS.subClassOf, self.Humanism))
        self.g.add((self.Family_and_Grief, RDFS.subClassOf, self.Humanism))
        self.g.add((self.Loss, RDFS.subClassOf, self.Family_and_Grief))
        self.g.add((self.Accidents, RDFS.subClassOf, self.Family_and_Grief))
        self.g.add((self.Existential, RDFS.subClassOf, self.Humanism))
        self.g.add((self.Ability_and_disability, RDFS.subClassOf, self.Humanism))
        self.g.add((self.Physical_handicaps, RDFS.subClassOf, self.Ability_and_disability))
        self.g.add((self.Mistreatment, RDFS.subClassOf, self.Ability_and_disability))

        # 2.t. Sub-hierarchy of Mental health
        self.g.add((self.Mental_illness, RDFS.subClassOf, self.Mental_health))
        self.g.add((self.Suicide, RDFS.subClassOf, self.Mental_health))
        self.g.add((self.Suicide_attempts, RDFS.subClassOf, self.Suicide))
        self.g.add((self.Gossip, RDFS.subClassOf, self.Mental_health))
        self.g.add((self.Rumors, RDFS.subClassOf, self.Gossip))
        self.g.add((self.Descriptions_of_sexual_abuse, RDFS.subClassOf, self.Mental_health))

        # 2.w Sub-hierarchy of Storytelling
        self.g.add((self.Imagination_and_escapism, RDFS.subClassOf, self.Storytelling))
        self.g.add((self.Simplicity, RDFS.subClassOf, self.Storytelling))


        # 3. subgenre
        self.g.add((self.Subgenres, RDFS.subClassOf, self.Subtheme))

        # 3.a Literature
        self.g.add((self.Literature, RDFS.subClassOf, self.Subgenres))
        self.g.add((self.Fiction, RDFS.subClassOf, self.Literature))
        self.g.add((self.Non_fiction, RDFS.subClassOf, self.Literature))
        self.g.add((self.Poetry, RDFS.subClassOf, self.Literature))
        self.g.add((self.Allegory, RDFS.subClassOf, self.Literature))
        self.g.add((self.Satire, RDFS.subClassOf, self.Literature))
        self.g.add((self.American, RDFS.subClassOf, self.Literature))
        self.g.add((self.Unreliable_Narrator, RDFS.subClassOf, self.Literature))
        self.g.add((self.Persuasive, RDFS.subClassOf, self.Literature))
        self.g.add((self.Foreshadowing, RDFS.subClassOf, self.Literature))
        self.g.add((self.Graphic_Novel, RDFS.subClassOf, self.Literature))
        self.g.add((self.Imagery, RDFS.subClassOf, self.Literature))
        self.g.add((self.Metaphorical, RDFS.subClassOf, self.Literature))
        self.g.add((self.Symbolism, RDFS.subClassOf, self.Literature))
        self.g.add((self.Childrens, RDFS.subClassOf, self.Literature))
        self.g.add((self.Animal_story, RDFS.subClassOf, self.Literature))
        self.g.add((self.Literary_reimagining, RDFS.subClassOf, self.Literature))
        self.g.add((self.Film_analysis, RDFS.subClassOf, self.Literature))
        self.g.add((self.Circular_Reporting, RDFS.subClassOf, self.Literature))

        # 3.a.i Fiction
        self.g.add((self.Historical_fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Adventure, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Fable, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Coming_of_Age, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Horror, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Fantasy, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Dystopian_fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Realistic_fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Psychological_fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Mystery, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Speculative, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Classic, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Science_Fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Romance, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Tragedy_subgenre, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Humor, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Multicultural, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Contemporary, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Short_fiction, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Postmodern, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Sports, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Nonsensical, RDFS.subClassOf, self.Fiction))
        self.g.add((self.Epistolary, RDFS.subClassOf, self.Fiction))

        # 3.a.i.1 Historical_fiction
        self.g.add((self.War, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.Medieval, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.Soviet_Union, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.African, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.Indigenous, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.European, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.World_War_II, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.American_South, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.World_War_I, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.Kansas, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.French_and_Indian_War, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self.Post_9_11, RDFS.subClassOf, self.Historical_fiction))
        self.g.add((self._1920s, RDFS.subClassOf, self.Historical_fiction))

        # 3.a.i.1.a War
        self.g.add((self.Violence, RDFS.subClassOf, self.War))
        self.g.add((self.Homecoming, RDFS.subClassOf, self.War))
        self.g.add((self.Heroism, RDFS.subClassOf, self.War))
        self.g.add((self.Heroic, RDFS.subClassOf, self.Heroism))
        self.g.add((self.Mock_heroic, RDFS.subClassOf, self.Heroic))
        self.g.add((self.Heros_journey, RDFS.subClassOf, self.Heroism))

        # 3.a.i.1 Rest of Historical_fiction
        self.g.add((self.Space_Race, RDFS.subClassOf, self.Soviet_Union))
        self.g.add((self.British, RDFS.subClassOf, self.European))
        self.g.add((self.Roman, RDFS.subClassOf, self.European))
        self.g.add((self.English, RDFS.subClassOf, self.European))
        self.g.add((self.Civil_Rights_Movement, RDFS.subClassOf, self.American_South))
        self.g.add((self.Reconstruction_Era, RDFS.subClassOf, self.American_South))
        self.g.add((self.The_Lost_Generation, RDFS.subClassOf, self.World_War_I))

        # 3.a.i. Rest of Fiction
        self.g.add((self.Exploration, RDFS.subClassOf, self.Adventure))
        self.g.add((self.Folklore, RDFS.subClassOf, self.Fable))
        self.g.add((self.Fairytale, RDFS.subClassOf, self.Fable))
        self.g.add((self.Teen_Drama, RDFS.subClassOf, self.Coming_of_Age))
        self.g.add((self.Young_adult_literature, RDFS.subClassOf, self.Teen_Drama))
        self.g.add((self.Bildungsroman, RDFS.subClassOf, self.Coming_of_Age))
        self.g.add((self.Gothic, RDFS.subClassOf, self.Horror))
        self.g.add((self.Superstitions, RDFS.subClassOf, self.Gothic))
        self.g.add((self.Haunting, RDFS.subClassOf, self.Horror))
        self.g.add((self.Dark, RDFS.subClassOf, self.Horror))
        self.g.add((self.Dark_comedy, RDFS.subClassOf, self.Dark))
        self.g.add((self.Dark_romanticism, RDFS.subClassOf, self.Dark))
        self.g.add((self.Supernatural, RDFS.subClassOf, self.Fantasy))
        self.g.add((self.Mythology, RDFS.subClassOf, self.Supernatural))
        self.g.add((self.Dark_fantasy, RDFS.subClassOf, self.Fantasy))
        self.g.add((self.Apocalyptic, RDFS.subClassOf, self.Dystopian_fiction))
        self.g.add((self.Post_apocalyptic, RDFS.subClassOf, self.Dystopian_fiction))
        self.g.add((self.Dark_realism, RDFS.subClassOf, self.Realistic_fiction))
        self.g.add((self.Urban, RDFS.subClassOf, self.Realistic_fiction))
        self.g.add((self.Magical_realism, RDFS.subClassOf, self.Realistic_fiction))
        self.g.add((self.Thriller, RDFS.subClassOf, self.Psychological_fiction))
        self.g.add((self.Suspense, RDFS.subClassOf, self.Psychological_fiction))
        self.g.add((self.Whodunnit, RDFS.subClassOf, self.Mystery))
        self.g.add((self.Locked_room_mystery, RDFS.subClassOf, self.Whodunnit))
        self.g.add((self.Modern_classic, RDFS.subClassOf, self.Classic))
        self.g.add((self.Drama, RDFS.subClassOf, self.Classic))
        self.g.add((self.Historical, RDFS.subClassOf, self.Drama))
        self.g.add((self.Space, RDFS.subClassOf, self.Science_Fiction))
        self.g.add((self.Space_Opera, RDFS.subClassOf, self.Science_Fiction))
        self.g.add((self.Revenge_Love, RDFS.subClassOf, self.Romance))
        self.g.add((self.Forbidden_Love, RDFS.subClassOf, self.Romance))
        self.g.add((self.Dramatic, RDFS.subClassOf, self.Tragedy_subgenre))
        self.g.add((self.Harlem_Renaissance, RDFS.subClassOf, self.Multicultural))
        self.g.add((self.Eye_Dialect, RDFS.subClassOf, self.Multicultural))
        self.g.add((self.Novella, RDFS.subClassOf, self.Short_fiction))
        self.g.add((self.Short_stories, RDFS.subClassOf, self.Short_fiction))
        self.g.add((self.Flash_fiction, RDFS.subClassOf, self.Short_fiction))


        # 3.a.ii Non-fiction
        self.g.add((self.Memoir, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Autobiography, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Narrative, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Social_Science, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Business_and_Economics, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Travel_Writing, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Nature_writing, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.True_Crime, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Speechcraft, RDFS.subClassOf, self.Non_fiction))
        self.g.add((self.Investigative_reporting, RDFS.subClassOf, self.True_Crime))
        self.g.add((self.Debate, RDFS.subClassOf, self.Speechcraft))

        # 3.a.iii Poetry
        self.g.add((self.Elegy, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Rondeau, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Imagism, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Confessional_poetry, RDFS.subClassOf, self.Poetry))
        self.g.add((self.Spoken_word, RDFS.subClassOf, self.Poetry))

        # 3.a. Rest of Literature
        self.g.add((self.Sardonic, RDFS.subClassOf, self.Satire))
        self.g.add((self.Irony, RDFS.subClassOf, self.Satire))
        self.g.add((self.Presidental, RDFS.subClassOf, self.American))
        self.g.add((self.Transcendentalism, RDFS.subClassOf, self.American))
        self.g.add((self.Philosophical, RDFS.subClassOf, self.Persuasive))
        self.g.add((self.Inspirational, RDFS.subClassOf, self.Persuasive))
        self.g.add((self.Anthropomorphism, RDFS.subClassOf, self.Animal_story))

    def get_subtheme_mapping(self, key):
        return self.subtheme_mapping.get(key)

    def get_graph(self):
        return self.g
    
    def save_ontology(self, output_path='data/owls/subtheme.owl'):
        self.g.serialize(output_path, format='xml')
        print(f'Subtheme ontology saved to {output_path}')



if __name__ == '__main__':
    subtheme_ontology = Subtheme()
    subtheme_ontology.create_subtheme_ontology()
    subtheme_ontology.save_ontology()