set1 = set()

set1.add(1)
set1.add(2)
set1.add(2)
set1.add("naila")
set1.add(("a", "B", "c"))
set1.remove(2) #it will remove 2 from set
#set1.pop() #{2, ('a', 'B', 'c'), 'naila'}

print(set1) #{1, 2, 'naila', ('a', 'B', 'c')}
