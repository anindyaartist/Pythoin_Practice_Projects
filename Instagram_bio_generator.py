#also contains a option to download the text in .txt

import textwrap
name=input("enter your name: ").strip()
profession=input("enter your profession: ").strip()
passion=input("enter your passion: ").strip()
emoji=input("enter your emoji: ").strip()
website=input("enter your website: ").strip()
print("\n Choose your style")
print("1. Simple lines")
print("2.Vertical flair")
print("3.Emoji sandwitch")
style=input("Enter 1,2 or 3: ").strip()
def generate_bio(style):
    if style == "1":
        return f"{emoji}{name}| {profession} \n 💡{passion}\n{website}"
    elif style=="2":
        return f"{emoji}{name}\n{profession}🔥\n{passion}\n{website}"
    elif style=="3":
        return f"{emoji*3}\n{name} - {passion}\n{profession}\n{website}\n{emoji*3}"   
bio=generate_bio(style)
print("*"*50)
print(textwrap.dedent(bio))
print("*"*50)
bio=generate_bio(style)
save=input("Do you want to save this bio in a text file?(y/n:)").lower()

if save=="y":
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename,"w", encoding="utf-8") as f:
        f.write(bio)
    print("Your file is saved!")
