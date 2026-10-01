import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# STUDENT DATA
# =========================

data = {
    "Student": ["Ali", "Sara", "Ahmed", "Ayesha", "Hamza",
                "Zara", "Usman", "Hina", "Daniyal", "Maha"],

    "Study_Hours": [2, 5, 3, 7, 4, 8, 6, 3, 9, 5],

    "Assignments": [4, 8, 5, 9, 6, 10, 8, 5, 10, 7],

    "Attendance": [65, 88, 72, 95, 80, 98, 90, 70, 97, 85],

    "Marks": [45, 72, 55, 88, 65, 94, 82, 58, 96, 75]
}

df = pd.DataFrame(data)

print("\n========== STUDENT DATA ==========\n")
print(df)


# =========================
# BASIC ANALYSIS
# =========================

print("\n========== AVERAGE ==========\n")

print("Average Study Hours:",
      np.mean(df["Study_Hours"]))

print("Average Attendance:",
      np.mean(df["Attendance"]))

print("Average Marks:",
      np.mean(df["Marks"]))


# =========================
# TOP STUDENT
# =========================

top_student = df.loc[df["Marks"].idxmax()]

print("\n========== TOP STUDENT ==========\n")

print("Name:", top_student["Student"])
print("Marks:", top_student["Marks"])


# =========================
# STUDENT PERFORMANCE
# =========================

plt.figure(figsize=(10, 5))

plt.bar(
    df["Student"],
    df["Marks"]
)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks (%)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# =========================
# STUDY HOURS VS MARKS
# =========================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Marks"],
    s=100
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks (%)")

plt.grid(True)

plt.show()


# =========================
# ATTENDANCE VS MARKS
# =========================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Marks"],
    s=100
)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks (%)")

plt.grid(True)

plt.show()


# =========================
# STUDY HOURS VISUALIZATION
# =========================

plt.figure(figsize=(9, 5))

plt.plot(
    df["Student"],
    df["Study_Hours"],
    marker="o"
)

plt.title("Student Study Hours")
plt.xlabel("Students")
plt.ylabel("Study Hours")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()
plt.show()


# =========================
# FINAL REPORT
# =========================

print("\n===================================")
print("       STUDENT ANALYSIS REPORT")
print("===================================")

print("Total Students:", len(df))

print("Average Marks:",
      round(np.mean(df["Marks"]), 2))

print("Highest Marks:",
      np.max(df["Marks"]))

print("Lowest Marks:",
      np.min(df["Marks"]))

print("Average Study Hours:",
      round(np.mean(df["Study_Hours"]), 2))

print("Average Attendance:",
      round(np.mean(df["Attendance"]), 2))

print("\nTop Student:",
      top_student["Student"])

print("===================================")