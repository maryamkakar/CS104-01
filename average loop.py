Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> numberOfTests = 2
>>> score1 = 97
>>> score2 = 86
>>> total = 0
>>> average = 0.0
>>> scoreCount = 0
>>> numberOfTests = int(input("Please enter the number of tests you want to average: "))
Please enter the number of tests you want to average: 2
>>> score1 = int(input("Please enter a score: "))
Please enter a score: 97
>>> score2 = int(input("Please enter a score: "))
Please enter a score: 86
>>> scoreCount = scoreCount + 1
>>> total = total + score
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    total = total + score
NameError: name 'score' is not defined
>>> total = total + score1 + score2
>>> average = (total/scoreCount)
>>> print("The average is ",average)
The average is  183.0
>>> for i in numberOfTests;
SyntaxError: invalid syntax
>>> average = 183
>>> while average > 0
SyntaxError: invalid syntax
>>> while average > 0:
	average -=1
	print(average)

	
182
181
180
179
178
177
176
175
174
173
172
171
170
169
168
167
166
165
164
163
162
161
160
159
158
157
156
155
154
153
152
151
150
149
148
147
146
145
144
143
142
141
140
139
138
137
136
135
134
133
132
131
130
129
128
127
126
125
124
123
122
121
120
119
118
117
116
115
114
113
112
111
110
109
108
107
106
105
104
103
102
101
100
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
69
68
67
66
65
64
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
>>> for average
SyntaxError: invalid syntax
>>> average = 183
>>> for x in average:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for x in average:
TypeError: 'int' object is not iterable
>>> inputs = ["numberOfTests", "score1", "score2", "total", "average", "scoreCount"]
>>> for x in inputs:
	print(x)

	
numberOfTests
score1
score2
total
average
scoreCount
>>> 