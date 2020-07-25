# wstud-thesis-tiwari

Master thesis of Prem Kumar Tiwari

Summary of Papers and their related use to my thesis 

### Automatic construction of lexicons, taxonomies, ontologies and other knowledge structures Olena Medelyan, Ian H. Witten, Anna Divoli and Jeen Broekstra

1. Knowledge structures differ in depth and coverage ranging from 

*  purpose built resources for document collection through domain specific representation of varying depth 
*  To extended efforts to capture comprehensive world knowledge in fine detail
Techniques for automatically constructing lexions, ontologies and taxonomies allow custom knowledge structures to be built for particular purpose [257].

2. Table 1 content : Types of Knowledge Structures

| Types  | Examples of Structures | Intended Applications | Encoding |
| ------ | ---------------------- | --------------------- | -------- |
| Term Lists | Lexicons, Dictionaries, Glossaries | Index of specialized Terms | XML |
| Term Hierarchies | Taxonomies, Thesauri | Indexing Content, exploratory Search | RDF, SKOS |
| Semantic databases | Dbpedia, Cyc, Babelnet | NLP, AI | OWL, OBO |

3. WordNet Vs Dbpedia and Freebase
WordNet, as its creator calls is a semi-ontology describes:
Nouns, adjectives, verbs and adverbs and their synset [synonym set]
Recent versions have started to differentiate between Concepts and instances
Dbpedia, homebase have majority of instances of concepts defined using specific temporal and geographical relations and other worldly facts

4. The web contains a plethora of domain-specific resources : Geonames[geographical names of cities in hierarchical ], Uniprot [names of proteins, relates them to scientific processes and molecular functions]. Hence, depth and coverage from different sources are different and it would be hard to name them all or integrate into one.

5. Ontology learning layer cake by Buitelaar from simple to complex.
6. Riloff E.   and Shepherd argue that it is necessary to focus on particular domain because it is hard to capture all specific terminology and jargon in a single general knowledge base.

**Process**


1.  From text to term.
        
    *  Identify few seed terms and iteratively add terms that based on co-occurrence. [ corpus based approach ]
    *  Keyword extraction [ Rake NLP ]
2.  From terms to meaning
3.  From terms to Hierarchies
    *  Lexico-syntactic pattern
    *  Co-occurrence analysis [ word embedding]
    *  Distributional Similarity computation
    *  Dependency parsing
4.  Relations and facts extraction : The ultimate goal is to build a fully comprehensible database of knowledge, preferably that can be improved iteratively. This is an automatic analog of the long-standing CYC project, which has manually assembled a comprehensive ontology and knowledge base of everyday common sense knowledge that also evolves over time. [ our interest ]



















### Entity Search : Building Bridges between two worlds

Information retrieval (IR) and Semantic Web(SW)

The entity search tasks comes in several flavors:
1.  Entity ranking [ER] (given a query and target category, return a ranked list of relevant entities)
2.  List completion [LC] (given a query and example entities, return similar entities),[most similar]
3.  Related entity ﬁnding  [REF] aims at making arbitrary relation between entities searchable.

By now, the LOD cloud contains millions of concepts from over one hundred structured data sets. Linking “free text queries” to objects in LOD cloud (SW approach).




























### Automatic Construction of Multifaceted Browsing interfaces [most promising paper]

1.  Automatic and scalable methods for creation of multifaceted interfaces
2.  Methods are integrated with relational databases and can scale well for large database
3.  Methods for selection of best portions of generated hierarchies.

The paper describes more about navigational facet generation.

*Are we interested in a similar generation or do we want to come up with everything.*

The above task[coming up with everything] in my opinion would be futile, because let’s say a actor that performs in a sitcom happening every wednesday, would be classified under wednesday, which is an awkward hierarchy, hence navigational hierarchical generation seems more appropriate.

1.  Facets categories are defined by already existing collections of metadata organized across different facets.
2.  Works by assigning keywords to appropriate facets using a ML algorithm. Each keyword has a different set of hypernyms, which is substituted for expansion [ after sense disambiguation realized by co-occurrence]
