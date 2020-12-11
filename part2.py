import time

STARTTIME = time.time()

file = open('input.txt', 'r')
fileContents = [rule.strip() for rule in file.readlines()]

Bags = {}

for line in fileContents:
    # array of words
    halves = line.strip().split("contain")
    bagName = halves[0].replace(' ', '')[:-4]
    bagContents = halves[1].strip().split(', ')
    cDict = {}
    for content in bagContents:
        content = content.strip().replace('.', '')
        if content != "no other bags":
            contentArray = content.strip().split(' ')
            contentQuantity = contentArray[0]
            contentName = contentArray[1] + contentArray[2]
            cDict[contentName] = contentQuantity
    Bags[bagName] = cDict



childrenArray = []
def getChildren(bag):
    global childrenArray
    children = Bags[bag]
    for child in children:
        n = child
        q = int(children[child])
        for x in range(q):
            childrenArray.append(item for item in getChildren(n))
    return childrenArray

print(len(getChildren("shinygold")))
"""
shiny gold bags contain 2 dark red bags.
dark red bags contain 3 dark orange bags, 4 dark blue bags.
dark orange bags contain no other bags.
dark blue bags contain no other bags.


shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

"""