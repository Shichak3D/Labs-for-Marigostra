import nltk
from pymorphy3 import MorphAnalyzer
from snowballstemmer import stemmer

with open("Andreev_Leonid_Bezdna_Litmir_club_47718_ddd89.txt", mode="r") as file:
    text = file.read()

nltk_text_segment = nltk.sent_tokenize(text)

def find_pairs(text_segment):
    analyzer = MorphAnalyzer()
    necessary_part_speech = [
        "NOUN",
        "ADJF",
        "ADJS"
    ]

    finded_pairs = []

    for sentence in text_segment:
        tokenized_sentence = nltk.word_tokenize(sentence)

        for index in range(0, len(tokenized_sentence)):
            word = tokenized_sentence[index]
            word_anylyze = analyzer.parse(word)[0]
            part_speech = word_anylyze.tag.POS

            if part_speech in necessary_part_speech:
                word_pair = tokenized_sentence[index + 1]
                word_pair_analyze = analyzer.parse(word_pair)[0]
                part_speech_pair = word_pair_analyze.tag.POS


                if part_speech_pair in necessary_part_speech:
                    gender_1 = word_anylyze.tag.gender
                    gender_2 = word_pair_analyze.tag.gender

                    number_1 = word_anylyze.tag.number
                    number_2 = word_pair_analyze.tag.number

                    case_1 = word_anylyze.tag.case
                    case_2 = word_pair_analyze.tag.case

                    if (gender_1 != None and gender_1 != None) and (gender_1 != gender_2):
                        break
                    if (number_1 != None and number_2 != None) and (number_1 != number_2):
                        break
                    if (case_1 != None and case_2 != None) and (case_1 != case_2):
                        break

                    finded_pairs.append(
                        [word_anylyze.normal_form, word_pair_analyze.normal_form]
                    )

    return finded_pairs

task_1_pairs = find_pairs(nltk_text_segment)
print(task_1_pairs)
