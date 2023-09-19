import random

print('WELCOME TO THE GAME OF SCRAMBLED WORDS !!!')
print('In this game you will given jumbled words and You will have to guess the correct word. If correct, then you will gain a point !! ')
print(' ')
ro=int(input("Enter the number of rounds you want to play: "))
wordlist =['hypothesis', 'sandalwood', 'elusive', 'naive', 'complement', 'exclusive', 'heavenly', 'decisive', 'malicious', 'murmured', 'bestseller', 'unicorn', 'glorious', 'grumpy', 'convincing', 'expired', 'reason', 'conference']
score=0
for i in range(ro):
    word=random.choice(wordlist)
    word_list = list(word)
    random.shuffle(word_list)
    mix = ''.join(word_list)
    print(mix)
    cou=4
    for j in range(ro):
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

if score/ro > 0.87:
    print('BRAVO !!!')
elif score/ro >0.70 :
    print('VERY GOOD !!')
elif score/ro > 0.50:
    print('GOOD !! BUT CAN DO BETTER :)')
elif score/ro > 0.4:
    print('NEEDS IMPROVEMENT !')
else:
    print('Failed miserably')
