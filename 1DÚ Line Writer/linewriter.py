def writeTextToFile (vstup):
    STATICKÝ_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    jméno_souboru = "vystup.txt"
    soubor = open(jméno_souboru, 'w')
    soubor.write(STATICKÝ_TEXT + str(vstup))
    soubor.close()
    return jméno_souboru

print(writeTextToFile("Lorem ipsum dolor sit amet"))