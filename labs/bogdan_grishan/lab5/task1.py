import function

print("Select function:\n 1)enter_list \n 2)random_list \n 3)search \n 4)max_element \n 5)sort \n 6)average")
i = 1
while i != "exit":
    i = input("Enter name function:")
    if i == 'enter_list':
        function.enter_list()
    if i == 'random_list':
        function.random_list()
    if i == 'search':
        function.search()
    if i == 'max_element':
        function.max_element()
    if i == 'sort':
        function.sort()
    if i == 'average':
        function.average()



