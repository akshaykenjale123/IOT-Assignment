sub1 = int(input("Enter marks of science :"))
sub2 = int(input("Enter marks of maths :"))
sub3 = int(input("Enter marks of english :"))

sum = sub1+sub2+sub3
marks=sum/3

print("Total marks =",sum)
print("Percentage =",marks)

if marks>=90 and marks<=100:
    print("Grade = A")
elif marks>=80 and marks<=89:
    print("Grade = B")
elif marks>=70 and marks<=79:
    print("Grade = C")   
elif marks>=60 and marks<=69:
    print("Grade = D") 
else:
    print("Grade = F")                    