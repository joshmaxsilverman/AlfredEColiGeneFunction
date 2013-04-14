import commands, os

# grep the given query across all genes and return a string of results
stringOfResults = commands.getoutput('grep -F {query} gene.txt | cut -f 3,9')
# split the return on endlines; resolve string to individual results
results = stringOfResults.split('\n')
# split each result into the gene name and its description
pairs = [result.split('\t') for result in results]

# push the pairs to a list of dictionaries describing each gene returned
pairsDict = [{'gene': pair[0], 'description': pair[1]} for pair in pairs]

# XML template for Alfred's feedback display. Gene name as title, function as subtitle
text = """
<item arg="%(gene)s" uid="%(gene)s">
	<title>%(gene)s</title>
	<subtitle>%(description)s</subtitle>
	<icon type="jpg">geneIcon.jpg</icon>
</item>
"""

#returns itemized list of XML objects to Alfred
print ("<items>%s</items>" % "".join(text % thing for thing in pairsDict))