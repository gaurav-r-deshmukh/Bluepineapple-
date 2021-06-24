def reverse(string):
    return string[::-1]
    
while(1):
    
    string=input("\nEnter 'exit' to exit outof program \nEnter String to reverse: ")
    print("\nReverse of '{}' is  '{}' ".format(string,reverse(string)))
    