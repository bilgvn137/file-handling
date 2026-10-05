# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    file=open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c+=1
    file.close()
    pass

# Exercise 2
def read_names(filename):
    file=open(filename,"r")
    lst=file.readlines()
    list=[]
    for line in lst:
        if line.strip()!="":
            list.append(line.strip())
    file.close()
    return list
    pass

# Exercise 3
def append_entry(filename, text):
    file=open(filename,"a")
    file.write(f"{text}\n")
    file.close()
    file=open(filename,"r")
    lst=file.readlines()
    file.close()
    return len(lst)
    pass

# Exercise 4
def search_file(filename, word):
    file=open(filename,"r")
    list=[]
    index=1
    for line in file:
        if word.lower() in line.lower():
            list.append(index)
        index+=1
    file.close()
    return list
    pass

# Exercise 5
def number_the_lines(source, destination):
    file=open(source,"r")
    lst=file.readlines()
    file.close()
    file=open(destination,"w")
    c=1
    for i  in lst:
        file.write(f"{c}: {i}")
        c+=1
    file.close()
    return len(lst)
    pass
