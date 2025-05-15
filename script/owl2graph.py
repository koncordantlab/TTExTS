from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, BNode, Literal
import networkx as nx
import pickle

class OWL2Graph:
    def __init__(self, owl_file):
        """Load OWL ontology and convert restrictions into explicit triples"""
        self.graph = Graph()
        self.graph.parse(owl_file, format='xml')
        self.nx_graph = nx.Graph()
        self.nx_graph_noconv = nx.Graph()
        self.existing_triples = set()

    def extract_direct_triples(self):
        """Extract direct rdf:Property triples, excluding subclass with blank nodes"""
        for subj, pred, obj in self.graph:
            if pred == RDFS.subClassOf and isinstance(obj, BNode):
                continue

            if isinstance(obj, Literal) or isinstance(subj, Literal):
                continue

            if isinstance(subj, BNode) or isinstance(obj, BNode):
                continue

            self.nx_graph.add_edge(str(subj), str(obj), relation=str(pred))
            self.existing_triples.add((str(subj), str(pred), str(obj)))

    def convert_restrictions(self):
        """Convert owl:Restrictions to explicit triples, avoiding duplicates"""
        OWL_NS = Namespace("http://www.w3.org/2002/07/owl#")

        for subj, _, restriction in self.graph.triples((None, RDFS.subClassOf, None)):
            if (restriction, RDF.type, OWL_NS.Restriction) in self.graph:
                on_property = None
                some_values_from = None

                for _, _, prop in self.graph.triples((restriction, OWL_NS.onProperty, None)):
                    on_property = prop

                for _, _, obj in self.graph.triples((restriction, OWL_NS.someValuesFrom, None)):
                    some_values_from = obj

                if on_property and some_values_from:
                    new_triple = (subj, on_property, some_values_from)
                    if new_triple not in self.existing_triples:
                        self.nx_graph.add_edge(str(subj), str(some_values_from), relation=str(on_property))

    def save_as_gpickle(self, output_file):
        """Save the NetworkX graph as a gpickle file"""
        with open(output_file, "wb") as f:
            pickle.dump(self.nx_graph, f)
            print(f"Graph saved as {output_file}")

    def run_conversion(self):
        """Extract direct triples first, then convert restrictions"""

        self.extract_direct_triples()
        
        self.convert_restrictions()
        
        self.save_as_gpickle("./data/graph.gpickle")


owl_file_path = "./data/output.owl"
converter = OWL2Graph(owl_file_path)
converter.run_conversion()
