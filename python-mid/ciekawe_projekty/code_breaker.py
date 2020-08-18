"""
BASED ON given kay phrases you can encode or decode a message (just lettars for now but gonna get bigger)
My phrases are from Sherlock Holmes :)
"""

from collections import Counter

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ';', '(', ')',
               '%', '$', '&', '#', '\n', '\t']

key_phrase_1 = """
    To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name.17In his eyes she 
    eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler.18All
    emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.19He was, I take
    it, the most perfect reasoning and observing machine that the world has seen,20but as a lover he would have placed 
    himself in a false position.21He never spoke of the softer passions, save with a gibe and a sneer."""
key_phrase_2 = """
    78Quite so! You have not observed. And yet you have seen.79That is just my point. Now, I know that
    there are seventeen steps, because I have both seen and observed.80By the way, since you are interested in these little 
    problems,81and since you are good enough to chronicle one or two of my trifling experiences, you may be interested 
    in this.82He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table.83It came 
    by the last post, said he."""


def clean(phrase):
    phrase = phrase.lower()
    for letter in phrase:
        if letter in non_letters:
            phrase = phrase.replace(letter, '')
    return phrase


def order(phrase):
    letter_count = Counter(phrase)
    ordered_list_of_letters = letter_count.most_common()
    phrase_ordered_letters = []
    for items in ordered_list_of_letters:
        phrase_ordered_letters.append(items[0])
    return phrase_ordered_letters


def choicer():
    phrase_one = clean(key_phrase_1)
    phrase_two = clean(key_phrase_2)
    ordered_phase_one = order(phrase_one)
    ordered_phase_two = order(phrase_two)

    choice = input("\n\nWould you like to encode or decode a message: ").lower()
    choice = clean(choice)
    phrase = input("What is the phrase: ").lower()
    phrase = clean(phrase)
    if choice == 'encode':
        coded = []
        for letter in phrase:
            index = ordered_phase_one.index(letter)
            coded.append(ordered_phase_two[index])
        return coded
    elif choice == 'decode':
        coded = []
        for letter in phrase:
            index = ordered_phase_two.index(letter)
            coded.append(ordered_phase_one[index])
        return coded


if __name__ == '__main__':
    print(choicer())
