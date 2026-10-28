import numpy as np
import matplotlib.pyplot as plt

names = np.array(["Amina", "Brian", "Cathy", "David", "Esther"])
subjects = np.array(["Math", "English", "Science", "History"])

scores = np.array([
    [78, 85, 90, 72],
    [55, 62, 48, 70],
    [92, 88, 95, 85],
    [67, 74, 60, 58],
    [81, 79, 84, 90],
])

print(scores.shape)

averages = scores.mean(axis=1)

for name, avg in zip(names, averages):
    print(name, round(avg, 1))# (5, 4): 5 rows, 4 columns


highest = scores.max(axis=0)

for subject, top in zip(subjects, highest):
    print(subject, 'highest:', top)


for i, subject in enumerate(subjects):
    above = names[scores[:, i] > 70]
    print(subject, "above 70:", list(above))

best = np.argmax(averages)
print("Top student:", names[best], "with", round(averages[best], 1))


best = np.argmax(averages)
print("Top student:", names[best], "with", round(averages[best], 1))

plt.bar(names, averages)
plt.title("Student Averages")
plt.ylabel("Average score")
plt.show()