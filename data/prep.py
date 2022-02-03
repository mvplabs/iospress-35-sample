import csv

papers = {}
collabs = []
collabs.append(["Journal", "Category", "Country 1", "Country 2", "Paper"])

with open('data/collaborationraw.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)

       # displaying the contents of the CSV file
       count = 0
       for line in csvFile:
            paper = line['paper']

            if paper in papers:
                papers[paper].append(line)
            else:
                papers[paper] = [line]

print("Papers found")    
print(len(papers))

for paper in papers:
    prevc1 = None
    prevc2 = None
    authors = papers[paper]
    author_number = len(authors)
    journal = authors[0]['journalName']
    category = authors[0]['category']
    for a1n in range(author_number):
        for a2n in range(a1n + 1,author_number):
            c1 = authors[a1n]['country']
            c2 = authors[a2n]['country']

            if(c1 != c2 and (prevc1 != c1 or prevc2 != c2)):
                #print("New collaboration between " + c1 + " and " + c2 + " in " + journal)
                if(c1 < c2): 
                    collabs.append([journal, category, c1, c2, paper])
                else:
                    collabs.append([journal, category, c2, c1, paper])
            
            prevc1 = c1
            prevc2 = c2

print("Collabs found")
print(len(collabs))
filename = "collabs.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(collabs)     

# Target:
# Category Journal Paper Country1 Country2 Number

# Get a list per Cat/Journal/Paper
# For each paper iterate on authors
  # For each author iterate on other authors
    # If ~= country add a collab