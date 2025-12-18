n=int(input("Enter number of books:"))
books=[]
for i in range (n):
    books.append(input("Enter book name: "))
for i in books:
    print(i,end="\n")
