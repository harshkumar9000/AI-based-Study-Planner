import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import os

# Try importing ML library safely
try:
    from sklearn.linear_model import LinearRegression
    ml_available = True
except:
    ml_available = False


# ---------------- FILE CHECK ----------------
if not os.path.exists("study.txt"):
    open("study.txt", "w").close()


# ---------------- ADD ----------------
def add():
    subject = input("Enter subject: ")

    try:
        hours = float(input("Enter hours: "))
    except:
        print("Invalid input\n")
        return

    with open("study.txt", "a") as f:
        f.write(subject + "," + str(hours) + "\n")

    print("Data added\n")


# ---------------- VIEW ----------------
def view():
    try:
        with open("study.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("No data found\n")
            return

        total = 0
        print("\n📘 Study Data:")

        for line in data:
            if "," not in line:
                continue

            s, h = line.strip().split(",")

            try:
                h = float(h)
            except:
                continue

            print(s, "-", h)
            total += h

        print("Total =", total, "hours\n")

    except Exception as e:
        print("Error:", e, "\n")


# ---------------- GRAPH ----------------
def graph():
    try:
        with open("study.txt", "r") as f:
            data = f.readlines()

        subjects = []
        hours = []

        for line in data:
            if "," not in line:
                continue

            s, h = line.strip().split(",")

            try:
                h = float(h)
            except:
                continue

            subjects.append(s)
            hours.append(h)

        if not subjects:
            print("No valid data for graph\n")
            return

        plt.bar(subjects, hours)
        plt.xlabel("Subjects")
        plt.ylabel("Hours")
        plt.title("Study Graph")
        plt.show()

    except Exception as e:
        print("Error:", e, "\n")


# ---------------- TIMER ----------------
def timer_window():
    subject = input("Enter subject: ")

    try:
        minutes = int(input("Enter minutes: "))
    except:
        print("Invalid input\n")
        return

    seconds = minutes * 60

    win = tk.Tk()
    win.title("Study Timer")
    win.geometry("300x200")

    label = tk.Label(win, font=("Arial", 30))
    label.pack(pady=40)

    def update():
        nonlocal seconds

        if seconds >= 0:
            m = seconds // 60
            s = seconds % 60

            label.config(text=str(m).zfill(2) + ":" + str(s).zfill(2))
            seconds -= 1
            win.after(1000, update)
        else:
            label.config(text="Time Up!")

            hours = minutes / 60
            with open("study.txt", "a") as f:
                f.write(subject + "," + str(hours) + "\n")

            print("Study time saved\n")

    update()
    win.mainloop()


# ---------------- ML PREDICTION ----------------
def predict():
    try:
        with open("study.txt", "r") as f:
            data = f.readlines()

        X = []
        y = []

        for i, line in enumerate(data):
            if "," not in line:
                continue

            s, h = line.strip().split(",")

            try:
                h = float(h)
            except:
                continue

            X.append([i])
            y.append(h)

        if len(X) < 2:
            print("Not enough data for prediction\n")
            return

        print("\n🤖 MACHINE LEARNING ANALYSIS:")

        if ml_available:
            model = LinearRegression()
            model.fit(X, y)

            pred = model.predict([[len(X)]])

            print("\n📊 Predicted Study Hours for Next Day:",
                  round(pred[0], 2), "hours")

        else:
            pred = sum(y) / len(y)

            print("ML library not available → Using Average Logic")
            print("Past Study Hours:", y)

            print("\n📊 Approx Prediction:",
                  round(pred, 2), "hours")

        print()

    except Exception as e:
        print("Error:", e, "\n")

# ---------------- AI RECOMMEND ----------------
def recommend():
    try:
        with open("study.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("No data available\n")
            return

        d = {}

        for line in data:
            if "," not in line:
                continue

            s, h = line.strip().split(",")

            try:
                h = float(h)
            except:
                continue

            d[s] = d.get(s, 0) + h

        if len(d) == 0:
            print("No valid data\n")
            return

        avg = sum(d.values()) / len(d)

        print("\n📊 AI Recommendation:")

        for sub in d:
            if d[sub] < avg:
                print(sub, "→ Increase time")
            else:
                print(sub, "→ Good")

        print()

    except Exception as e:
        print("Error:", e, "\n")


# ---------------- ANALYSIS ----------------
def analysis():
    try:
        with open("study.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("No data\n")
            return

        d = {}

        for line in data:
            if "," not in line:
                continue

            s, h = line.strip().split(",")

            try:
                h = float(h)
            except:
                continue

            d[s] = d.get(s, 0) + h

        if len(d) == 0:
            print("No valid data\n")
            return

        print("\n📉 Analysis:")
        print("Weakest:", min(d, key=d.get))
        print("Strongest:", max(d, key=d.get))
        print()

    except Exception as e:
        print("Error:", e, "\n")


# ---------------- MENU ----------------
while True:
    print("\n====== AI + ML STUDY PLANNER ======")
    print("1 Add Study")
    print("2 View Data")
    print("3 Timer (GUI)")
    print("4 Graph")
    print("5 Prediction (AI + ML)")
    print("6 Recommendation (AI)")
    print("7 Analysis")
    print("8 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        view()
    elif ch == "3":
        timer_window()
    elif ch == "4":
        graph()
    elif ch == "5":
        predict()
    elif ch == "6":
        recommend()
    elif ch == "7":
        analysis()
    elif ch == "8":
        print("Exit")
        break
    else:
        print("Wrong choice\n")
