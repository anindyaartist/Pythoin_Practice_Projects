
import datetime

name=input("Enter your name").strip()
city=input("Enter your city").strip()
age=input("Enter your age").strip()
hobby=input("Enter your hobby").strip()
profession=input("Enter your profession").strip()

intro_message= (
    f"Hello! My name is {name}, I am {age} years old and live in {city}"
    f"I work as a {profession} and i love {hobby} in my free time\n"
    f"Nice to meet you!\n"
)

current_date= datetime.date.today().isoformat()
intro_message+=f"\n Logged on: {current_date}"
border="*"*80
final_output=f"{border}\n{intro_message}\n{border}"
print("\n"+final_output)
