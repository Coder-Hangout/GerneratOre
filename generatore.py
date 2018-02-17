import random


# returns a with config gennerated string
def generate(config):
    out = ""
    words = config[0]
    structure = config[1]
    out += gen_str(structure, words)
    return out


# gets a random word from words[num]
def get_word(num, words):
    if num == -1:
        return ""
    collection = words[num]
    rand = random.randint(1, len(collection) - 1)
    return collection[rand] + " "


# gennerates a string out of struc
def gen_str(struc, words):
    out = ""

    if type(struc) is int:
        out += get_word(struc, words)
    else:
        for c in range(1, len(struc)):
            on = struc[c]
            if type(on) is int:
                out += get_word(on, words)
            else:
                max_percent = 0
                percent_list = []

                for i in on:
                    max_percent += i[0]
                    percent_list += [max_percent]

                rand = random.randint(1, max_percent)

                for j in range(0, len(percent_list)):
                    if percent_list[j] >= rand:
                        out += gen_str(on[j], words)
                        # print(percent_list)
                        # print(max_percent)
                        # print(j)
                        # print(rand)
                        break

    return out


# returns a list with the description and the number of a category to that things can get added
def get_addable(config):
    words = config[0]
    description = "!"
    counter = 0
    for i in words:
        if i[0].startswith("!"):
            counter += 1
    if counter == len(words):
        return ["!Error: nothing avainable", -1]
    while description.startswith("!"):
        rand = random.randint(0, len(words) - 1)
        description = words[rand][0]
    return [description, rand]


# used to add a word  to the addabele/num inside config
def add_addable(config, word, num):
    if num != -1:
        words = config[0]
        words[num] += [word]


# example code:
conf = [
    [
        ["pre", "the", "Dr", "old"],
        ["evil adjectives", "evil", "angry"],
        ["good adjectives", "good", "great", "glorious"],
        ["first name", "Tim", "Tom", "Ben", "Jac", "Mike", "Chad", "Rohn", "Henry", "Frank", "Greg", "Joe", "Andrew",
         "Donald", "Noha", "Nathan", "John", "Robert", "Leo", "Thomas", "James", "Logan", "Archie", "Theo", "Henry",
         "Max", "Joshua", "William", "Lucas", "Ethan", "Mason", "Harrison", "Isaac", "Finley", "Teddy", "Alexander",
         "Riley", "Arthur", "Daniel", "Joseph", "Adam", "Edward", "Samuel", "Reggie", "Benjamin", "Sebastian", "Dylan",
         "Jaxon", "Jake", "Toby", "Harley", "Elijah", "Jenson", "Carter", "Arlo", "Louie", "Lewis", "Tommy", "Jude",
         "Hugo", "Ollie", "David", "Rory", "Alex", "Bobby", "Frankie", "Ronnie", "Jackson", "Matthew", "Zachary",
         "Harvey", "Jayden", "Luca", "Blake", "Nathan", "Elliot", "Albie", "Caleb", "Reuben", "Hunter", "Luke", "Tyler",
         "Stanley", "Michael", "Dexter", "Theodore", "Roman", "Ryan", "Albert", "Elliott", "Ellis", "Kai", "Louis",
         "Liam", "Finn", "Connor", "Austin", "Ezra", "Aiden", "Jamie", "Callum", "Leon", "Aaron", "Finlay", "Gabriel",
         "Eli", "Ben", "Grayson"],
        ["last names", "Wolf", "Smith", "Miller", "Jones", "Williams", "Taylor", "Davies", "Rubik", "Brown", "Wilson",
         "Evans", "Thomas", "Johnson", "Trump", "Roberts", "Walker", "Wright", "Robinson", "Thompson", "White",
         "Hughes", "Edwards", "Green", "Lewis", "Wood", "Harris", "Martin", "Jackson", "Clarke", "Chips", "Hatman",
         "Temples", "Raynott", "Woodbead", "Nithercott", "Rummage", "Southwark", "Harred", "Jarsdel"],
        ["!aristocratics", "von", "van", "from","of"],
        ["citys", "london", "verdict village", "new castell"]
    ],
    [
        1, [[5, -1], [1, 0]], [[7, -1], [3, 1], [5, 2]], 3, [[10, 4], [1, 5, 6]]
    ]
]

for i in range(0, 25):
    print(generate(conf))
