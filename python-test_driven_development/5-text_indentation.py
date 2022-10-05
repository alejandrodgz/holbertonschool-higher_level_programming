#!/usr/bin/python3
'''this the 5-text_indentation module with one function
called text_indentation, the function creates a new line
when these characteres are found (. , ? :)'''


def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError('text must be a string')
    a = 0
    for i in range(len(text)):
        if (text[i] == '.') or (text[i] == '?' or text[i] == ':'):
            new_string = text[a:i + 1]
            print(new_string)
            print("")
            a = i + 2
    new_string = text[a:i + 1]
    print(new_string, end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")