poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

# Splitting Strings

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# Splitting Strings III
spring_storm_text = \
    """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)

# Joining Strings
print("TASK")
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)

# Joining Strings II
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
                      'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds',
                      'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

# .strip()
print("################################")
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']
love_maybe_lines_stripped = []
print(love_maybe_lines)

for i in love_maybe_lines:
    love_maybe_lines_stripped.append(i.strip())

print(love_maybe_lines_stripped)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

# Replace
print("################################")
toomer_bio = \
    """
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# .find()
print("################################")
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

# .format()
print("################################")


def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)


# .format() II
print("################################")


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date,author,title,original_work)

# Review
print("################################")

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela " \
                    "Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold " \
                    "Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico " \
                    "City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, " \
                    "Dreamwood:Adrienne Rich:1987 "

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []

for i in highlighted_poems_list:
    highlighted_poems_stripped.append(i.strip())

print(highlighted_poems_stripped)

highlighted_poems_details = []

for i in highlighted_poems_stripped:
    highlighted_poems_details.append(i.split(":"))

print("############################")
titles = []
poets = []
dates = []

for i in highlighted_poems_details:
    titles.append(i[0])
    poets.append(i[1])
    dates.append(i[2])


for i in range(0, len(highlighted_poems_details)):
    print("The poem {title} was published by {poet} in {date}".format(title=titles[i], poet=poets[i], date=dates[i]))




