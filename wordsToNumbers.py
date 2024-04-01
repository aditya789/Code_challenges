'''Challenge 1

In this problem, you will be given one or more integers in English. Your task is to translate these numbers into their integer representation. The numbers can range from negative 999,999,999 to positive 999,999,999. The following is an exhaustive list of English words that your program must account for:
negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million

INPUT AND OUTPUT

Notes on input:

•	Negative numbers will be preceded by the word negative.
•	The word “hundred” is not used when “thousand” could be. For example, 1500 is written “one thousand five hundred”, not “fifteen hundred”.

SAMPLE INPUT

six, negative seven hundred twenty nine, one million one hundred one

SAMPLE OUTPUT

6, -729, 1000101


Python Version :: Python 3.11.3
Package used :: word2number-1.1
Source :: https://pypi.org/project/word2number/'''

from word2number import w2n

def wordsToNumber(words):
      for word in words.split():
            if word.isnumeric():
                  raise Exception(f'Word Should not contain number {word}')
      result = w2n.word_to_num(words.replace('negative',''))
      number = -result if words.startswith('negative') else result
      return number


# Calling the function with few inputs
inputs =['six', 'negative seven hundred twenty nine', 'one million one hundred one']
for i in inputs:
      output = wordsToNumber(i)
      print(f'{i} : {output}')
