def main() :
   try:
      booklist = []
      infile = open("theBooklist.txt","r")
      line = infile.readline()
      while line :
         booklist.append(line.rstrip("\n").split(","))
         line = infile.readline()
      infile.close()


   except FileNotFoundError:
      print("the <booklist.txt> file not found")
      print("Start a new booklist")
      booklist = []


   choice = 0
   while choice != 4:
      print("***Book Manager***")
      print("1) Add a book")
      print("2) lookup a book")
      print("3) Display books")
      print("4) Quit")
      choice = int(input("Enter a choice: "))
      

      if choice == 1:
         print("Adding a book...")
         nBook = input("Enter the name of book : ")
         nAuthor = input("Enter the name of author : ")
         nPages = input("Enter the number of pages : ")
         booklist.append([nBook, nAuthor, nPages])

      elif choice == 2:
         print("Looking up for book...")
         keyword = input("Enter Search Term: ")
         for book in booklist:
            if keyword in book:
               print(book)

      elif choice == 3:
         print("Display all books...")
         for i in range(len(booklist)):
            print(booklist[i])         
      
      elif choice == 4:
         print("Quitting Program... ")

   print("Program Terminated!")  

   # Saving to external TXT file
   outfile = open("theBooklist.txt","w")
   for book in booklist:
      outfile.write(",".join(book) + "\n")
   outfile.close()   



if __name__ == "__main__":
  main()  
