import random

a2=[i for i in range(1,26)]


def story():
    s1=["Princess Cimorene is not a proper princess. Nor is Kazul a typical dragon. But being a Dragon’s Princess is a respectable enough job for her family to leave Cimorene in peace. In Wrede’s world, humans and dragons can form friendships together at any age, if they are polite beings. The ability to make a good cherries jubilee turns out to be a helpful skill in building friendships as well. And when magic is involved, being rude has unexpected consequences","Once upon a time in the middle of winter, when the flakes of snow were falling like feathers from the clouds, a Queen sat at her palace window, which had an ebony black frame, stitching her husband’s shirts. While she was thus engaged and looking out at the snow she pricked her finger, and three drops of blood fell upon the snow. Now the red looked so well upon the white that she thought to herself, “Oh, that I had a child as white as this snow, as red as this blood, and as black as the wood of this frame!” Soon afterwards a little daughter came to her, who was as white as snow, and with cheeks as red as blood, and with hair as black as ebony, and from this she was named “Snow-White.” And at the same time her mother died.","There was once a shoemaker, who worked very hard and was very honest: but still he could not earn enough to live upon; and at last all he had in the world was gone, save just leather enough to make one pair of shoes.","Then he cut his leather out, all ready to make up the next day, meaning to rise early in the morning to his work. His conscience was clear and his heart light amidst all his troubles; so he went peaceably to bed, left all his cares to Heaven, and soon fell asleep. In the morning after he had said his prayers, he sat himself down to his work; when, to his great wonder, there stood the shoes all ready made, upon the table. The good man knew not what to say or think at such an odd thing happening. He looked at the workmanship; there was not one false stitch in the whole job; all was so neat and true, that it was quite a masterpiece.","There was once upon a time an old goat who had seven little kids, and loved them with all the love of a mother for her children.","One day she wanted to go into the forest and fetch some food. So she called all seven to her and said:","‘Dear children, I have to go into the forest, be on your guard against the wolf; if he comes in, he will devour you all—skin, hair, and everything. The wretch often disguises himself, but you will know him at once by his rough voice and his black feet.","Far out in the ocean, where the water is as blue as the prettiest cornflower and as clear as crystal, it is very, very deep; so deep, indeed, that no cable could sound it, and many church steeples, piled one upon another, would not reach from the ground beneath to the surface of the water above. There dwell the Sea King and his subjects.","We must not imagine that there is nothing at the bottom of the sea but bare yellow sand. No, indeed, for on this sand grow the strangest flowers and plants, the leaves and stems of which are so pliant that the slightest agitation of the water causes them to stir as if they had life. Fishes, both large and small, glide between the branches as birds fly among the trees here upon land."]
    a=random.choice(s1)
    print('\n\t\b',a)
story()
man=input('\n\t\bEnter your name :-')
def game():
    
    b=100
    b1=100
    c=[]
    c1=[]
    
    while b:
        print(f'\n\t\b {man} HP ({b})\t\t\b dragon HP({b1})')
        print('\n\t\bFight with dragon using numbers')
        man1=int(input('\n\t\bEnter numbers (1 to 25):- '))

        if man1 in c:
            print(f'\n\t\bYou already fill that value {c} please fill another value')
            man1=int(input('\n\t\bEnter the numbers (1 to 25):- '))
            
        while man1 not in a2:
            print('\n\t\b Invalid choice . Please fill correct !!')
            man1=int(input('\n\t\bEnter the numbers (1 to 25):- '))
        while man1>b1:
            man1=int(input('\n\t\bEnter the numbers (1 to 25):- '))
        
        c.append(man1)
        
        dragon=random.randint(1,25)
        if dragon in c1:
            dragon=random.randint(1,25)
        while dragon>b:
            dragon=random.randint(1,25)
        print(f'\n\t\b Dragon attack :- {dragon}')
        c1.append(dragon)
        
        b=b-dragon
        b1=b1-man1
        
        if b==0:
            print(f'\n\t\b{man} lost')
            print(f'\n\t\b {man} HP ({b})\t\t\b dragon HP({b1})')
            break
        elif b1==0:
            print(f'\n\t\b {man} HP ({b})\t\t\b dragon HP({b1})')
            print(f'\n\t\b {man} win')
            break
game()
while True:

    print('\n\t\b 1.Play again \n\t\b 2.Exit')
    option=int(input('\n\t\b Enter your choice :- '))
    if option==1:
        story()
        game()
        
    elif option==2:
        exit()
        