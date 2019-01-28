import random
from codecs import open

#function to handle playing in each word
def playWord(word,hint,totalScore) :
    answerSet = set()
    for alp in word.upper() :
        if alp.isalpha() :
            answerSet.add(alp)
    guessAlphabet = set()
    correctGuess = set()
    wrongGuess = list()
    currentScore = 100
    chance = 8
    while chance > 0 :
        out = ''
        for alp in word :
            if (not alp.isalpha()) or (alp.upper() in correctGuess) :
                out += alp + ' '
            else :
                out += '_ '
        wrong = ''
        for alp in wrongGuess :
            wrong += alp + ' '
        print('\n' + out.strip() + '\tHint: ' + hint + '\tScore for this word: ' + str(currentScore) + ' , Your total score: ' + str(totalScore) + ' , Remaining chance(s): ' + str(chance) + ' , Wrong guessd: ' + wrong.strip())
        if chance > 1 :
            guess = input('Guess >>> ').upper()
        else :
            guess = input('Final Chance!!! Guess! >>> ').upper()
        while (not guess.isalpha()) or (guess in guessAlphabet) or (len(guess) != 1) :
            if guess in guessAlphabet :
                print('You have already guessed this alphabet.')
            elif (not guess.isalpha()) or (len(guess) != 1) :
                print('Invalid input')
            guess = input('Guess >>> ').upper()
        if guess not in answerSet :
            currentScore -= 10
            chance -= 1
            guessAlphabet.add(guess)
            wrongGuess.append(guess)
        else :
            guessAlphabet.add(guess)
            correctGuess.add(guess)
            answerSet.remove(guess)
        if len(answerSet) <= 0 :
            return currentScore
    return 0

#function to handle playing through the category
def playCategory(category) :
    totalScore = 0
    wordList = list()
    splitWord = '__h!Nt_'
    for wordAndHint in category :
        wordList.append(wordAndHint.strip().split(splitWord))
    categorySize = len(wordList)
    while categorySize > 0 :
        print('\n' + str(categorySize) + ' word(s) left...')
        index = random.randint(0,categorySize-1)
        nextWord = wordList[index]
        wordList.remove(wordList[index])
        categorySize -= 1
        pendingScore = playWord(nextWord[0],nextWord[1],totalScore)
        if pendingScore <= 0 :
            print('\nThe word is "' + nextWord[0] +'". ' + 'Opps!!! You failed this word !')
        else :
            print('\nThe word is "' + nextWord[0] +'". ' + 'Congratulation!!! You won this word !')
        totalScore += pendingScore
    print('\nYou end this game with ' + str(totalScore) + ' scores.')
    while True :
        print('\nType "play" to continue playing or "exit" to leave.')
        playOrLeave = input('>>>').strip().lower()
        if playOrLeave == 'play' :
            return
        elif playOrLeave == 'exit' :
            exit(0)
        else :
            print('Invalid input')

def main() :
    print('Let\'s Play Hangman!')
    while True :
        while True :
            print('Select the category from the categories below:')
            print('\nSong' + '\nAnimal' + '\n')
            chosen = input('Enter the name of category or "exit" to leave: ').lower().strip()
            if (chosen == 'exit'):
                exit(0)
            try :
                file = open(chosen + '.txt','r',encoding='utf-8')
                break
            except :
                print('\nThe category you enter does not exist.\n')
        playCategory(file)
    file.close()

main()