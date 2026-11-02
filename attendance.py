students = {
    "S001": {"name": "Alice", "attended": 18, "total": 20},
    "S002": {"name": "Bob", "attended": 14, "total": 20},
    "S003": {"name": "Charlie", "attended": 20, "total": 20},
    "S004": {"name": "Diana", "attended": 0, "total": 20},
}


def calculate_attendance(attended, total):
    if total <= 0:
        raise ValueError("Total classes must be greater than zero")
    if attended < 0 or attended > total:
        raise ValueError("Invalid attendance values")
    return (attended / total) * 100


def generate_report(filepath="attendance_report.txt"):
    lines = []
    lines.append("Student Attendance Report")
    lines.append("=" * 40)
    for sid, data in students.items():
        pct = calculate_attendance(data["attended"], data["total"])
        status = "OK" if pct >= 75 else "LOW"
        lines.append(f"{sid} | {data['name']:10s} | {pct:.1f}% | {status}")
    report = "\n".join(lines)
    with open(filepath, "w") as f:
        f.write(report)
    return report


def print_summary():
    report = generate_report()
    print(report)


if __name__ == "__main__":
    print_summary()
