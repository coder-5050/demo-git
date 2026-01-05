import random

subject=["sahil","ashish","ravi","abhay","kamakshi","shreya","neha","sanajana","abhijeet"]
action=["eat","poop","laugh","dance","walk","run","poking"]
place=["home","red fort","kota","school","assembly"]

while True:
    
    subject= random.choice(subject)
    place=random.choice(place)
    action=random.choice(action)


    headline=f"{subject} {action} {place}"

    print ("\n"+ headline)
    
    user=input("\ndo you want to generate another headline(yes/no)").strip().lower()

    if user=="no":
        break