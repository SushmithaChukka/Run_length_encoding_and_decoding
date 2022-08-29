def getString(string):
    n = len(string)
    i = 0 
    while i < n-1:
        count = 1 
        while (i<n-1 and string[i]==string[i+1]):
            count+=1 
            i+=1 
        i+=1 
        print(string[i-1] + str(count),end = "")
string = "aaabbccccdeegfffjjjjkk"
getString(string)