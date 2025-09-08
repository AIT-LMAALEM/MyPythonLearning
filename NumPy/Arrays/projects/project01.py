import numpy as np


grades = np.random.randint(0, 21, size=(20, 5))
print("Grades (20 students x 5 subjects):")
print(grades)
print("-" * 50)


student_avg = np.mean(grades, axis=1)
print("Average grade per student:")
print(student_avg)
print("-" * 50)

subject_avg = np.mean(grades, axis=0)
print("Average grade per subject:")
print(subject_avg)
print("-" * 50)


best_student_index = np.argmax(student_avg)  # index of best student
print("Best student index:", best_student_index)
print("Best student average:", student_avg[best_student_index])
print("Best student grades:", grades[best_student_index])
print("-" * 50)


worst_subject_index = np.argmin(subject_avg)  # index of worst subject
print("Worst subject index:", worst_subject_index)
print("Worst subject average:", subject_avg[worst_subject_index])
print("All grades for this subject:", grades[:, worst_subject_index])
print("-" * 50)


random_student_index = np.random.choice(grades.shape[0])  # choose one student index
print("Random student index:", random_student_index)
print("Random student grades:", grades[random_student_index])