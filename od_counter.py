# import statements should generally be the very first line in a module
import re

# select a keyword (user input)
print("Welcome to the overdose counter.")
keyword = input("Which number would you like to search for? Please enter one digit, 1-7.")

# while the keyword isn't a single word
while len(keyword.split()) > 1:
	keyword = input("Please enter one digit, 1-7. For example, '3'.")

# create a dictionary of song names to file names
alcohol_files = {"Alcohol": "data/Alcohol.txt",
}

cocaine_files = {"Cocaine": "data/Cocaine.txt",
}

alphrazolam_files = { "Alphrazolam": "data/Alphrazolam.txt",
}

heroin_files = {"Heroin": "data/Heroin.txt",
}

fentanyl_files = {"Fentanyl": "data/Fentanyl.txt",
}

# make the songs dictionary, using the filenames dictionary
alcohol = {}
for alcohol_file in alcohol_files:
	fv = open(alcohol_files[alcohol_file])
	alcohol[alcohol_file] = "".join(fv.readlines()).lower()
	fv.close()

alphrazolam = {}
for alphrazolam_file in alphrazolam_files:
	fv = open(alphrazolam_files[alphrazolam_file])
	alphrazolam[alphrazolam_file] = "".join(fv.readlines()).lower()
	fv.close()

cocaine = {}
for cocaine_file in cocaine_files:
	fv = open(cocaine_files[cocaine_file])
	cocaine[cocaine_file] = "".join(fv.readlines()).lower()
	fv.close()

heroin = {}
for heroin_file in heroin_files:
	fv = open(heroin_files[heroin_file])
	heroin[heroin_file] = "".join(fv.readlines()).lower()
	fv.close()

fentanyl = {}
for fentanyl_file in fentanyl_files:
	fv = open(fentanyl_files[fentanyl_file])
	fentanyl[fentanyl_file] = "".join(fv.readlines()).lower()
	fv.close()

# create a drug
drug_name1 = "alcohol"
drug1_ods = ""
for alcohol_ods in alcohol:
	drug1_ods += alcohol[alcohol_ods]

alcohol_total= "84"

drug_name2 = "alphrazolam"
drug2_ods = ""
for alphrazolam_ods in alphrazolam:
	drug2_ods += alphrazolam[alphrazolam_ods]

alphrazolam_total="68"

drug_name3 = "cocaine"
drug3_ods = ""
for cocaine_ods in cocaine:
	drug3_ods += cocaine[cocaine_ods]

cocaine_total="145"

drug_name4 = "heroin"
drug4_ods = ""
for heroin_ods in heroin:
	drug4_ods += heroin[heroin_ods]

heroin_total="206"

drug_name5 = "fentanyl"
drug5_ods = ""
for fentanyl_ods in fentanyl:
	drug5_ods += fentanyl[fentanyl_ods]

fentanyl_total="235"

# count and print for drugs!
print("")
print("Within Allegheny County in 2016, there were %s drugs (including the main drug) combined in" % (keyword))

alcohol_word_count = re.sub("[^\w]", " ", drug1_ods).split().count(keyword.lower())
print("%d out of %s total %s overdose%s." % (alcohol_word_count, alcohol_total, drug_name1, "" if (alcohol_word_count == 1) else "s"))

alphrazolam_word_count = re.sub("[^\w]", " ", drug2_ods).split().count(keyword.lower())
print("%d out of %s total %s overdose%s." % (alphrazolam_word_count, alphrazolam_total, drug_name2, "" if (alphrazolam_word_count == 1) else "s"))

cocaine_word_count = re.sub("[^\w]", " ", drug3_ods).split().count(keyword.lower())
print("%d out of %s total %s overdose%s." % (cocaine_word_count, cocaine_total, drug_name3, "" if (cocaine_word_count == 1) else "s"))

heroin_word_count = re.sub("[^\w]", " ", drug4_ods).split().count(keyword.lower())
print("%d out of %s total %s overdose%s." % (heroin_word_count, heroin_total, drug_name4, "" if (heroin_word_count == 1) else "s"))

fentanyl_word_count = re.sub("[^\w]", " ", drug5_ods).split().count(keyword.lower())
print("%d out of %s total %s overdose%s." % (fentanyl_word_count, fentanyl_total, drug_name5, "" if (fentanyl_word_count == 1) else "s"))
