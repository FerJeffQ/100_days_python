#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PATH_LETTER = "Input/Letters/starting_letter.txt"
PATH_NAMES = "Input/Names/invited_names.txt"

with open(PATH_LETTER, "r") as f:
    letter = f.readlines()
with open(PATH_NAMES, "r") as f:
    names = f.readlines()    

new_document = []
for name in names:
    name = name.strip()
    for line in letter:            
        new_line = line.replace("[name]",name)        
        new_document.append(new_line)
        
    with open(f"Output/ReadyToSend/letter_{name}.txt","w") as f:
        for _ in new_document:            
            f.write(_)
    new_document = []



 