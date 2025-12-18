n=int(input("Enter number of books:"))
books=[]
author=[]
for i in range (n):
    books.append(input("Enter Book Name: "))
    author.append(input("Enter Author Name"))
print("BOOK",'  ','Author')
for i in range(n):
    print(books[i],"    ",author[i],end="\n")
