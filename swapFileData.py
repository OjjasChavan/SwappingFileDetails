def swapFileData():
  
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            data1 = f1.read()
            data2 = f2.read()

    with open(file1, 'w') as f1:
        f1.write(data2)

    with open(file2, 'w') as f2:
        f2.write(data1)

    print("Files swapped successfully")
    
swapFileData()