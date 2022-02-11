question_list=[
    "How many continents are there?",
    "What is the capital of india?",
    "NG mai kaunsa course hota hai?"
]
Options_lists=[
    ["Four","Nine","Sever","Eight"],
    ["Chandigarh","Bhopal","Chennai","Delhi"],
    ["Software Engineering","Counselling","Tourism","Agriculture"]
]

Solution_list=[3,4,1]
life_line=[[1,3],[2,4],[1,2]]
Money=[1000, 5000, 10000]
i=0
sum=0
count=0
while i<len(question_list):
    print (i+1,question_list[i])
    j=0
    while j<=len(Options_lists):
        print(j+1,Options_lists[i],[j])
        j+=1
    if count<1:
        print("do you want to use life_line :")
        s = (input("Enter yes or no :"))
        if s == "yes":
            count+=1
            print(life_line[i])
    else:
        print("you have already used life_line")
    n=int(input("Enter the Number :"))
    if n==Solution_list[i]:
        sum=sum+money[i]
        print("ur ans is corrrct, you won rupees,sum,/-")
    else:
        print("ur ans is wrong")
        break
    i+=1