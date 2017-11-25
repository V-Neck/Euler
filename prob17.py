ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
TENS = ['', 'teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

first_twenty = """
one
two
three
four
five
six
seven
eight
nine
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen"""

first_twenty = first_twenty.split("\n")

names = {}
for hundred in range(10):
    for ten in range(10):
        for one in range(10):
            num = ""
            if ten < 2:
                last_two_digits = first_twenty[10*ten + one]
            else:
                last_two_digits = TENS[ten] + ONES[one]
            num = ""
            if hundred > 0:
                if last_two_digits == "":
                    hundreds = ONES[hundred] + "hundred"
                else:
                    hundreds = ONES[hundred] + "hundredand"
            digit = hundreds + last_two_digits
            names[100 * hundred + 10 * ten + one] = digit

names[1000] = "onethousand"

print (len("".join(names.values())))
