
import requests
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:5000/api/students"


def main():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    students = response.json()

    if not students:
        print("No student records found.")
        return

    names = [student["name"] for student in students]
    scores = [student["score"] for student in students]

    average = sum(scores) / len(scores)

    print("Student Test Scores")
    print("-" * 35)

    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    print("-" * 35)
    print(f"Average score: {average:.2f}")

    bars = plt.bar(names, scores)
    plt.bar_label(bars, padding=3)
    plt.axhline(
        average,
        linestyle="--",
        label=f"Average: {average:.2f}"
    )

    plt.title("Student Test Scores")
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()
    plt.savefig("student_scores.png")
    plt.show()


if __name__ == "__main__":
    main()
