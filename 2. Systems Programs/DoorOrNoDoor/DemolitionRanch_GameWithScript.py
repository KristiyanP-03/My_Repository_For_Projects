from time import sleep
name = input("Your name is? ")
print("Denny: Welcome to Door or No Door!")
sleep(3)
print("My name is Denny from Denny's doorknobs and doorbells.", end=" ")
print("We are going to have a game today, that's going to blow your mind.", end=" ")
print("We're going to pick one lucky contestant today to step up here", end=" ")
print("and play Doorbell dings or No Doorbell dings.")
sleep(20)
print(f"Denny: Let's see. The first one up, the first contestant is ...")
sleep(8)
print(name + "!" + " *applause crownd cheering sound*")
sleep(1)
print(f"Are you here? {name} where are you? Is he you? Oh, come on over here!")
sleep(5)
print("Wow, congratulations! Nice to meet you.")
sleep(3)
print("You: Thank you, Sir! Thank you!")
sleep(1)
print("Denny: So you ... ? What do you need ... to go to collage or something?")
sleep(1)
answer_collage = input("You: ")
sleep(2)
print("Denny: Oh, you must have a job ... what do you do for a living?")
sleep(1)
answer_job = input("You: ")
sleep(2)
print("Denny: Okay ... well we're gonna play Door dingers and Not Door dingers ...")
sleep(1)
print("*louder applause crownd cheering sound*")
sleep(5)
print("Denny: ... and all you have to do is pick which door and you will win the", end=" ")
print("price thats is behind it.", end=" ")
print("So, son. Let's see which door would you like to pick first?")
sleep(13)
door_picked_number = int(input("Console: You have 3 doors. Pick one of them. "))
print(f"You: Door number {door_picked_number}")
sleep(2)
print("Denny: You got it, bud! *more louder applause crownd cheering sound*")
sleep(2)
print(f"Denny: Let's get it going baby! What do we have behind door number {door_picked_number}?")
sleep(1)
print(f"*you opens door number {door_picked_number}*")
sleep(5)

# part 1 / not door number 3 , meant door number 2
if door_picked_number == 3:
        print("A full tank of gasoline ... actually it's three quarters full tank of gasoli...", end="")
        print(" I'm pretty sure that's 91 octane. That's not bad!")
        sleep(11)
        misheard_number = int(input("Console: You meant door number ...? "))
        print(f"You: I meant door number {misheard_number}")
        sleep(2)
        print("Denny: Oh, oh ... I must have misheard you, son. Come on, well, let's close that.", end=" ")
        print("That'll be the next contestant win that one.")
        sleep(8)
        print("*you closes the door*")
        sleep(1)
        print(f"Denny: Let's see what's behind door number {misheard_number}, folks.", end=" ")
        print("This is gonna be good, this is gonna change your life.")
        sleep(9)
        print(f"*you opens door number {misheard_number}*")
        sleep(1)
        print("*applause crownd cheering sound*")
        sleep(5)

# part 2 / you have 3 of these mini-bikes
if misheard_number == 2:
    print("Denny: A brand new, well, almost new motorcycle! Amazing! It's a mini-bike,", end=" ")
    print("though so you can't actually get it street legal. You just have to ride it like on the sidewalk.")
    sleep(15)
    unneded_bikes = int(input("Console: You have 3 of these. You meant door number ...? "))
    print("You: I have three of these.")
    sleep(3)
    print("Denny: You are homelees and you have three of these and don't ...")
    sleep(1)
    print(f"You: I MEANT ... okay, look, look. I meant door number {unneded_bikes}, okay?")
    sleep(6)
    print("Denny wispers to you: Nah, anyway ... I don't ... we usualy don't do that, uh, like switching ...")
    sleep(9)
    print(f"Denny: You know what, folks? I like this kid. What do you guys think, we should let him open door number {unneded_bikes}.")
    sleep(7)
    print("*loud applause crownd cheering sound*")
    sleep(3)
    print(f"Denny: Folks, should we let him see what's behind door number {unneded_bikes}")
    sleep(6)
    print(f"*you opens door number {unneded_bikes}*")
    sleep(5)

# part 3 end / It's demolition range
if unneded_bikes == 1:
    print("*everyone is surprised*")
    print("Denny: It's Denny ... ")
    sleep(1)
    print("Denny: ... but nude. :)" )