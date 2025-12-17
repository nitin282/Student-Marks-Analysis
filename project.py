import numpy as np
student_marks=np.array([
    [90,98,97],
    [98,67,90],
    [93,92,91],
    [95,94,87],
    [78,84,99]])
print("total marks is:")
total_marks=np.sum(student_marks,axis=1)
print(total_marks)
print("average marks is:")
average_student=np.mean(student_marks,axis=1)
print(average_student)
print("Highest marks is:")
highest=np.max(student_marks,axis=0)
print(highest)
print("Lowest marks is:")
lowest=np.min(student_marks,axis=0)
print(lowest)
print("average marks is:")
average=np.mean(student_marks,axis=0)
print(average)
print("student highest marks")
highest_student_marks=np.max(total_marks)
print(highest_student_marks)
print("lowest marks is:")
lowest_student_marks=np.min(total_marks)
print(lowest_student_marks)
subjects=["Maths","Science","English"]
print("subject best performance:")
best_performance_subjest=subjects[np.argmax(highest)]
print(best_performance_subjest)
print("subject worst performance ")
worst_performance_subject=subjects[np.argmin(lowest)]
print(worst_performance_subject)