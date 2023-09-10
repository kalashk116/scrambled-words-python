import random

print('WELCOME TO THE GAME OF SCRAMBLED WORDS !!!')
print('In this game you will given jumbled words and You will have to guess the correct word. If correct, then you will gain a point !! ')
print(' ')
print('you will be given 5 rounds to play !!')
wordlist =['hypothesis', 'sandalwood', 'elusive', 'naive', 'complement', 'exclusive', 'heavenly', 'decisive', 'malicious', 'murmured', 'bestseller', 'unicorn', 'glorious', 'grumpy', 'convincing', 'expired', 'reason', 'conference']
score=0
for i in range(5):
    word=random.choice(wordlist)
    word_list = list(word)
    random.shuffle(word_list)
    mix = ''.join(word_list)
    print(mix)
    cou=4
    for j in range(5):
        answer = input()

        if answer == word :
            print('Correct answer !!! You gain a point')
            score = score + 1
            print("your score is ",score)
            break
        else:
            if cou>1:
                cou=cou-1
                cou=cou
                print(cou, " tries left")
                print("try again")
            elif cou==1:
                print('Its you last chance, your all tries have been exhausted. if you fail you will be given another word !!')
            elif cou==0:
                print('all tries exhausted. Here is another word')

if score==5:
    print('BRAVO !!!')
elif score==4:
    print('VERY GOOD !!')
elif score==3:
    print('GOOD !! BUT CAN DO BETTER :)')
elif score==2:
    print('NEEDS IMPROVEMENT !!')
else:
    print('Go and pick up a dictionary asshole')