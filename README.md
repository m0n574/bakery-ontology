# David's Bamboozled Bakery

- Link to this Ontology https://raw.githubusercontent.com/damorton/bakery-ontology/master/bamboozledbakery.owl
- List of desserts https://github.com/damorton/bakery-ontology/blob/master/scripts/data.csv
- Scripts used to convert `.csv` data to `.ttl` in https://github.com/damorton/bakery-ontology/tree/master/scripts
- `utils.py` does not include label/comment/etc information when creating `.ttl` data.

# Resources

- Download and install Protege https://protege.stanford.edu/products.php#desktop-protege
- Download and install Apache Jena Fuseki https://jena.apache.org/download/index.cgi
- Watch these youtube videos for an Intro to Protege and Apache Jena Fuseki https://youtu.be/0zUos1zWB5k

# Release Log

## Version 1.0 8th April 2018

- Contains 154 desserts
- Constina 129 ingredients.
- Includes ingredient groupings for:
  - VeganIngredient
  - Allergen
- Includes dessert groupings for:
  - ComplexDessert
  - DiabeticFriendly
  - EggAllergyFriendly
  - FruityDessert
  - GlutenFriendly
  - LactoseFriendly
  - NonDiabetic
  - NonEggAllergy
  - NonGluten
  - NonLactose
  - NonNutAllergy
  - NonTeetotaller
  - NonVegan
  - NonVegetarian
  - NutAllergyFriendly
  - SpicyDessert
  - TeetotallerFriendly
  - VeganFriendly
  - VegetarianFriendly
- Groupings include attributes for label, prefLabel, altLabel, definitions, and comments.
- Ontology includes prefixes for:
  - : https://raw.githubusercontent.com/damorton/bakery-ontology/master/bamboozledbakery.owl#
  - bakery: https://raw.githubusercontent.com/damorton/bakery-ontology/master/bamboozledbakery.owl#
  - dc: http://purl.org/dc/elements/1.1/
  - owl: http://www.w3.org/2002/07/owl#
  - rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  - rdfs: http://www.w3.org/2000/01/rdf-schema#
  - skos: http://www.w3.org/2004/02/skos/core#
  - terms: http://purl.org/dc/terms/
  - xml: http://www.w3.org/XML/1998/namespace
  - xsd: http://www.w3.org/2001/XMLSchema#
