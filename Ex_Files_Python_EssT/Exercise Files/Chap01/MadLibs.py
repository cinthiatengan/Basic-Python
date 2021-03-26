"""" Mad Libs Generator ----------------------------------------- """""

#Loop back to this point once code finishes
loop = 1
while(loop < 10):
#Todas as questões que o programa pergunta ao usuario
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
# Mostra a historia baseada nas entradas do usuario
    print("---------------------------------------------")
    print("Be kind to your ",noun, "- footed")
    print("For a duck may be somebody's ",noun2, ",")
    print("Be kind to your ", p_noun," in ",place)
    print("Where the weather is always ",adjective, ".")
    print()
    print("You may think that is this the ",noun3, ",")
    print("well it is.")
    print("--------------------------------------------")
# Loop para voltar a "loop =1'
    loop = loop+1