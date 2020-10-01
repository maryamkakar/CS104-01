Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> numberOfTests = 2
>>> score1 = 85
>>> score2 = 67
>>> total = 152
>>> average = 76
>>> scoreCount = 2
>>> numberOfTests = int(input("Please enter the number of tests you want to average: "))
Please enter the number of tests you want to average: 2
>>> score1 = int(input("Please enter a score: "))
Please enter a score: 85
>>> score2 = int(input("Please enter a score: "))
Please enter a score: 67
>>> total = total + score1 + score2
>>> average = (total/scoreCount)
>>> print("The average is ",average)
The average is  152.0
>>> inputs = ["numberOfTests", "score1", "score2", "total", "average", "scoreCount"]
>>> for x in inputs:
	print(x)

	
numberOfTests
score1
score2
total
average
scoreCount


>>> average = 152.0
>>> while average > 0:
	average -= 5
	if average < 60:
		break
	print(average)
	print("END OF LOOP")

	
147.0
END OF LOOP
142.0
END OF LOOP
137.0
END OF LOOP
132.0
END OF LOOP
127.0
END OF LOOP
122.0
END OF LOOP
117.0
END OF LOOP
112.0
END OF LOOP
107.0
END OF LOOP
102.0
END OF LOOP
97.0
END OF LOOP
92.0
END OF LOOP
87.0
END OF LOOP
82.0
END OF LOOP
77.0
END OF LOOP
72.0
END OF LOOP
67.0
END OF LOOP
62.0
END OF LOOP
>>> 
