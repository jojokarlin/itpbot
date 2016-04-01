#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import "random" library
import random

# Create word lists by part of speech
buzz_nouns = [
    "about", 
    "me", 
    "academia", 
    "agile", 
    "development", 
    "bios", 
    "Bootcamp", 
    "Chris Stein", 
    "collaboration",
    "Contexts",
    "Digital",
	"academia",
	"agile development",
	"bios",
	"Bootcamp",
	"Chris Stein",
	"collaboration",
	"Contexts",
	"Digital",
	"Fellows",
	"digital humanities",
	"discussion",
	"diversity",
	"education",
	"English",
	"Ethan Marcotte",
	"GCDI",
	"Get",
	"Real",
	"guest speakers",
	"independent study",
	"interactive",
	"intersectionality",
	"ITP 2011",
	"ITP 2016",
	"ITP",
	"students",
	"Jason Santa Maria",
	"learning",
	"lightning talks",
	"memory",
	"NYCDH",
	"Office",
	"Hours",
	"Omeka",
	"online",
	"Practicalities",
	"project development",
	"project proposals",
	"responsive web design",
	"scope creep",
	"start-up",
	"culture",
	"teaching",
	"technology",
	"Tom Kuhlmann",
	"user",
	"experience",
	"waterfall method",
	"Wikipedia",
	"workshops",
	"archive",
	"art",
	"Capitalism",
	"commodity",
	"biography",
	"Copyright",
	"Creative Commons",
	"critical",
	"pedagogy",
	"cyborg",
	"Cyborg Manifesto",
	"database",
	"Dialectic",
	"digital collection",
	"digital humanities",
	"Economic",
	"Structure",
	"Educational technology",
	"embodiment",
	"eversion",
	"evolution",
	"Feminism",
	"film",
	"Free software",
	"games",
	"gender",
	"Haraway",
	"HOW TO",
	"information",
	"internet",
	"Irony",
	"knowledge",
	"Labor",
	"learning",
	"Machines",
	"Marx",
	"N. Katherine Hayles",
	"Nakamura",
	"New Media",
	"open source",
	"pedagogy",
	"posthuman",
	"Power structure",
	"race",
	"sharing",
	"Technology",
	"Twitter",
	"Wikipedia",
	"Annotation",
	"Archive",
	"Assessment",
	"Attention",
	"Audio",
	"Blogging",
	"Classroom",
	"Code",
	"Collaboration",
	"Community",
	"Composition",
	"Curation",
	"Design",
	"Disability",
	"Failure",
	"Fieldwork",
	"Gaming",
	"Gender",
	"Hacking",
	"History",
	"Hybrid",
	"Information",
	"Interface",
	"Makerspace",
	"Multimodal",
	"Open",
	"Peer Review",
	"play",
	"Praxis",
	"professionalization",
	"project management",
	"prototyping",
	"public",
	"queer",
	"race",
	"remix",
	"rhetoric",
	"sexuality",
	"sound",
	"storytelling",
	"text analysis",
	"Video",
	"Work",
    "archive",
    "art",
    "Capitalism",
    "commodity",
    "biography",
    "copyright",
    "Creative Commons",
    "critical",
    "pedagogy",
    "cyborg",
    "Cyborg Manifesto",
    "database",
    "dialectic",
    "digital",
    "collection",
    "digital",
    "humanities",
    "Economic",
    "Structure",
    "Educational",
    "Technology",
    "embodiment",
    "eversion",
    "evolution",
    "Feminism",
    "film",
    "Free",
    "Software",
    "games",
    "gender",
    "Haraway",
    "HOWTO",
    "information",
    "internet",
    "Irony",
    "knowledge",
    "Labor",
    "learning",
    "Machines",
    "Marx",
    "N. Katherine Hayles",
    "Nakamura",
    "New media",
    "open",
    "source",
    "pedagogy",
    "posthuman",
    "Power",
    "Structure",
    "race",
    "sharing",
    "technology",
    "Twitter",
    "Wikipedia",
    "academia",
    "agile development",
    "bootcamp",
    "Chris Stein",
    "collaboration",
    "contexts",
    "digital",
    "Fellows",
    "digitalhumanities",
    "discussion",
    "diversity",
    "education",
    "English",
    "Ethan Marcotte",
    "GCDI",
    "Get Real",
    "guest speakers",
    "independent study",
    "interactive",
    "intersectionality",
    "ITP",
    "2011",
    "ITP2016",
    "ITP students",
    "Jason Santa Maria",
    "learning",
    "lightning",
    "talks",
    "memory",
    "NYCDH",
    "Omeka",
    "online",
    "Practicalities",
    "project development",
    "project proposals",
    "responsive web",
    "design",
    "scope creep",
    "start-up culture",
    "teaching technology",
    "user experience",
    "waterfall method",
    "Wikipedia workshops"
]


computer_adj = [
    "minimal",
    "neural",
    "synaptic",
    "solid state",
    "asymptotic",
    "concurrent",
    "multithreaded",
    "augmented",
    "presingularity",
    "responsive",
    "Cartesian",
    "extreme",
    "critical",
    "meatspace",
    "trinary",
    "recursive",
    "Pythonic",
    "functional",
    "imperative",
    "backend",
    "trontend",
    "social",
    "bio",
    "strategic",
    "sustainable",
    "value added",
    "holistic",
    "nano",
    "granular",
    "cloud",
    "content",
    "core",
    "brick-and-mortar",
    "digital",
    "cyber",
    "mono",
    "uni",
    "duplo",
    "curve",
    "cloud",
    "geodesic",
    "colocal",
    "electronic",
    "transcendant",
    "programatic",
    "media agnostic",
    "immersive",
    "technocratic",
    "AI",
    "VC",
    "procedural",
    "effective",
    "full spectrum",
    "analytic",
    "peer-to-peer",
    "semiotic",
    "best practice",
    "new",
    "viral",
    "zero-sum",
    "maker",
    "convergence",
    ]

# noncomp adjectives = [
# 	"Accurate",
# 	"Adaptable",
# 	"Agile",
# 	"Capable/capability",
# 	"Collaborative",
# 	"Competitive",
# 	"edge/advantage",
# 	"Cool under pressure",
# 	"Communication",
# 	"Confident",
# 	"Conflict resolution",
# 	"Consistent",
# 	"Creative",
# 	"Critical thinking",
# 	"Cross functional",
# 	"Culturally conscious",
# 	"Ethical",
# 	"Facilitator",
# 	"Flexible",
# 	"Focused",
# 	"Decision making",
# 	"Detail oriented",
# 	"Determination",
# 	"Diligent",
# 	"Directive",
# 	"Dynamic",
# 	"Effective",
# 	"Efficient",
# 	"Enthusiastic",
# 	"Follow-up",
# 	"Go getter",
# 	"Hardworking",
# 	"Initiative",
# 	"Innovative",
# 	"Integrity",
# 	"Intuitive",
# 	"Investigative",
# 	"Judgment",
# 	"Leader",
# 	"Mindful",
# 	"Motivated",
# 	"Negotiations",
# 	"Objective",
# 	"Organized",
# 	"Quality",
# 	"Quick learner",
# 	"Partnering",
# 	"Passionate",
# 	"Persuasive",
# 	"Prepared",
# 	"Proactive",
# 	"Problem solver",
# 	"Productive",
# 	"Professional",
# 	"Prompt",
# 	"Provide/provision",
# 	"Punctual",
# 	"Reliable",
# 	"Resourceful",
# 	"Respectable",
# 	"Respectful",
# 	"Responsive",
# 	"Selfless",
# 	"Service",
# 	"Specialist",
# 	"Strategic",
# 	"Tactical",
# 	"Task oriented",
# 	"Teamwork",
# 	"Technical",
# 	"Time management",
# 	"Transformative",
# 	"Troubleshooter",
# 	"Unifying",
# 	"Updated",
# 	"Visionary",
# 	"Well-written",

# 	]

# currency = [
#     "Dollar",
#     "Cent",
#     "Livre",
#     "Ducat",
#     "buck",
#     "Deutschmark",
#     "Euro",
#     "coin",
#     "wampum",
#     "porkbelly",
#     "future",
#     "bond",
#     "equity",
#     ]

computer_prefixes = [
    "neo",
    "net",
    "geo",
    "crypto",
    "info",
    "digi",
    "tele",
    "cyber",
    "compu",
    "meta",
    "hyper",
    "q-",
    "e-",
    "i",
    "micro",
    "ether",
    "macro",
    "mecha",
    "neuro",
    "tech",
    "x-",
    "stegano",
    "click",
    "pheno",
]

biparte_nouns = [
    "optics",
    "ops",
    "local",
    "drone",
    "vector",
    "graphy",
    "hacker",
    "blog",
    "speech",    
    "management",
    "design",
    "tech",
    "nocracy",
    "selfie",
    ]

# biparte_adjectives = [
#     "service",
#     "dendritic",
#     "centric",
#     "focused",
#     "morphic",
#     "dermic",
#     "sphere",
#     "desic",
#     "logical",
#     "thermic",
#     "nomic",
#     "factor",
#     ]


# buzz_gerund = [
#     "computing",
#     "making",
#     "dog fooding",
#     "growth hacking",
#     "newsjacking",
#     "deep linking",
#     ]

# politician = [
#     "Hillary Clinton",
#     "Barack Obama",
#     "Arnold Schwarzenegger",
#     "Mitt Romney",
#     "Paul Ryan",
#     "Sarah Palin",
#     "Queen Rania Al Abdullah",
#     "Bill Clinton",
#     "Goodluck Jonathan",
#     "Mike Huckabee",
#     "Herman Cain",
#     "Nicolas Sarkozy",
#     ]

# p_modifier = [
#     "Mecha",
#     "Cyber",
#     "Cyborg",
#     "Zombie",
#     "Posthuman",
#     "Pandimensional",
#     "3-D",
# ]

# post = [
#     "Prime Minister",
#     "President",
#     "Senator",
#     "Chairman",
#     "Representative",
#     "Hegemon",
#     "General",
#     "Secretary",
#     ]

# s_modifier = [
#     " 2.0",
#     " Prime",
#     "++",
#     " Bot",
#     ]

hashtags = [
    '#technology',
    '#futurism',
    '#innovation',
    '#strategics',
    '#digital',
    '#tech',
    '#future',
    '#analytics',
    '#b2b',
    '#BigData',
    '#data',
    '#business',
    '#cloud',
    '#contextmarketing',
    '#convergence',
    '#crm',
    '#epic',
    '#ftw',
    '#unfail',
    '#FCoE',
    '#thoughtleader',
    '#management',
    '#marketing',
    '#news',
    '#PredictiveAnalytics',
    '#strategy',
    '#upandcoming',
    '#virtualization',
    '#webdev',
    '#whitepaper',
    ]

verb = [
    "Accomplished",
    "Achieved",
    "Adapted",
    "Administered",
    "Advanced",
    "Analyzed",
    "Attained",
    "Balanced",
    "Brainstormed",
    "Budgeted",
    "Built",
    "Calculated",
    "Centralized",
    "Championed",
    "Changed",
    "Clarified",
    "Coached",
    "Collaborated",
    "Communicated",
    "Complied",
    "Conceptualized",
    "Configured",
    "Constructed",
    "Converted",
    "Created",
    "Decreased",
    "Delivered",
    "Demonstrated",
    "Designed",
    "Determined",
    "Developed",
    "Devised",
    "Directed",
    "Distributed",
    "Documented",
    "Earned",
    "Eliminated",
    "Energized",
    "Engineered",
    "Enhanced",
    "Ensured",
    "Established",
    "Evaluated",
    "Exceeded",
    "Excelled",
    "Executed",
    "Expedited",
    "Extract",
    "Facilitat",
    "Finalize",
    "Followup/through",
    "Forecast",
    "Form",
    "Fulfill",
    "Gained",
    "Generated",
    "Handled",
    "Headed",
    "Identified",
    "Implemented",
    "Improved",
    "Increased",
    "Initiated",
    "Innovated",
    "Installed",
    "Instituted",
    "Integrated",
    "Introduced",
    "Investigated",
    "Landed",
    "Launched",
    "Lead",
    "Maintained",
    "Managed",
    "Manufactured",
    "Maximized",
    "Monitored",
    "Negotiated",
    "Operated",
    "Optimized",
    "Ordered",
    "Organized",
    "Out",
    "Outsourced",
    "Overcame",
    "Oversaw",
    "Partnered",
    "Performed",
    "Piloted",
    "Pinpointed",
    "Planned",
    "Positioned",
    "Predicted",
    "Prepared",
    "Presented",
    "Prevented",
    "Processed",
    "Procured",
    "Produced",
    "Programmed",
    "Qualified",
    "Quantified",
    "Rebuilt",
    "Rectified",
    "Redefined",
    "Redesigned",
    "Re-engineered",
    "Related",
    "Resolved",
    "Restored",
    "Restructured",
    "Revitalized",
    "Salvaged",
    "Satisfied",
    "Saved",
    "Set-up",
    "Solved",
    "Specialized",
    "Streamlined",
    "Supported",
    "Tailored",
    "Tested",
    "Trained",
    "Uncovered",
    "Unified",
    "Upgraded",
    "Utilized",
    "Validated",
    "Wrote",

	]

handle = [
    "@saraevogel",
    "@trsober",
    "@jojokarlin",
    "@smythp",
    "@mauraweb",
    "@mandiberg",
    "@lisabrundage",
    "@RobertPRobinson",
    "@erinroseglass",
    "@JITPedagogy",
    "@miriamkp",
    "@audreywatters",
    "@mckinniburgh",
    "@ITP_NYU",
    "@syllabusproject",
    "@CUNYworks",
    "@laurhur ",
    "@DanicaSavonick",
    ]

# Define a function for each template
# These functions take words and randomly put them into preset sentences
# Note that I didn't use the first one
def create_politico(politician,p_modifier,s_modifier):
    lenall = len(p_modifier) + len(s_modifier)
    if random.randint(0,lenall) >= len(p_modifier):
        finalpol = ("%s %s" % (random.choice(politician),random.choice(s_modifier)))
    else:
        finalpol = ("%s %s" % (random.choice(p_modifier),random.choice(politician)))
    return(finalpol)

# Use print instead of text file write (for testing)
# Notice this is commented out
    
#print("Can %s curb fluctuations in the %s%s market?" % (create_politico(politician,p_modifier,s_modifier),random.choice(computer_prefixes),random.choice(currency)))


def happy_gen():
    return("#ITPCore2 is %s. %s %s %s" % (random.choice(handle),random.choice(verb).lower(),random.choice(computer_adj),random.choice(buzz_nouns).lower()))

def ped_gen():
    return("Interact with pedagogy! %s %s! #ITPCore2" % (random.choice(computer_adj),random.choice(hashtags)))

def tech_gen():
    return("Teaching tech! %s %s #ITPCore2" % (random.choice(computer_adj).lower(),random.choice(buzz_nouns).lower()))

    
# def future_gen():
#     return("%s%s: The future of %s %s?" % (random.choice(computer_prefixes).title(),random.choice(biparte_nouns),random.choice(computer_adjectives),random.choice(buzz_gerund)))

#def hack_gen():
#    print("%sfounders hack %s with a simple %s) % ())

# This function randonly picks one of the above templates
# and and rcalls it to create a sentence
def generate_sentence():
    rolldice = random.randint(0,2)
    if rolldice == 0:
        return happy_gen()
    if rolldice == 1:
        return ped_gen()
    if rolldice == 2:
        return tech_gen()

        
#print(generate_sentence())

tfile = open("tweets.txt", 'w')

# Create variable for the site name and a random buzzword hashtag
site = "https://2016core2.commons.gc.cuny.edu/"
hashtag1 = " #" + random.choice(computer_prefixes) + random.choice(biparte_nouns)


sen1 = generate_sentence() + " " + site + hashtag1
print(sen1)
#print(len(sen1))

# Wites 100 tweets to tweets.py
# If there's room, also adds two more hashtags to the tweet
# The /n creates a new line. 
for numtweets in range(0,1000):
    hashtag1 = " #" + random.choice(computer_prefixes) + random.choice(biparte_nouns)
    sen1 = (generate_sentence() + " " + site + hashtag1)
    for limiting1 in range(0,2):
        hashtag2 = random.choice(hashtags)
        if len(sen1) + len(hashtag2) > 138:
            break
        else:
            sen1 = sen1 + " " + hashtag2
    tfile.write(sen1)
    tfile.write("\n")

tfile.close()

# Can sparkstrea survive chaosmonkey?
