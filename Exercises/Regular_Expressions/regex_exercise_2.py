import re

text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. 
Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""

pattern1 = "\w+@\w+.\w+" 
pattern2 = "\w{3,6}"

x = re.findall(pattern1, text)
y = re.search(pattern2, text)

print("All emails in text are as follows:\n", x)

print("All words with a span of 3 characters\n", y)