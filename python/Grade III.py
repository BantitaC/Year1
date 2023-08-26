'''Grade III'''
def grade(subject):
    '''Grade III'''
    total = 0
    for _ in range(1, subject+1, 1):
        score = float(input())
        if score >= 95 and score <= 100:
            total += 4
        elif score >= 90 and score < 95:
            total += 3.5
        elif score >= 85 and score < 90:
            total += 3
        elif score >= 80 and score < 85:
            total += 2.5
        elif score >= 75 and score < 80:
            total += 2
        elif score >= 70 and score < 75:
            total += 1.5
        elif score >= 65 and score < 70:
            total += 1
        elif score >= 60 and score < 65:
            total += 0.5
        elif score >= 0 and score < 60:
            total += 0
    result = total/subject
    print("%.2f" % (int(result*100)/100))
grade(int(input()))
