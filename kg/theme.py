from rdflib import Graph, URIRef, Namespace, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL, XSD
import os

class Theme:
    def __init__(self):
        self.g = Graph()

        self.n = Namespace('https://koncordantlab.com/TTEXTS/')
        self.theme = Namespace('https://koncordantlab.com/TTEXTS/theme/')
        
        self.g.bind('TTEXTS',self.n)
        self.g.bind('theme', self.theme)

        self.Theme = URIRef(self.n.Theme)
        self.Coming_of_age = URIRef(self.theme.Coming_of_age)
        self.Self_discovery = URIRef(self.theme.Self_discovery)
        self.Personal_growth = URIRef(self.theme.Personal_growth)
        self.Confronting_the_past = URIRef(self.theme.Confronting_the_past)
        self.Self_improvement = URIRef(self.theme.Self_improvement)
        self.Purpose = URIRef(self.theme.Purpose)
        self.Courage = URIRef(self.theme.Courage)
        self.The_power_of_voice = URIRef(self.theme.The_power_of_voice)
        self.Advocacy = URIRef(self.theme.Advocacy)
        self.Power_of_words = URIRef(self.theme.Power_of_words)
        self.Storytelling = URIRef(self.theme.Storytelling)
        self.Rhetoric = URIRef(self.theme.Rhetoric)
        self.Rights_to_language = URIRef(self.theme.Rights_to_language)
        self.Heroism_vs_normalcy = URIRef(self.theme.Heroism_vs_normalcy)
        self.Identity = URIRef(self.theme.Identity)
        self.Cultural_identity = URIRef(self.theme.Cultural_identity)
        self.Food_in_culture = URIRef(self.theme.Food_in_culture)
        self.Independence = URIRef(self.theme.Independence)
        self.Dangers_of_naivety = URIRef(self.theme.Dangers_of_naivety)
        self.Youth_vs_Age = URIRef(self.theme.Youth_vs_Age)
        self.Self_expression = URIRef(self.theme.Self_expression)
        self.Sexuality = URIRef(self.theme.Sexuality)
        self.The_impact_of_love_on_identity = URIRef(self.theme.The_impact_of_love_on_identity)
        self.Loss_of_innocence = URIRef(self.theme.Loss_of_innocence)
        self.Consequences_of_actions = URIRef(self.theme.Consequences_of_actions)
        self.The_butterfly_effect = URIRef(self.theme.The_butterfly_effect)
        self.Accountability = URIRef(self.theme.Accountability)
        self.Self_worth = URIRef(self.theme.Self_worth)
        self.Authenticity = URIRef(self.theme.Authenticity)
        self.Isolation = URIRef(self.theme.Isolation)
        self.Alienation = URIRef(self.theme.Alienation)
        self.Phoniness = URIRef(self.theme.Phoniness)
        self.Solitude = URIRef(self.theme.Solitude)
        self.Self_reliance = URIRef(self.theme.Self_reliance)
        self.Anonymity = URIRef(self.theme.Anonymity)
        self.Self_destruction = URIRef(self.theme.Self_destruction)
        self.Community = URIRef(self.theme.Community)
        self.Social_Belonging = URIRef(self.theme.Social_Belonging)
        self.Cultural_belonging = URIRef(self.theme.Cultural_belonging)
        self.Friendship = URIRef(self.theme.Friendship)
        self.Found_Family = URIRef(self.theme.Found_Family)
        self.Unconditional_love = URIRef(self.theme.Unconditional_love)
        self.The_importance_of_human_connection = URIRef(self.theme.The_importance_of_human_connection)
        self.Role_models = URIRef(self.theme.Role_models)
        self.The_myth_of_individual_success = URIRef(self.theme.The_myth_of_individual_success)
        self.Self_consciousness = URIRef(self.theme.Self_consciousness)
        self.Conformity = URIRef(self.theme.Conformity)
        self.Appearance = URIRef(self.theme.Appearance)
        self.The_importance_of_a_home_and_love = URIRef(self.theme.The_importance_of_a_home_and_love)
        self.Race = URIRef(self.theme.Race)
        self.Prejudice = URIRef(self.theme.Prejudice)
        self.Cultural_conflict = URIRef(self.theme.Cultural_conflict)
        self.Racial_Inequality = URIRef(self.theme.Racial_Inequality)
        self.Systemic_racism = URIRef(self.theme.Systemic_racism)
        self.Legacy_of_slavery = URIRef(self.theme.Legacy_of_slavery)
        self.Indigenous_oppression = URIRef(self.theme.Indigenous_oppression)
        self.Racial_injustice = URIRef(self.theme.Racial_injustice)
        self.Facing_racism = URIRef(self.theme.Facing_racism)
        self.Civil_disobedience = URIRef(self.theme.Civil_disobedience)
        self.Rebellion = URIRef(self.theme.Rebellion)
        self.Order_vs_Disorder = URIRef(self.theme.Order_vs_Disorder)
        self.Indigenous_rights = URIRef(self.theme.Indigenous_rights)
        self.Defiance = URIRef(self.theme.Defiance)
        self.Inhumanity_towards_others = URIRef(self.theme.Inhumanity_towards_others)
        self.Hatred = URIRef(self.theme.Hatred)
        self.Equality = URIRef(self.theme.Equality)
        self.Tolerance = URIRef(self.theme.Tolerance)
        self.Diversity = URIRef(self.theme.Diversity)
        self.Immigration = URIRef(self.theme.Immigration)
        self.Totalitarianism = URIRef(self.theme.Totalitarianism)
        self.Leadership = URIRef(self.theme.Leadership)
        self.Unchecked_ambition = URIRef(self.theme.Unchecked_ambition)
        self.Power_and_control = URIRef(self.theme.Power_and_control)
        self.Violence_for_power = URIRef(self.theme.Violence_for_power)
        self.Censorship = URIRef(self.theme.Censorship)
        self.Propaganda = URIRef(self.theme.Propaganda)
        self.Technological_control = URIRef(self.theme.Technological_control)
        self.The_impact_of_technology = URIRef(self.theme.The_impact_of_technology)
        self.Freedom_vs_Control = URIRef(self.theme.Freedom_vs_Control)
        self.The_cost_of_happiness_and_individuality = URIRef(self.theme.The_cost_of_happiness_and_individuality)
        self.Deceit = URIRef(self.theme.Deceit)
        self.Misinformation = URIRef(self.theme.Misinformation)
        self.Public_ignorance = URIRef(self.theme.Public_ignorance)
        self.Corruption = URIRef(self.theme.Corruption)
        self.Pursuit_of_happiness = URIRef(self.theme.Pursuit_of_happiness)
        self.Perseverance = URIRef(self.theme.Perseverance)
        self.Resilience = URIRef(self.theme.Resilience)
        self.Acceptance_of_change = URIRef(self.theme.Acceptance_of_change)
        self.Individuality = URIRef(self.theme.Individuality)
        self.Expectations_vs_Reality = URIRef(self.theme.Expectations_vs_Reality)
        self.Unpredictability = URIRef(self.theme.Unpredictability)
        self.Dreams_vs_Reality = URIRef(self.theme.Dreams_vs_Reality)
        self.Opportunity = URIRef(self.theme.Opportunity)
        self.Class_and_society = URIRef(self.theme.Class_and_society)
        self.Social_class = URIRef(self.theme.Social_class)
        self.Class_corruption = URIRef(self.theme.Class_corruption)
        self.Poverty = URIRef(self.theme.Poverty)
        self.Social_Status = URIRef(self.theme.Social_Status)
        self.The_value_of_reputation = URIRef(self.theme.The_value_of_reputation)
        self.Wealth_gap = URIRef(self.theme.Wealth_gap)
        self.Ambition = URIRef(self.theme.Ambition)
        self.Greed = URIRef(self.theme.Greed)
        self.Toxic_capitalism = URIRef(self.theme.Toxic_capitalism)
        self.Greed_vs_Selflessness = URIRef(self.theme.Greed_vs_Selflessness)
        self.Wealth_vs_Value = URIRef(self.theme.Wealth_vs_Value)
        self.Corporations = URIRef(self.theme.Corporations)
        self.Consumerism = URIRef(self.theme.Consumerism)
        self.Human_nature = URIRef(self.theme.Human_nature)
        self.Revenge = URIRef(self.theme.Revenge)
        self.Guilt = URIRef(self.theme.Guilt)
        self.Revenge_love = URIRef(self.theme.Revenge_love)
        self.Betrayal = URIRef(self.theme.Betrayal)
        self.Betrayal_vs_Loyalty = URIRef(self.theme.Betrayal_vs_Loyalty)
        self.The_power_of_the_mind = URIRef(self.theme.The_power_of_the_mind)
        self.Imagination = URIRef(self.theme.Imagination)
        self.Creativity = URIRef(self.theme.Creativity)
        self.Innovation = URIRef(self.theme.Innovation)
        self.Intelligence = URIRef(self.theme.Intelligence)
        self.Strategy = URIRef(self.theme.Strategy)
        self.Memory = URIRef(self.theme.Memory)
        self.Disconnection_between_body_and_mind = URIRef(self.theme.Disconnection_between_body_and_mind)
        self.Fate_vs_Free_will = URIRef(self.theme.Fate_vs_Free_will)
        self.Dangers_of_tempting_fate = URIRef(self.theme.Dangers_of_tempting_fate)
        self.Destiny = URIRef(self.theme.Destiny)
        self.Limits_of_human_agency = URIRef(self.theme.Limits_of_human_agency)
        self.Fate_and_foreknowledge = URIRef(self.theme.Fate_and_foreknowledge)
        self.Limits_of_knowledge = URIRef(self.theme.Limits_of_knowledge)
        self.Judgement = URIRef(self.theme.Judgement)
        self.Stereotypes = URIRef(self.theme.Stereotypes)
        self.Pride = URIRef(self.theme.Pride)
        self.Consequences_of_selfishness = URIRef(self.theme.Consequences_of_selfishness)
        self.Vanity = URIRef(self.theme.Vanity)
        self.Superficiality_of_beauty = URIRef(self.theme.Superficiality_of_beauty)
        self.Humility = URIRef(self.theme.Humility)
        self.Dignity = URIRef(self.theme.Dignity)
        self.Arrogance = URIRef(self.theme.Arrogance)
        self.Jealousy = URIRef(self.theme.Jealousy)
        self.The_passage_of_time = URIRef(self.theme.The_passage_of_time)
        self.Finding_beauty_in_the_everyday = URIRef(self.theme.Finding_beauty_in_the_everyday)
        self.Urgency_of_action = URIRef(self.theme.Urgency_of_action)
        self.Lost_opportunities = URIRef(self.theme.Lost_opportunities)
        self.Gratitude = URIRef(self.theme.Gratitude)
        self.Madness = URIRef(self.theme.Madness)
        self.Obsession = URIRef(self.theme.Obsession)
        self.Compassion = URIRef(self.theme.Compassion)
        self.Forgiveness = URIRef(self.theme.Forgiveness)
        self.Apology = URIRef(self.theme.Apology)
        self.Empathy = URIRef(self.theme.Empathy)
        self.Redemption = URIRef(self.theme.Redemption)
        self.Overcoming_adversity = URIRef(self.theme.Overcoming_adversity)
        self.Kindness = URIRef(self.theme.Kindness)
        self.Respect = URIRef(self.theme.Respect)
        self.Cruelty_vs_Kindness = URIRef(self.theme.Cruelty_vs_Kindness)
        self.Love = URIRef(self.theme.Love)
        self.Sacrifice = URIRef(self.theme.Sacrifice)
        self.Selflessness = URIRef(self.theme.Selflessness)
        self.Love_vs_Self_interest = URIRef(self.theme.Love_vs_Self_interest)
        self.Love_vs_Hate = URIRef(self.theme.Love_vs_Hate)
        self.Relationships = URIRef(self.theme.Relationships)
        self.Altruism_vs_self_interest = URIRef(self.theme.Altruism_vs_self_interest)
        self.Honor = URIRef(self.theme.Honor)
        self.Victory = URIRef(self.theme.Victory)
        self.Loyalty = URIRef(self.theme.Loyalty)
        self.Motherhood = URIRef(self.theme.Motherhood)
        self.Human_insignificance = URIRef(self.theme.Human_insignificance)
        self.Universe_indifference = URIRef(self.theme.Universe_indifference)
        self.Dishonesty = URIRef(self.theme.Dishonesty)
        self.Hypocrisy = URIRef(self.theme.Hypocrisy)
        self.Tradition = URIRef(self.theme.Tradition)
        self.Sacrifice_for_family = URIRef(self.theme.Sacrifice_for_family)
        self.Gender = URIRef(self.theme.Gender)
        self.Gender_Roles = URIRef(self.theme.Gender_Roles)
        self.Marriage = URIRef(self.theme.Marriage)
        self.Martial_expectations = URIRef(self.theme.Martial_expectations)
        self.Domesticity = URIRef(self.theme.Domesticity)
        self.Chivalry = URIRef(self.theme.Chivalry)
        self.Patriarchal_control = URIRef(self.theme.Patriarchal_control)
        self.Masculinity = URIRef(self.theme.Masculinity)
        self.Legacy_of_heritage = URIRef(self.theme.Legacy_of_heritage)
        self.Blind_tradition = URIRef(self.theme.Blind_tradition)
        self.Tradition_vs_Change = URIRef(self.theme.Tradition_vs_Change)
        self.Generational_divide = URIRef(self.theme.Generational_divide)
        self.Familial_expectations = URIRef(self.theme.Familial_expectations)
        self.Morality = URIRef(self.theme.Morality)
        self.The_danger_of_temptation = URIRef(self.theme.The_danger_of_temptation)
        self.Personal_and_public_truth = URIRef(self.theme.Personal_and_public_truth)
        self.The_cruelty_of_bullying = URIRef(self.theme.The_cruelty_of_bullying)
        self.Complexity_of_childhood_behavior = URIRef(self.theme.Complexity_of_childhood_behavior)
        self.Moral_Responsibility = URIRef(self.theme.Moral_Responsibility)
        self.Human_impact_on_the_environment = URIRef(self.theme.Human_impact_on_the_environment)
        self.The_nature_of_evil = URIRef(self.theme.The_nature_of_evil)
        self.Dark_side_of_human_nature = URIRef(self.theme.Dark_side_of_human_nature)
        self.Good_vs_Evil = URIRef(self.theme.Good_vs_Evil)
        self.Crime = URIRef(self.theme.Crime)
        self.Ethics_of_science_experimentation = URIRef(self.theme.Ethics_of_science_experimentation)
        self.Morality_in_war = URIRef(self.theme.Morality_in_war)
        self.Burdens_of_war = URIRef(self.theme.Burdens_of_war)
        self.Nuclear_war = URIRef(self.theme.Nuclear_war)
        self.Moral_corruption = URIRef(self.theme.Moral_corruption)
        self.Tragedy = URIRef(self.theme.Tragedy)
        self.Survival = URIRef(self.theme.Survival)
        self.Man_vs_Nature = URIRef(self.theme.Man_vs_Nature)
        self.Nature_as_a_force = URIRef(self.theme.Nature_as_a_force)
        self.Civilization_vs_The_wild = URIRef(self.theme.Civilization_vs_The_wild)
        self.Resourcefulness = URIRef(self.theme.Resourcefulness)
        self.Civilization_vs_Barbarism = URIRef(self.theme.Civilization_vs_Barbarism)
        self.Primal_instincts = URIRef(self.theme.Primal_instincts)
        self.Savagery_vs_Civilization = URIRef(self.theme.Savagery_vs_Civilization)
        self.Mortality = URIRef(self.theme.Mortality)
        self.Fragility_of_life = URIRef(self.theme.Fragility_of_life)
        self.The_value_of_life = URIRef(self.theme.The_value_of_life)
        self.Aging = URIRef(self.theme.Aging)
        self.Death = URIRef(self.theme.Death)
        self.Grief = URIRef(self.theme.Grief)
        self.Spirituality = URIRef(self.theme.Spirituality)
        self.Immortality = URIRef(self.theme.Immortality)
        self.Healing = URIRef(self.theme.Healing)
        self.Mass_Hysteria = URIRef(self.theme.Mass_Hysteria)
        self.The_supernatural = URIRef(self.theme.The_supernatural)
        self.Superstition_vs_Reality = URIRef(self.theme.Superstition_vs_Reality)
        self.Fear_of_the_unknown = URIRef(self.theme.Fear_of_the_unknown)
        self.Faith_vs_Knowledge = URIRef(self.theme.Faith_vs_Knowledge)
        self.Gods_Will = URIRef(self.theme.Gods_Will)
        self.Divine_Intervention = URIRef(self.theme.Divine_Intervention)
        self.Abuse = URIRef(self.theme.Abuse)
        self.Silence = URIRef(self.theme.Silence)
        self.Cycle_of_Violence = URIRef(self.theme.Cycle_of_Violence)
        self.Child_labor = URIRef(self.theme.Child_labor)
        self.Justice = URIRef(self.theme.Justice)
        self.The_struggle_for_justice = URIRef(self.theme.The_struggle_for_justice)
        self.Nationalism = URIRef(self.theme.Nationalism)
        self.Patriotism = URIRef(self.theme.Patriotism)
        self.Duality = URIRef(self.theme.Duality)
        self.Logical_Paradox = URIRef(self.theme.Logical_Paradox)
        self.Fact_vs_Fiction = URIRef(self.theme.Fact_vs_Fiction)
        self.Technological_advancements = URIRef(self.theme.Technological_advancements)
        self.Scientific_curiosity = URIRef(self.theme.Scientific_curiosity)
        self.Nature_theme = URIRef(self.theme.Nature)
        self.The_role_of_nature = URIRef(self.theme.The_role_of_nature)
        self.Connection_to_nature = URIRef(self.theme.Connection_to_nature)
        self.Religious_Oppression = URIRef(self.theme.Religious_Oppression)
        self.Experience_of_Art = URIRef(self.theme.Experience_of_Art)
        self.Education = URIRef(self.theme.Education)
        self.Democracy = URIRef(self.theme.Democracy)
        self.Health = URIRef(self.theme.Health)
        self.Food_Safety = URIRef(self.theme.Food_Safety)
        self.Physical_activity_and_movement = URIRef(self.theme.Physical_activity_and_movement)


        self.theme_mapping = {
            "coming of age": self.Coming_of_age,
            "self discovery": self.Self_discovery,
            "personal growth": self.Personal_growth,
            "confronting the past": self.Confronting_the_past,
            "self improvement": self.Self_improvement,
            "purpose": self.Purpose,
            "courage": self.Courage,
            "the power of voice": self.The_power_of_voice,
            "advocacy": self.Advocacy,
            "power of words": self.Power_of_words,
            "the power of words": self.Power_of_words,
            "storytelling": self.Storytelling,
            "rhetoric": self.Rhetoric,
            "rights to language": self.Rights_to_language,
            "importance of language": self.Rights_to_language,
            "the importance of language": self.Rights_to_language,
            "the power of language": self.Rights_to_language,
            "heroism vs normalcy": self.Heroism_vs_normalcy,
            "identity": self.Identity,
            "cultural identity": self.Cultural_identity,
            "food in culture": self.Food_in_culture,
            "independence": self.Independence,
            "dangers of naivety": self.Dangers_of_naivety,
            "youth vs age": self.Youth_vs_Age,
            "self expression": self.Self_expression,
            "sexuality": self.Sexuality,
            "the impact of love on identity": self.The_impact_of_love_on_identity,
            "loss of innocence": self.Loss_of_innocence,
            "consequences of actions": self.Consequences_of_actions,
            "the butterfly effect": self.The_butterfly_effect,
            "accountability": self.Accountability,
            "self worth": self.Self_worth,
            "authenticity": self.Authenticity,
            "isolation": self.Isolation,
            "alienation": self.Alienation,
            "phoniness": self.Phoniness,
            "solitude": self.Solitude,
            "self reliance": self.Self_reliance,
            "anonymity": self.Anonymity,
            "self destruction": self.Self_destruction,
            "destruction": self.Self_destruction,
            "community": self.Community,
            "social belonging": self.Social_Belonging,
            "cultural belonging": self.Cultural_belonging,
            "friendship": self.Friendship,
            "found family": self.Found_Family,
            "family": self.Found_Family,
            "unconditional love": self.Unconditional_love,
            "the importance of human connection": self.The_importance_of_human_connection,
            "human connection": self.The_importance_of_human_connection,
            "role models": self.Role_models,
            "the myth of individual success": self.The_myth_of_individual_success,
            "self consciousness": self.Self_consciousness,
            "conformity": self.Conformity,
            "appearance": self.Appearance,
            "the importance of a home and love": self.The_importance_of_a_home_and_love,
            "race": self.Race,
            "prejudice": self.Prejudice,
            "cultural conflict": self.Cultural_conflict,
            "racial inequality": self.Racial_Inequality,
            "systemic racism": self.Systemic_racism,
            "legacy of slavery": self.Legacy_of_slavery,
            "indigenous oppression": self.Indigenous_oppression,
            "racial injustice": self.Racial_injustice,
            "facing racism": self.Facing_racism,
            "racism": self.Facing_racism,
            "civil disobedience": self.Civil_disobedience,
            "rebellion": self.Rebellion,
            "order vs disorder": self.Order_vs_Disorder,
            "indigenous rights": self.Indigenous_rights,
            "defiance": self.Defiance,
            "inhumanity towards others": self.Inhumanity_towards_others,
            "hatred": self.Hatred,
            "equality": self.Equality,
            "tolerance": self.Tolerance,
            "diversity": self.Diversity,
            "immigration": self.Immigration,
            "totalitarianism": self.Totalitarianism,
            "leadership": self.Leadership,
            "unchecked ambition": self.Unchecked_ambition,
            "power and control": self.Power_and_control,
            "violence for power": self.Violence_for_power,
            "censorship": self.Censorship,
            "propaganda": self.Propaganda,
            "technological control": self.Technological_control,
            "the impact of technology": self.The_impact_of_technology,
            "freedom vs control": self.Freedom_vs_Control,
            "freedom": self.Freedom_vs_Control,
            "the cost of happiness and individuality": self.The_cost_of_happiness_and_individuality,
            "deceit": self.Deceit,
            "misinformation": self.Misinformation,
            "public ignorance": self.Public_ignorance,
            "corruption": self.Corruption,
            "pursuit of happiness": self.Pursuit_of_happiness,
            "perseverance": self.Perseverance,
            "resilience": self.Resilience,
            "acceptance of change": self.Acceptance_of_change,
            "individuality": self.Individuality,
            "expectations vs reality": self.Expectations_vs_Reality,
            "unpredictability": self.Unpredictability,
            "dreams vs reality": self.Dreams_vs_Reality,
            "opportunity": self.Opportunity,
            "class and society": self.Class_and_society,
            "social class": self.Social_class,
            "class corruption": self.Class_corruption,
            "poverty": self.Poverty,
            "social status": self.Social_Status,
            "the value of reputation": self.The_value_of_reputation,
            "wealth gap": self.Wealth_gap,
            "ambition": self.Ambition,
            "greed": self.Greed,
            "toxic capitalism": self.Toxic_capitalism,
            "greed vs selflessness": self.Greed_vs_Selflessness,
            "wealth vs value": self.Wealth_vs_Value,
            "corporations": self.Corporations,
            "consumerism": self.Consumerism,
            "human nature": self.Human_nature,
            "revenge": self.Revenge,
            "guilt": self.Guilt,
            "revenge love": self.Revenge_love,
            "betrayal": self.Betrayal,
            "betrayal vs loyalty": self.Betrayal_vs_Loyalty,
            "the power of the mind": self.The_power_of_the_mind,
            "imagination": self.Imagination,
            "creativity": self.Creativity,
            "innovation": self.Innovation,
            "intelligence": self.Intelligence,
            "strategy": self.Strategy,
            "memory": self.Memory,
            "disconnection between body and mind": self.Disconnection_between_body_and_mind,
            "fate vs free will": self.Fate_vs_Free_will,
            "dangers of tempting fate": self.Dangers_of_tempting_fate,
            "destiny": self.Destiny,
            "limits of human agency": self.Limits_of_human_agency,
            "fate and foreknowledge": self.Fate_and_foreknowledge,
            "limits of knowledge": self.Limits_of_knowledge,
            "judgement": self.Judgement,
            "stereotypes": self.Stereotypes,
            "pride": self.Pride,
            "consequences of selfishness": self.Consequences_of_selfishness,
            "vanity": self.Vanity,
            "superficiality of beauty": self.Superficiality_of_beauty,
            "humility": self.Humility,
            "dignity": self.Dignity,
            "arrogance": self.Arrogance,
            "jealousy": self.Jealousy,
            "the passage of time": self.The_passage_of_time,
            "finding beauty in the everyday": self.Finding_beauty_in_the_everyday,
            "urgency of action": self.Urgency_of_action,
            "lost opportunities": self.Lost_opportunities,
            "gratitude": self.Gratitude,
            "madness": self.Madness,
            "obsession": self.Obsession,
            "compassion": self.Compassion,
            "forgiveness": self.Forgiveness,
            "apology": self.Apology,
            "empathy": self.Empathy,
            "redemption": self.Redemption,
            "overcoming adversity": self.Overcoming_adversity,
            "kindness": self.Kindness,
            "respect": self.Respect,
            "cruelty vs kindness": self.Cruelty_vs_Kindness,
            "love": self.Love,
            "sacrifice": self.Sacrifice,
            "selflessness": self.Selflessness,
            "love vs self interest": self.Love_vs_Self_interest,
            "love vs hate": self.Love_vs_Hate,
            "relationships": self.Relationships,
            "altruism vs self interest": self.Altruism_vs_self_interest,
            "honor": self.Honor,
            "victory": self.Victory,
            "loyalty": self.Loyalty,
            "motherhood": self.Motherhood,
            "human insignificance": self.Human_insignificance,
            "universe indifference": self.Universe_indifference,
            "dishonesty": self.Dishonesty,
            "hypocrisy": self.Hypocrisy,
            "tradition": self.Tradition,
            "sacrifice for family": self.Sacrifice_for_family,
            "gender": self.Gender,
            "gender roles": self.Gender_Roles,
            "marriage": self.Marriage,
            "martial expectations": self.Martial_expectations,
            "domesticity": self.Domesticity,
            "chivalry": self.Chivalry,
            "patriarchal control": self.Patriarchal_control,
            "masculinity": self.Masculinity,
            "legacy of heritage": self.Legacy_of_heritage,
            "blind tradition": self.Blind_tradition,
            "tradition vs change": self.Tradition_vs_Change,
            "generational divide": self.Generational_divide,
            "familial expectations": self.Familial_expectations,
            "morality": self.Morality,
            "the danger of temptation": self.The_danger_of_temptation,
            "the dangers of temptation": self.The_danger_of_temptation,
            "personal and public truth": self.Personal_and_public_truth,
            "the cruelty of bullying": self.The_cruelty_of_bullying,
            "complexity of childhood behavior": self.Complexity_of_childhood_behavior,
            "moral responsibility": self.Moral_Responsibility,
            "human impact on the environment": self.Human_impact_on_the_environment,
            "the nature of evil": self.The_nature_of_evil,
            "dark side of human nature": self.Dark_side_of_human_nature,
            "good vs evil": self.Good_vs_Evil,
            "crime": self.Crime,
            "ethics of science experimentation": self.Ethics_of_science_experimentation,
            "morality in war": self.Morality_in_war,
            "war": self.Morality_in_war,
            "burdens of war": self.Burdens_of_war,
            "nuclear war": self.Nuclear_war,
            "moral corruption": self.Moral_corruption,
            "tragedy": self.Tragedy,
            "survival": self.Survival,
            "man vs nature": self.Man_vs_Nature,
            "nature as a force": self.Nature_as_a_force,
            "civilization vs the wild": self.Civilization_vs_The_wild,
            "resourcefulness": self.Resourcefulness,
            "civilization vs barbarism": self.Civilization_vs_Barbarism,
            "primal instincts": self.Primal_instincts,
            "savagery vs civilization": self.Savagery_vs_Civilization,
            "mortality": self.Mortality,
            "fragility of life": self.Fragility_of_life,
            "the value of life": self.The_value_of_life,
            "aging": self.Aging,
            "death": self.Death,
            "grief": self.Grief,
            "spirituality": self.Spirituality,
            "immortality": self.Immortality,
            "healing": self.Healing,
            "mass hysteria": self.Mass_Hysteria,
            "the supernatural": self.The_supernatural,
            "superstition vs reality": self.Superstition_vs_Reality,
            "fear of the unknown": self.Fear_of_the_unknown,
            "fear": self.Fear_of_the_unknown,
            "faith vs knowledge": self.Faith_vs_Knowledge,
            "faith": self.Faith_vs_Knowledge,
            "god's will": self.Gods_Will,
            "divine intervention": self.Divine_Intervention,
            "abuse": self.Abuse,
            "silence": self.Silence,
            "cycle of violence": self.Cycle_of_Violence,
            "child labor": self.Child_labor,
            "justice": self.Justice,
            "the struggle for justice": self.The_struggle_for_justice,
            "nationalism": self.Nationalism,
            "patriotism": self.Patriotism,
            "duality": self.Duality,
            "logical paradox": self.Logical_Paradox,
            "fact vs fiction": self.Fact_vs_Fiction,
            "technological advancements": self.Technological_advancements,
            "scientific curiosity": self.Scientific_curiosity,
            "nature": self.Nature_theme,
            "the role of nature": self.The_role_of_nature,
            "connection to nature": self.Connection_to_nature,
            "religious oppression": self.Religious_Oppression,
            "experience of art": self.Experience_of_Art,
            "art vs nature": self.Experience_of_Art,
            "music": self.Experience_of_Art,
            "education": self.Education,
            "democrac": self.Democracy,
            "health": self.Health,
            "food safety": self.Food_Safety,
            "physical activity and movement": self.Physical_activity_and_movement
        }


    def create_theme_ontology(self):
        self.g.add((self.Theme, RDF.type, OWL.Class))
        self.g.add((self.Coming_of_age, RDF.type, OWL.Class))
        self.g.add((self.Self_discovery, RDF.type, OWL.Class))
        self.g.add((self.Personal_growth, RDF.type, OWL.Class))
        self.g.add((self.Confronting_the_past, RDF.type, OWL.Class))
        self.g.add((self.Self_improvement, RDF.type, OWL.Class))
        self.g.add((self.Purpose, RDF.type, OWL.Class))
        self.g.add((self.Courage, RDF.type, OWL.Class))
        self.g.add((self.The_power_of_voice, RDF.type, OWL.Class))
        self.g.add((self.Advocacy, RDF.type, OWL.Class))
        self.g.add((self.Power_of_words, RDF.type, OWL.Class))
        self.g.add((self.Storytelling, RDF.type, OWL.Class))
        self.g.add((self.Rhetoric, RDF.type, OWL.Class))
        self.g.add((self.Rights_to_language, RDF.type, OWL.Class))
        self.g.add((self.Heroism_vs_normalcy, RDF.type, OWL.Class))
        self.g.add((self.Identity, RDF.type, OWL.Class))
        self.g.add((self.Cultural_identity, RDF.type, OWL.Class))
        self.g.add((self.Food_in_culture, RDF.type, OWL.Class))
        self.g.add((self.Independence, RDF.type, OWL.Class))
        self.g.add((self.Dangers_of_naivety, RDF.type, OWL.Class))
        self.g.add((self.Youth_vs_Age, RDF.type, OWL.Class))
        self.g.add((self.Self_expression, RDF.type, OWL.Class))
        self.g.add((self.Sexuality, RDF.type, OWL.Class))
        self.g.add((self.The_impact_of_love_on_identity, RDF.type, OWL.Class))
        self.g.add((self.Loss_of_innocence, RDF.type, OWL.Class))
        self.g.add((self.Consequences_of_actions, RDF.type, OWL.Class))
        self.g.add((self.The_butterfly_effect, RDF.type, OWL.Class))
        self.g.add((self.Accountability, RDF.type, OWL.Class))
        self.g.add((self.Self_worth, RDF.type, OWL.Class))
        self.g.add((self.Authenticity, RDF.type, OWL.Class))
        self.g.add((self.Isolation, RDF.type, OWL.Class))
        self.g.add((self.Alienation, RDF.type, OWL.Class))
        self.g.add((self.Phoniness, RDF.type, OWL.Class))
        self.g.add((self.Solitude, RDF.type, OWL.Class))
        self.g.add((self.Self_reliance, RDF.type, OWL.Class))
        self.g.add((self.Anonymity, RDF.type, OWL.Class))
        self.g.add((self.Self_destruction, RDF.type, OWL.Class))
        self.g.add((self.Community, RDF.type, OWL.Class))
        self.g.add((self.Social_Belonging, RDF.type, OWL.Class))
        self.g.add((self.Cultural_belonging, RDF.type, OWL.Class))
        self.g.add((self.Friendship, RDF.type, OWL.Class))
        self.g.add((self.Found_Family, RDF.type, OWL.Class))
        self.g.add((self.Unconditional_love, RDF.type, OWL.Class))
        self.g.add((self.The_importance_of_human_connection, RDF.type, OWL.Class))
        self.g.add((self.Role_models, RDF.type, OWL.Class))
        self.g.add((self.The_myth_of_individual_success, RDF.type, OWL.Class))
        self.g.add((self.Self_consciousness, RDF.type, OWL.Class))
        self.g.add((self.Conformity, RDF.type, OWL.Class))
        self.g.add((self.Appearance, RDF.type, OWL.Class))
        self.g.add((self.The_importance_of_a_home_and_love, RDF.type, OWL.Class))
        self.g.add((self.Race, RDF.type, OWL.Class))
        self.g.add((self.Prejudice, RDF.type, OWL.Class))
        self.g.add((self.Cultural_conflict, RDF.type, OWL.Class))
        self.g.add((self.Racial_Inequality, RDF.type, OWL.Class))
        self.g.add((self.Systemic_racism, RDF.type, OWL.Class))
        self.g.add((self.Legacy_of_slavery, RDF.type, OWL.Class))
        self.g.add((self.Indigenous_oppression, RDF.type, OWL.Class))
        self.g.add((self.Racial_injustice, RDF.type, OWL.Class))
        self.g.add((self.Facing_racism, RDF.type, OWL.Class))
        self.g.add((self.Civil_disobedience, RDF.type, OWL.Class))
        self.g.add((self.Rebellion, RDF.type, OWL.Class))
        self.g.add((self.Order_vs_Disorder, RDF.type, OWL.Class))
        self.g.add((self.Indigenous_rights, RDF.type, OWL.Class))
        self.g.add((self.Defiance, RDF.type, OWL.Class))
        self.g.add((self.Inhumanity_towards_others, RDF.type, OWL.Class))
        self.g.add((self.Hatred, RDF.type, OWL.Class))
        self.g.add((self.Equality, RDF.type, OWL.Class))
        self.g.add((self.Tolerance, RDF.type, OWL.Class))
        self.g.add((self.Diversity, RDF.type, OWL.Class))
        self.g.add((self.Immigration, RDF.type, OWL.Class))
        self.g.add((self.Totalitarianism, RDF.type, OWL.Class))
        self.g.add((self.Leadership, RDF.type, OWL.Class))
        self.g.add((self.Unchecked_ambition, RDF.type, OWL.Class))
        self.g.add((self.Power_and_control, RDF.type, OWL.Class))
        self.g.add((self.Violence_for_power, RDF.type, OWL.Class))
        self.g.add((self.Censorship, RDF.type, OWL.Class))
        self.g.add((self.Propaganda, RDF.type, OWL.Class))
        self.g.add((self.Technological_control, RDF.type, OWL.Class))
        self.g.add((self.The_impact_of_technology, RDF.type, OWL.Class))
        self.g.add((self.Freedom_vs_Control, RDF.type, OWL.Class))
        self.g.add((self.The_cost_of_happiness_and_individuality, RDF.type, OWL.Class))
        self.g.add((self.Deceit, RDF.type, OWL.Class))
        self.g.add((self.Misinformation, RDF.type, OWL.Class))
        self.g.add((self.Public_ignorance, RDF.type, OWL.Class))
        self.g.add((self.Corruption, RDF.type, OWL.Class))
        self.g.add((self.Pursuit_of_happiness, RDF.type, OWL.Class))
        self.g.add((self.Perseverance, RDF.type, OWL.Class))
        self.g.add((self.Resilience, RDF.type, OWL.Class))
        self.g.add((self.Acceptance_of_change, RDF.type, OWL.Class))
        self.g.add((self.Individuality, RDF.type, OWL.Class))
        self.g.add((self.Expectations_vs_Reality, RDF.type, OWL.Class))
        self.g.add((self.Unpredictability, RDF.type, OWL.Class))
        self.g.add((self.Dreams_vs_Reality, RDF.type, OWL.Class))
        self.g.add((self.Opportunity, RDF.type, OWL.Class))
        self.g.add((self.Class_and_society, RDF.type, OWL.Class))
        self.g.add((self.Social_class, RDF.type, OWL.Class))
        self.g.add((self.Class_corruption, RDF.type, OWL.Class))
        self.g.add((self.Poverty, RDF.type, OWL.Class))
        self.g.add((self.Social_Status, RDF.type, OWL.Class))
        self.g.add((self.The_value_of_reputation, RDF.type, OWL.Class))
        self.g.add((self.Wealth_gap, RDF.type, OWL.Class))
        self.g.add((self.Ambition, RDF.type, OWL.Class))
        self.g.add((self.Greed, RDF.type, OWL.Class))
        self.g.add((self.Toxic_capitalism, RDF.type, OWL.Class))
        self.g.add((self.Greed_vs_Selflessness, RDF.type, OWL.Class))
        self.g.add((self.Wealth_vs_Value, RDF.type, OWL.Class))
        self.g.add((self.Corporations, RDF.type, OWL.Class))
        self.g.add((self.Consumerism, RDF.type, OWL.Class))
        self.g.add((self.Human_nature, RDF.type, OWL.Class))
        self.g.add((self.Revenge, RDF.type, OWL.Class))
        self.g.add((self.Guilt, RDF.type, OWL.Class))
        self.g.add((self.Revenge_love, RDF.type, OWL.Class))
        self.g.add((self.Betrayal, RDF.type, OWL.Class))
        self.g.add((self.Betrayal_vs_Loyalty, RDF.type, OWL.Class))
        self.g.add((self.The_power_of_the_mind, RDF.type, OWL.Class))
        self.g.add((self.Imagination, RDF.type, OWL.Class))
        self.g.add((self.Creativity, RDF.type, OWL.Class))
        self.g.add((self.Innovation, RDF.type, OWL.Class))
        self.g.add((self.Intelligence, RDF.type, OWL.Class))
        self.g.add((self.Strategy, RDF.type, OWL.Class))
        self.g.add((self.Memory, RDF.type, OWL.Class))
        self.g.add((self.Disconnection_between_body_and_mind, RDF.type, OWL.Class))
        self.g.add((self.Fate_vs_Free_will, RDF.type, OWL.Class))
        self.g.add((self.Dangers_of_tempting_fate, RDF.type, OWL.Class))
        self.g.add((self.Destiny, RDF.type, OWL.Class))
        self.g.add((self.Limits_of_human_agency, RDF.type, OWL.Class))
        self.g.add((self.Fate_and_foreknowledge, RDF.type, OWL.Class))
        self.g.add((self.Limits_of_knowledge, RDF.type, OWL.Class))
        self.g.add((self.Judgement, RDF.type, OWL.Class))
        self.g.add((self.Stereotypes, RDF.type, OWL.Class))
        self.g.add((self.Pride, RDF.type, OWL.Class))
        self.g.add((self.Consequences_of_selfishness, RDF.type, OWL.Class))
        self.g.add((self.Vanity, RDF.type, OWL.Class))
        self.g.add((self.Superficiality_of_beauty, RDF.type, OWL.Class))
        self.g.add((self.Humility, RDF.type, OWL.Class))
        self.g.add((self.Dignity, RDF.type, OWL.Class))
        self.g.add((self.Arrogance, RDF.type, OWL.Class))
        self.g.add((self.Jealousy, RDF.type, OWL.Class))
        self.g.add((self.The_passage_of_time, RDF.type, OWL.Class))
        self.g.add((self.Finding_beauty_in_the_everyday, RDF.type, OWL.Class))
        self.g.add((self.Urgency_of_action, RDF.type, OWL.Class))
        self.g.add((self.Lost_opportunities, RDF.type, OWL.Class))
        self.g.add((self.Gratitude, RDF.type, OWL.Class))
        self.g.add((self.Madness, RDF.type, OWL.Class))
        self.g.add((self.Obsession, RDF.type, OWL.Class))
        self.g.add((self.Compassion, RDF.type, OWL.Class))
        self.g.add((self.Forgiveness, RDF.type, OWL.Class))
        self.g.add((self.Apology, RDF.type, OWL.Class))
        self.g.add((self.Empathy, RDF.type, OWL.Class))
        self.g.add((self.Redemption, RDF.type, OWL.Class))
        self.g.add((self.Overcoming_adversity, RDF.type, OWL.Class))
        self.g.add((self.Kindness, RDF.type, OWL.Class))
        self.g.add((self.Respect, RDF.type, OWL.Class))
        self.g.add((self.Cruelty_vs_Kindness, RDF.type, OWL.Class))
        self.g.add((self.Love, RDF.type, OWL.Class))
        self.g.add((self.Sacrifice, RDF.type, OWL.Class))
        self.g.add((self.Selflessness, RDF.type, OWL.Class))
        self.g.add((self.Love_vs_Self_interest, RDF.type, OWL.Class))
        self.g.add((self.Love_vs_Hate, RDF.type, OWL.Class))
        self.g.add((self.Relationships, RDF.type, OWL.Class))
        self.g.add((self.Altruism_vs_self_interest, RDF.type, OWL.Class))
        self.g.add((self.Honor, RDF.type, OWL.Class))
        self.g.add((self.Victory, RDF.type, OWL.Class))
        self.g.add((self.Loyalty, RDF.type, OWL.Class))
        self.g.add((self.Motherhood, RDF.type, OWL.Class))
        self.g.add((self.Human_insignificance, RDF.type, OWL.Class))
        self.g.add((self.Universe_indifference, RDF.type, OWL.Class))
        self.g.add((self.Dishonesty, RDF.type, OWL.Class))
        self.g.add((self.Hypocrisy, RDF.type, OWL.Class))
        self.g.add((self.Tradition, RDF.type, OWL.Class))
        self.g.add((self.Sacrifice_for_family, RDF.type, OWL.Class))
        self.g.add((self.Gender, RDF.type, OWL.Class))
        self.g.add((self.Gender_Roles, RDF.type, OWL.Class))
        self.g.add((self.Marriage, RDF.type, OWL.Class))
        self.g.add((self.Martial_expectations, RDF.type, OWL.Class))
        self.g.add((self.Domesticity, RDF.type, OWL.Class))
        self.g.add((self.Chivalry, RDF.type, OWL.Class))
        self.g.add((self.Patriarchal_control, RDF.type, OWL.Class))
        self.g.add((self.Masculinity, RDF.type, OWL.Class))
        self.g.add((self.Legacy_of_heritage, RDF.type, OWL.Class))
        self.g.add((self.Blind_tradition, RDF.type, OWL.Class))
        self.g.add((self.Tradition_vs_Change, RDF.type, OWL.Class))
        self.g.add((self.Generational_divide, RDF.type, OWL.Class))
        self.g.add((self.Familial_expectations, RDF.type, OWL.Class))
        self.g.add((self.Morality, RDF.type, OWL.Class))
        self.g.add((self.The_danger_of_temptation, RDF.type, OWL.Class))
        self.g.add((self.Personal_and_public_truth, RDF.type, OWL.Class))
        self.g.add((self.The_cruelty_of_bullying, RDF.type, OWL.Class))
        self.g.add((self.Complexity_of_childhood_behavior, RDF.type, OWL.Class))
        self.g.add((self.Moral_Responsibility, RDF.type, OWL.Class))
        self.g.add((self.Human_impact_on_the_environment, RDF.type, OWL.Class))
        self.g.add((self.The_nature_of_evil, RDF.type, OWL.Class))
        self.g.add((self.Dark_side_of_human_nature, RDF.type, OWL.Class))
        self.g.add((self.Good_vs_Evil, RDF.type, OWL.Class))
        self.g.add((self.Crime, RDF.type, OWL.Class))
        self.g.add((self.Ethics_of_science_experimentation, RDF.type, OWL.Class))
        self.g.add((self.Morality_in_war, RDF.type, OWL.Class))
        self.g.add((self.Burdens_of_war, RDF.type, OWL.Class))
        self.g.add((self.Nuclear_war, RDF.type, OWL.Class))
        self.g.add((self.Moral_corruption, RDF.type, OWL.Class))
        self.g.add((self.Tragedy, RDF.type, OWL.Class))
        self.g.add((self.Survival, RDF.type, OWL.Class))
        self.g.add((self.Man_vs_Nature, RDF.type, OWL.Class))
        self.g.add((self.Nature_as_a_force, RDF.type, OWL.Class))
        self.g.add((self.Civilization_vs_The_wild, RDF.type, OWL.Class))
        self.g.add((self.Resourcefulness, RDF.type, OWL.Class))
        self.g.add((self.Civilization_vs_Barbarism, RDF.type, OWL.Class))
        self.g.add((self.Primal_instincts, RDF.type, OWL.Class))
        self.g.add((self.Savagery_vs_Civilization, RDF.type, OWL.Class))
        self.g.add((self.Mortality, RDF.type, OWL.Class))
        self.g.add((self.Fragility_of_life, RDF.type, OWL.Class))
        self.g.add((self.The_value_of_life, RDF.type, OWL.Class))
        self.g.add((self.Aging, RDF.type, OWL.Class))
        self.g.add((self.Death, RDF.type, OWL.Class))
        self.g.add((self.Grief, RDF.type, OWL.Class))
        self.g.add((self.Spirituality, RDF.type, OWL.Class))
        self.g.add((self.Immortality, RDF.type, OWL.Class))
        self.g.add((self.Healing, RDF.type, OWL.Class))
        self.g.add((self.Mass_Hysteria, RDF.type, OWL.Class))
        self.g.add((self.The_supernatural, RDF.type, OWL.Class))
        self.g.add((self.Superstition_vs_Reality, RDF.type, OWL.Class))
        self.g.add((self.Fear_of_the_unknown, RDF.type, OWL.Class))
        self.g.add((self.Faith_vs_Knowledge, RDF.type, OWL.Class))
        self.g.add((self.Gods_Will, RDF.type, OWL.Class))
        self.g.add((self.Divine_Intervention, RDF.type, OWL.Class))
        self.g.add((self.Abuse, RDF.type, OWL.Class))
        self.g.add((self.Silence, RDF.type, OWL.Class))
        self.g.add((self.Cycle_of_Violence, RDF.type, OWL.Class))
        self.g.add((self.Child_labor, RDF.type, OWL.Class))
        self.g.add((self.Justice, RDF.type, OWL.Class))
        self.g.add((self.The_struggle_for_justice, RDF.type, OWL.Class))
        self.g.add((self.Nationalism, RDF.type, OWL.Class))
        self.g.add((self.Patriotism, RDF.type, OWL.Class))
        self.g.add((self.Duality, RDF.type, OWL.Class))
        self.g.add((self.Logical_Paradox, RDF.type, OWL.Class))
        self.g.add((self.Fact_vs_Fiction, RDF.type, OWL.Class))
        self.g.add((self.Technological_advancements, RDF.type, OWL.Class))
        self.g.add((self.Scientific_curiosity, RDF.type, OWL.Class))
        self.g.add((self.Nature_theme, RDF.type, OWL.Class))
        self.g.add((self.The_role_of_nature, RDF.type, OWL.Class))
        self.g.add((self.Connection_to_nature, RDF.type, OWL.Class))
        self.g.add((self.Religious_Oppression, RDF.type, OWL.Class))
        self.g.add((self.Experience_of_Art, RDF.type, OWL.Class))
        self.g.add((self.Education, RDF.type, OWL.Class))
        self.g.add((self.Democracy, RDF.type, OWL.Class))
        self.g.add((self.Health, RDF.type, OWL.Class))
        self.g.add((self.Food_Safety, RDF.type, OWL.Class))
        self.g.add((self.Physical_activity_and_movement, RDF.type, OWL.Class))


        self.g.add((self.Coming_of_age, RDFS.subClassOf, self.Theme))
        self.g.add((self.Race, RDFS.subClassOf, self.Theme))
        self.g.add((self.Totalitarianism, RDFS.subClassOf, self.Theme))
        self.g.add((self.Pursuit_of_happiness, RDFS.subClassOf, self.Theme))
        self.g.add((self.Class_and_society, RDFS.subClassOf, self.Theme))
        self.g.add((self.Human_nature, RDFS.subClassOf, self.Theme))
        self.g.add((self.Tradition, RDFS.subClassOf, self.Theme))
        self.g.add((self.Morality, RDFS.subClassOf, self.Theme))
        self.g.add((self.Tragedy, RDFS.subClassOf, self.Theme))
        self.g.add((self.Mass_Hysteria, RDFS.subClassOf, self.Theme))
        self.g.add((self.Faith_vs_Knowledge, RDFS.subClassOf, self.Theme))
        self.g.add((self.Abuse, RDFS.subClassOf, self.Theme))
        self.g.add((self.Justice, RDFS.subClassOf, self.Theme))
        self.g.add((self.Nationalism, RDFS.subClassOf, self.Theme))
        self.g.add((self.Duality, RDFS.subClassOf, self.Theme))
        self.g.add((self.Technological_advancements, RDFS.subClassOf, self.Theme))
        self.g.add((self.Nature_theme, RDFS.subClassOf, self.Theme))
        self.g.add((self.Religious_Oppression, RDFS.subClassOf, self.Theme))
        self.g.add((self.Experience_of_Art, RDFS.subClassOf, self.Theme))
        self.g.add((self.Education, RDFS.subClassOf, self.Theme))
        self.g.add((self.Democracy, RDFS.subClassOf, self.Theme))
        self.g.add((self.Health, RDFS.subClassOf, self.Theme))

        # Coming of age Hierarchy
        self.g.add((self.Self_discovery, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Courage, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Identity, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Isolation, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Self_destruction, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Community, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.Self_consciousness, RDFS.subClassOf, self.Coming_of_age))
        self.g.add((self.The_importance_of_a_home_and_love, RDFS.subClassOf, self.Coming_of_age))

        # Sub-hierarchy of Self-discovery
        self.g.add((self.Personal_growth, RDFS.subClassOf, self.Self_discovery))
        self.g.add((self.Self_improvement, RDFS.subClassOf, self.Self_discovery))
        self.g.add((self.Purpose, RDFS.subClassOf, self.Self_discovery))
        self.g.add((self.Confronting_the_past, RDFS.subClassOf, self.Personal_growth))

        # Sub-hierarchy of Courage
        self.g.add((self.The_power_of_voice, RDFS.subClassOf, self.Courage))
        self.g.add((self.Heroism_vs_normalcy, RDFS.subClassOf, self.Courage))
        self.g.add((self.Advocacy, RDFS.subClassOf, self.The_power_of_voice))
        self.g.add((self.Power_of_words, RDFS.subClassOf, self.The_power_of_voice))
        self.g.add((self.Storytelling, RDFS.subClassOf, self.Power_of_words))
        self.g.add((self.Rhetoric, RDFS.subClassOf, self.Power_of_words))
        self.g.add((self.Rights_to_language, RDFS.subClassOf, self.Power_of_words))

        # Sub-hierarchy of Identity
        self.g.add((self.Cultural_identity, RDFS.subClassOf, self.Identity))
        self.g.add((self.Independence, RDFS.subClassOf, self.Identity))
        self.g.add((self.Dangers_of_naivety, RDFS.subClassOf, self.Identity))
        self.g.add((self.Self_expression, RDFS.subClassOf, self.Identity))
        self.g.add((self.Sexuality, RDFS.subClassOf, self.Identity))
        self.g.add((self.The_impact_of_love_on_identity, RDFS.subClassOf, self.Identity))
        self.g.add((self.Loss_of_innocence, RDFS.subClassOf, self.Identity))
        self.g.add((self.Self_worth, RDFS.subClassOf, self.Identity))
        self.g.add((self.Authenticity, RDFS.subClassOf, self.Identity))
        self.g.add((self.Food_in_culture, RDFS.subClassOf, self.Cultural_identity))
        self.g.add((self.Youth_vs_Age, RDFS.subClassOf, self.Dangers_of_naivety))
        self.g.add((self.Consequences_of_actions, RDFS.subClassOf, self.Loss_of_innocence))
        self.g.add((self.The_butterfly_effect, RDFS.subClassOf, self.Self_worth))
        self.g.add((self.Accountability, RDFS.subClassOf, self.Self_worth))

        # Sub-hierarchy of Isolation
        self.g.add((self.Alienation, RDFS.subClassOf, self.Isolation))
        self.g.add((self.Phoniness, RDFS.subClassOf, self.Isolation))
        self.g.add((self.Solitude, RDFS.subClassOf, self.Isolation))
        self.g.add((self.Anonymity, RDFS.subClassOf, self.Isolation))
        self.g.add((self.Self_reliance, RDFS.subClassOf, self.Solitude))

        # Sub-hierarchy of Community
        self.g.add((self.Social_Belonging, RDFS.subClassOf, self.Community))
        self.g.add((self.Found_Family, RDFS.subClassOf, self.Community))
        self.g.add((self.Role_models, RDFS.subClassOf, self.Community))
        self.g.add((self.The_myth_of_individual_success, RDFS.subClassOf, self.Community))
        self.g.add((self.Cultural_belonging, RDFS.subClassOf, self.Social_Belonging))
        self.g.add((self.Friendship, RDFS.subClassOf, self.Social_Belonging))
        self.g.add((self.Unconditional_love, RDFS.subClassOf, self.Found_Family))
        self.g.add((self.The_importance_of_human_connection, RDFS.subClassOf, self.Found_Family))

        # Sub-hierarchy of Self-consciousness
        self.g.add((self.Conformity, RDFS.subClassOf, self.Self_consciousness))
        self.g.add((self.Appearance, RDFS.subClassOf, self.Self_consciousness))

        # Race Hierarchy
        self.g.add((self.Prejudice, RDFS.subClassOf, self.Race))
        self.g.add((self.Racial_Inequality, RDFS.subClassOf, self.Race))
        self.g.add((self.Facing_racism, RDFS.subClassOf, self.Race))
        self.g.add((self.Inhumanity_towards_others, RDFS.subClassOf, self.Race))
        self.g.add((self.Equality, RDFS.subClassOf, self.Race))
        self.g.add((self.Immigration, RDFS.subClassOf, self.Race))
        self.g.add((self.Cultural_conflict, RDFS.subClassOf, self.Prejudice))
        self.g.add((self.Systemic_racism, RDFS.subClassOf, self.Racial_Inequality))
        self.g.add((self.Indigenous_oppression, RDFS.subClassOf, self.Racial_Inequality))
        self.g.add((self.Racial_injustice, RDFS.subClassOf, self.Racial_Inequality))
        self.g.add((self.Legacy_of_slavery, RDFS.subClassOf, self.Systemic_racism))
        self.g.add((self.Civil_disobedience, RDFS.subClassOf, self.Facing_racism))
        self.g.add((self.Indigenous_rights, RDFS.subClassOf, self.Facing_racism))
        self.g.add((self.Defiance, RDFS.subClassOf, self.Facing_racism))
        self.g.add((self.Rebellion, RDFS.subClassOf, self.Civil_disobedience))
        self.g.add((self.Order_vs_Disorder, RDFS.subClassOf, self.Civil_disobedience))
        self.g.add((self.Hatred, RDFS.subClassOf, self.Inhumanity_towards_others))
        self.g.add((self.Tolerance, RDFS.subClassOf, self.Equality))
        self.g.add((self.Diversity, RDFS.subClassOf, self.Equality))

        # Totalitarianism Hierarchy
        self.g.add((self.Leadership, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Censorship, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Freedom_vs_Control, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Deceit, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Public_ignorance, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Corruption, RDFS.subClassOf, self.Totalitarianism))
        self.g.add((self.Unchecked_ambition, RDFS.subClassOf, self.Leadership))
        self.g.add((self.Power_and_control, RDFS.subClassOf, self.Unchecked_ambition))
        self.g.add((self.Violence_for_power, RDFS.subClassOf, self.Power_and_control))
        self.g.add((self.Propaganda, RDFS.subClassOf, self.Censorship))
        self.g.add((self.Technological_control, RDFS.subClassOf, self.Censorship))
        self.g.add((self.The_impact_of_technology, RDFS.subClassOf, self.Technological_control))
        self.g.add((self.The_cost_of_happiness_and_individuality, RDFS.subClassOf, self.Freedom_vs_Control))
        self.g.add((self.Misinformation, RDFS.subClassOf, self.Deceit))

        # Pursuit of happiness Hierarchy
        self.g.add((self.Perseverance, RDFS.subClassOf, self.Pursuit_of_happiness))
        self.g.add((self.Individuality, RDFS.subClassOf, self.Pursuit_of_happiness))
        self.g.add((self.Expectations_vs_Reality, RDFS.subClassOf, self.Pursuit_of_happiness))
        self.g.add((self.Opportunity, RDFS.subClassOf, self.Pursuit_of_happiness))
        self.g.add((self.Resilience, RDFS.subClassOf, self.Perseverance))
        self.g.add((self.Acceptance_of_change, RDFS.subClassOf, self.Resilience))
        self.g.add((self.Unpredictability, RDFS.subClassOf, self.Expectations_vs_Reality))
        self.g.add((self.Dreams_vs_Reality, RDFS.subClassOf, self.Expectations_vs_Reality))

        # Class and society Hierarchy
        self.g.add((self.Social_class, RDFS.subClassOf, self.Class_and_society))
        self.g.add((self.Ambition, RDFS.subClassOf, self.Class_and_society))
        self.g.add((self.Toxic_capitalism, RDFS.subClassOf, self.Class_and_society))
        self.g.add((self.Class_corruption, RDFS.subClassOf, self.Social_class))
        self.g.add((self.Poverty, RDFS.subClassOf, self.Ambition))
        self.g.add((self.Social_Status, RDFS.subClassOf, self.Ambition))
        self.g.add((self.Wealth_gap, RDFS.subClassOf, self.Ambition))
        self.g.add((self.The_value_of_reputation, RDFS.subClassOf, self.Social_Status))
        self.g.add((self.Greed, RDFS.subClassOf, self.Wealth_gap))
        self.g.add((self.Greed_vs_Selflessness, RDFS.subClassOf, self.Toxic_capitalism))
        self.g.add((self.Wealth_vs_Value, RDFS.subClassOf, self.Toxic_capitalism))
        self.g.add((self.Corporations, RDFS.subClassOf, self.Toxic_capitalism))
        self.g.add((self.Consumerism, RDFS.subClassOf, self.Toxic_capitalism))

        # Human nature Hierarchy
        self.g.add((self.Revenge, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Betrayal, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.The_power_of_the_mind, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Disconnection_between_body_and_mind, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Fate_vs_Free_will, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Judgement, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Pride, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.The_passage_of_time, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Gratitude, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Madness, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Compassion, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Redemption, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Kindness, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Love, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Altruism_vs_self_interest, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Honor, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Loyalty, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Motherhood, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Human_insignificance, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Dishonesty, RDFS.subClassOf, self.Human_nature))
        self.g.add((self.Guilt, RDFS.subClassOf, self.Revenge))
        self.g.add((self.Revenge_love, RDFS.subClassOf, self.Revenge))
        self.g.add((self.Betrayal_vs_Loyalty, RDFS.subClassOf, self.Betrayal))
        self.g.add((self.Imagination, RDFS.subClassOf, self.The_power_of_the_mind))
        self.g.add((self.Creativity, RDFS.subClassOf, self.The_power_of_the_mind))
        self.g.add((self.Intelligence, RDFS.subClassOf, self.The_power_of_the_mind))
        self.g.add((self.Strategy, RDFS.subClassOf, self.The_power_of_the_mind))
        self.g.add((self.Memory, RDFS.subClassOf, self.The_power_of_the_mind))
        self.g.add((self.Innovation, RDFS.subClassOf, self.Creativity))
        self.g.add((self.Dangers_of_tempting_fate, RDFS.subClassOf, self.Fate_vs_Free_will))
        self.g.add((self.Destiny, RDFS.subClassOf, self.Fate_vs_Free_will))
        self.g.add((self.Fate_and_foreknowledge, RDFS.subClassOf, self.Fate_vs_Free_will))
        self.g.add((self.Limits_of_human_agency, RDFS.subClassOf, self.Destiny))
        self.g.add((self.Limits_of_knowledge, RDFS.subClassOf, self.Judgement))
        self.g.add((self.Stereotypes, RDFS.subClassOf, self.Limits_of_knowledge))
        self.g.add((self.Consequences_of_selfishness, RDFS.subClassOf, self.Pride))
        self.g.add((self.Vanity, RDFS.subClassOf, self.Pride))
        self.g.add((self.Humility, RDFS.subClassOf, self.Pride))
        self.g.add((self.Arrogance, RDFS.subClassOf, self.Pride))
        self.g.add((self.Jealousy, RDFS.subClassOf, self.Pride))
        self.g.add((self.Superficiality_of_beauty, RDFS.subClassOf, self.Vanity))
        self.g.add((self.Dignity, RDFS.subClassOf, self.Humility))
        self.g.add((self.Finding_beauty_in_the_everyday, RDFS.subClassOf, self.The_passage_of_time))
        self.g.add((self.Urgency_of_action, RDFS.subClassOf, self.The_passage_of_time))
        self.g.add((self.Lost_opportunities, RDFS.subClassOf, self.The_passage_of_time))
        self.g.add((self.Obsession, RDFS.subClassOf, self.Madness))
        self.g.add((self.Forgiveness, RDFS.subClassOf, self.Compassion))
        self.g.add((self.Empathy, RDFS.subClassOf, self.Compassion))
        self.g.add((self.Apology, RDFS.subClassOf, self.Forgiveness))
        self.g.add((self.Overcoming_adversity, RDFS.subClassOf, self.Redemption))
        self.g.add((self.Respect, RDFS.subClassOf, self.Kindness))
        self.g.add((self.Cruelty_vs_Kindness, RDFS.subClassOf, self.Kindness))
        self.g.add((self.Sacrifice, RDFS.subClassOf, self.Love))
        self.g.add((self.Selflessness, RDFS.subClassOf, self.Love))
        self.g.add((self.Love_vs_Self_interest, RDFS.subClassOf, self.Love))
        self.g.add((self.Love_vs_Hate, RDFS.subClassOf, self.Love))
        self.g.add((self.Relationships, RDFS.subClassOf, self.Love))
        self.g.add((self.Victory, RDFS.subClassOf, self.Honor))
        self.g.add((self.Universe_indifference, RDFS.subClassOf, self.Human_insignificance))
        self.g.add((self.Hypocrisy, RDFS.subClassOf, self.Dishonesty))

        # Tradition Hierarchy
        self.g.add((self.Sacrifice_for_family, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Gender, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Legacy_of_heritage, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Blind_tradition, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Tradition_vs_Change, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Familial_expectations, RDFS.subClassOf, self.Tradition))
        self.g.add((self.Gender_Roles, RDFS.subClassOf, self.Gender))
        self.g.add((self.Chivalry, RDFS.subClassOf, self.Gender))
        self.g.add((self.Patriarchal_control, RDFS.subClassOf, self.Gender))
        self.g.add((self.Marriage, RDFS.subClassOf, self.Gender_Roles))
        self.g.add((self.Domesticity, RDFS.subClassOf, self.Gender_Roles))
        self.g.add((self.Martial_expectations, RDFS.subClassOf, self.Marriage))
        self.g.add((self.Masculinity, RDFS.subClassOf, self.Patriarchal_control))
        self.g.add((self.Generational_divide, RDFS.subClassOf, self.Tradition_vs_Change))

        # Morality Hierarchy
        self.g.add((self.The_danger_of_temptation, RDFS.subClassOf, self.Morality))
        self.g.add((self.Personal_and_public_truth, RDFS.subClassOf, self.Morality))
        self.g.add((self.The_cruelty_of_bullying, RDFS.subClassOf, self.Morality))
        self.g.add((self.Moral_Responsibility, RDFS.subClassOf, self.Morality))
        self.g.add((self.The_nature_of_evil, RDFS.subClassOf, self.Morality))
        self.g.add((self.Ethics_of_science_experimentation, RDFS.subClassOf, self.Morality))
        self.g.add((self.Morality_in_war, RDFS.subClassOf, self.Morality))
        self.g.add((self.Moral_corruption, RDFS.subClassOf, self.Morality))
        self.g.add((self.Complexity_of_childhood_behavior, RDFS.subClassOf, self.The_cruelty_of_bullying))
        self.g.add((self.Human_impact_on_the_environment, RDFS.subClassOf, self.Moral_Responsibility))
        self.g.add((self.Dark_side_of_human_nature, RDFS.subClassOf, self.The_nature_of_evil))
        self.g.add((self.Good_vs_Evil, RDFS.subClassOf, self.The_nature_of_evil))
        self.g.add((self.Crime, RDFS.subClassOf, self.The_nature_of_evil))
        self.g.add((self.Burdens_of_war, RDFS.subClassOf, self.Morality_in_war))
        self.g.add((self.Nuclear_war, RDFS.subClassOf, self.Morality_in_war))

        # Tragedy Hierarchy
        self.g.add((self.Survival, RDFS.subClassOf, self.Tragedy))
        self.g.add((self.Mortality, RDFS.subClassOf, self.Tragedy))
        self.g.add((self.Healing, RDFS.subClassOf, self.Tragedy))
        self.g.add((self.Man_vs_Nature, RDFS.subClassOf, self.Survival))
        self.g.add((self.Primal_instincts, RDFS.subClassOf, self.Survival))
        self.g.add((self.Nature_as_a_force, RDFS.subClassOf, self.Man_vs_Nature))
        self.g.add((self.Civilization_vs_The_wild, RDFS.subClassOf, self.Man_vs_Nature))
        self.g.add((self.Resourcefulness, RDFS.subClassOf, self.Man_vs_Nature))
        self.g.add((self.Civilization_vs_Barbarism, RDFS.subClassOf, self.Civilization_vs_The_wild))
        self.g.add((self.Savagery_vs_Civilization, RDFS.subClassOf, self.Primal_instincts))
        self.g.add((self.Fragility_of_life, RDFS.subClassOf, self.Mortality))
        self.g.add((self.The_value_of_life, RDFS.subClassOf, self.Mortality))
        self.g.add((self.Aging, RDFS.subClassOf, self.Mortality))
        self.g.add((self.Spirituality, RDFS.subClassOf, self.Mortality))
        self.g.add((self.Immortality, RDFS.subClassOf, self.Mortality))
        self.g.add((self.Death, RDFS.subClassOf, self.Aging))

        # Mass Hysteria Hierarchy
        self.g.add((self.The_supernatural, RDFS.subClassOf, self.Mass_Hysteria))
        self.g.add((self.Grief, RDFS.subClassOf, self.The_supernatural))
        self.g.add((self.Superstition_vs_Reality, RDFS.subClassOf, self.Grief))
        self.g.add((self.Fear_of_the_unknown, RDFS.subClassOf, self.Grief))

        # Faith vs. Knowledge Hierarchy
        self.g.add((self.Gods_Will, RDFS.subClassOf, self.Faith_vs_Knowledge))
        self.g.add((self.Divine_Intervention, RDFS.subClassOf, self.Faith_vs_Knowledge))

        # Abuse Hierarchy
        self.g.add((self.Silence, RDFS.subClassOf, self.Abuse))
        self.g.add((self.Cycle_of_Violence, RDFS.subClassOf, self.Abuse))
        self.g.add((self.Child_labor, RDFS.subClassOf, self.Abuse))

        # Justice Hierarchy
        self.g.add((self.The_struggle_for_justice, RDFS.subClassOf, self.Justice))

        # Nationalism Hierarchy
        self.g.add((self.Patriotism, RDFS.subClassOf, self.Nationalism))

        # Duality Hierarchy
        self.g.add((self.Logical_Paradox, RDFS.subClassOf, self.Duality))
        self.g.add((self.Fact_vs_Fiction, RDFS.subClassOf, self.Duality))

        # Technological advancements Hierarchy
        self.g.add((self.Scientific_curiosity, RDFS.subClassOf, self.Technological_advancements))

        # Nature Hierarchy
        self.g.add((self.The_role_of_nature, RDFS.subClassOf, self.Nature_theme))
        self.g.add((self.Connection_to_nature, RDFS.subClassOf, self.Nature_theme))

        # Health Hierarchy
        self.g.add((self.Food_Safety, RDFS.subClassOf, self.Health))
        self.g.add((self.Physical_activity_and_movement, RDFS.subClassOf, self.Health))

    def get_theme_mapping(self, key):
        return self.theme_mapping.get(key)

    def get_graph(self):
        return self.g

    def save_ontology(self, output_path='data/owls/theme.owl'):
        self.g.serialize(output_path, format='xml')
        print(f'Theme ontology saved to {output_path}')


if __name__ == '__main__':
    theme_ontology = Theme()
    theme_ontology.create_theme_ontology()
    theme_ontology.save_ontology()