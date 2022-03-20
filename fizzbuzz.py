for i in range(101):
     
    while i<101:
        
       if i % 3 ==0:
           mylist.append("fizz")
        
       elif i % 5 ==0:
           mylist.append("buzz")
       
       elif i % 3 and i % 5 ==0:
           mylist.append("fizzbuzz")  

       else:
          mylist.append(i)       
       i+=1
  
print(mylist)
