#!/usr/bin/env python

#import the CSV module for dealing with CSV files
import csv

#create a 'reader' variable, which allows us to play with the contents of the CSV file
#in order to do that, we create the ifile variable, open the CSV file into that, then pass its' contents into the reader variable.
ifile = open('data.csv', 'rb')
reader = csv.reader(ifile)

#create a new variable called 'outfile' (could be any name), which we'll use to create a new file that we'll pass our TTL into.
outfile = open('data.ttl', 'a')

uri = '###  https://raw.githubusercontent.com/damorton/bakery-ontology/master/bamboozledbakery.owl#'

allIngredientsSet = set([])

#get python to loop through each row in the CSV, and ignore the first row.
rownum = 0
for row in reader:
	if rownum == 0: # if it's the first row, then ignore it, move on to the next one.
		pass
	else: # if it's not the first row, place the contents of the row into the 'c' variable, then create a 'd' variable with the stuff we want in the file.
		
		c = row

		# dessert block
		dessert = c[0].replace(' ','_')
		dessert = dessert.replace("'", '')
		dessert = dessert.lower()
		dessertBlock = ''
		dessertBlock = uri + dessert + '\n'
		dessertBlock += 'bakery:' + dessert + ' rdf:type owl:NamedIndividual ,\n bakery:Dessert ;\nbakery:contains '
		
		# add ingredients
		ingredientsStr = ''
		count = 0
		dessertIngredientList = c[1].split(',')
		for ingredient in dessertIngredientList:
			ingredient = ingredient.replace(' ','')
			ingredient = ingredient.replace("'",'')

			# add ingredient to set
			allIngredientsSet.add(ingredient)

			ingredientsStr += 'bakery:' + ingredient
			count += 1
			if len(dessertIngredientList) != count:
				ingredientsStr += ' ,\n'
			else:
				ingredientsStr += ' .\n'			

		dessertBlock += ingredientsStr + '\n'

		result = dessertBlock

		outfile.write(result)	# now write the d variable into the file

	rownum += 1 # advance the row number so we can loop through again with the next row

# output all ingredients to file
for ingredient in allIngredientsSet:
	ingredientBlock = uri + ingredient + '\n' + 'bakery:' + ingredient + ' rdf:type owl:NamedIndividual ,\nbakery:Ingredient .\n\n'
	outfile.write(ingredientBlock)
		

# finish off by closing the two files we created

outfile.close()
ifile.close()
