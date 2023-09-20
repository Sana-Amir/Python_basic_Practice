student_name="Sana"
role_number=7774
maths_score = 89
eng_score = 99
urdu_score = 77

total_score = maths_score + eng_score + urdu_score
avg_score =  total_score / 3

if avg_score >= 50:
    result= "Pass"
else:
    result = "Fail"

if avg_score >= 90:
 grade = " A "
elif avg_score >= 80:
 grade = " B "
elif avg_score >= 70:
 grade = " C "
elif avg_score >= 60:
 grade = " D "
elif avg_score >= 50:
 grade = " E "
else:
 grade = " F "

txt= "Student name is {}."
print(txt.format(student_name))

txt = "Student role number is {}."
print(txt.format(role_number))

txt= "Maths score is {}."
print(txt.format(maths_score))

txt= "Eng score is {}."
print(txt.format(eng_score))

txt= "Urdu score is {}."
print(txt.format(urdu_score))

txt= "Total score is {}."
print(txt.format(total_score))

txt= "Average score is {}."
print(txt.format(avg_score))

x = "The student has {}"
print(x.format(result))

y = "The Grade is {}"
print(y.format(grade))