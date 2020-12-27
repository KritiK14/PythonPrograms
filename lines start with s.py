def countS():
    f=open("pytest.txt",'r+')
    lines=0
    l=readlines()
    for i in l:
        if i[0]=='S':
            lines+=1
    print("No of lines are",lines)
