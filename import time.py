import time 
import random
def get_divisor(n):
    l=[]
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)
if __name__ == "__main__":
    ops=["+", "-", "*", "/"]
    start_time = time.time()
    total =0
    correct =0
    questions = []
    while time.time() - start_time <= 60:
        a = random.randint(1,99)
        op = random.choice(ops)
        if op =="/":
            b = get_divisor(a)
        else:
            b= random.randint(1,99)
        a_op_b = "{} {} {}".format(a, op, b)
        c=int(eval(a_op_b))
        try:
            ans = int(input('{} = '.format(a_op_b)))
        except:
            ans=""
        if time.time() - start_time <=60:
            if c ==ans:
                print("Correct!")
                correct +=1
            else:                print("Wrong! The correct answer is {}".format(c))
            total +=1
            questions.append("{} = {}".format(a_op_b, ans))
print('{} questions and your correct rate is {:.2f}%'.format(total, correct / total * 100))
for q in questions:
    print(q)
        