from time import sleep

print("This is my presentation for the Algorithms pro intensive course.")
print(" ")
print(" ")
sleep(3)
print("I will go through the questions one by one and answer them.")
print(" ")
print(" ")
sleep(3)
print("""While building the maze we attempted moving 2 cells at a time.
What would the maze look like when moving a larger number of cells?""")
print(" ")
print(" ")
sleep(3)
print("""There would be far fewer walls as everytime the mow function ran it
would mow down more walls than before. There would also be far more swag dropped
across the maze because since there are now more open steps in our maze due to
the mow function mowing down more walls the swag dice rolls far more times than
before resulting in more swag.""")
print(" ")
print(" ")
sleep(3)
print("What would the maze look like if this number was not constant?")
print(" ")
print(" ")
sleep(3)
print("""It would depend how high or how low the possible number could be.
If the range of the possible number went high enough you would have a similar
result as before with fewer walls and more swag. If the range was extremely low
like between 1 and 2 the result would be more walls and fewer swag than before.""")
print(" ")
print(" ")
sleep(3)
print("What algorithms could you use to find a path through this maze? Compare and contrast at least 2.")
print(" ")
print(" ")
sleep(3)
print("2 algorithms that come to mind are Dijkstra's algorithm and the A* algorithm.")
print(" ")
sleep(1)
print("I also imagine its possible to use a linear search but it would be messy and inneficient.")
sleep(1)
print(" ")
print("""How does knowing the algorithm used to generate the maze influence
the best algorithm to solve it with?""")
sleep(3)
print(" ")
print(" ")
print("""It is inevitable that the algorithm used to find a pathway would be similar
to the one used to create the maze because the mechanism by which each of these things
is accomplished is nearly identical.""")
sleep(3)
print(" ")
print(" ")
print("""As a patron picking up swag along the way, how might you best store
the list of items you've collected?""")
print(" ")
print(" ")
sleep(3)
print("""One could store these items in a hash map that maps each item to their
location in the maze. One could also use a linked list which would store the
items in chronological order.""")
sleep(3)
print(" ")
print(" ")
print("""If the farmer asked you to sort the items you collected before leaving
the maze, what sorting algorithms would you consider using?""")
print(" ")
print(" ")
sleep(3)
print("""A quicksort seems like the best option because of how efficient it is
assuming the criteria by which the swag is sorted is ascending alphabetical order.
However, if there was a very larger variety of swag a radix sort would perhaps
handle it a bit better.""")
sleep(3)
print(" ")
print(" ")
print("""How does the quantity and variety of swag influence your answer?""")
print(" ")
print(" ")
sleep(3)
print("""The more variety in the swag list the more comparisons have to be made
with the sorting algorithm which means a longer runtime. I don't believe a swag
list of high quantity but little variety would be an issue for the quicksort but
when you add in more variety the bucketing process of the radix sort seems to make
more sense intuitively.""")
sleep(5)
print(" ")
print(" ")
print("This concludes my presentation..... goodbye.")
exit(0)

      

































      
