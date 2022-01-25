students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
vse, nevse = set.intersection(*students), set.union(*students)
print(len(vse), *sorted(vse), sep='\n')
print(len(nevse), *sorted(nevse), sep='\n')
