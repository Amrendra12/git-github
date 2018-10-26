def search():
    let = input("Which letter you want to delete in a,b,c,d: ")
    letters=["a","b","c","d"]
    del letters[letters.index(let)]
    return letters
a=search()
print(a)
