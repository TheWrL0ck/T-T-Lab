animalQuestions=[
    {
        "question":"1. What type of animal is a seahorse?",
        "options":["Crustacean","Arachnid","Fish"],
        "correct":2
    },
    {
        "question":"2. Which of the following dog breeds is the smallest?",
        "options":["Poodle","Pomeranian","Chihuahua"],
        "correct":2
    },
    {
        "question":"3. What color are zebras?",
        "options":["White with black stripes","Black with white stripes","Both of the above"],
        "correct":1
    },
    {
        "question":"4. What existing bird has the largest wingspan?",
        "options":["Albatross","Swan","Condor"],
        "correct":0
    },
    {
        "question":"5. What is the biggest animal that has ever lived?",
        "options":["Blue whale","African elephant","Apatosaurus (aka Brontosaurus)"],
        "correct":0
    },
    {
        "question":"6. Fill in the blank: Out of these pets, there are the most pet ___ in the U.S.",
        "options":["Birds","Cats","Dogs"],
        "correct":1
    },
    {
        "question":"7. Which of these animals lives the longest?",
        "options":["Ocean quahog (clam)","Red sea urchin","Galapagos tortoise"],
        "correct":0
    },
    {
        "question":"8. What are female elephants called?",
        "options":[" Mares","Sows","Cows"],
        "correct":2
    },
    {
        "question":"9. Which of the following animals sleeps standing up?",
        "options":["Gorillas","Flamingos","Hedgehogs"],
        "correct":1
    },
    {
        "question":"10. What is the fastest water animal?",
        "options":["Porpoise","Sailfish","Flying fish"],
        "correct":1
    }
]

techQuestions=[
    {
        "question":"What is part of a database that holds only one type of information?",
        "options":["1850s","1880s","1930s"],
        "correct":1
    },
    {
        "question":"What is part of a database that holds only one type of information",
        "options":["Report","Field","Record"],
        "correct":1
    },
    {
        "question":"'OS' computer abbreviation usually means ?",
        "options":["Order of Significance","Open Software","Operating System"],
        "correct":2
    },
    {
        "question":"In which decade with the first transatlantic radio broadcast occur?",
        "options":["1850","1860","1900"],
        "correct":2
    },
    {
        "question":"'.MOV' extension refers usually to what kind of file?",
        "options":["Image File","Animation/movie file","Audio file"],
        "correct":1
    },
    {
        "question":"In which decade was the SPICE simulator introduced?",
        "options":["1950","1960","1970"],
        "correct":2
    },
    {
        "question":"Most modern TV's draw power even if turned off. The circuit the power is used in does what function?",
        "options":["Sound","Remote Control","Color Balance"],
        "correct":1
    },
    {
        "question":"Which is a type of Electrically-Erasable Programmable Read-Only Memory?",
        "options":["Flash","Flange","Fury"],
        "correct":0
    },
    {
        "question":"The purpose of choke in tube light is ?",
        "options":["To dcrease the current","To increase the current","To increase the voltage"],
        "correct":2
    },
    {
        "question":"'.MPG' extension refers usually to what kind of file?",
        "options":["WordPerfect Doxument file","MS Officce documment","Movie file"],
        "correct":2
    }
]

plantQuestions = [
    {
        "question":"1.  Which part of plant is responsible for making food?",
        "options":["Leaf","Root","Trunk"],
        "correct":0
    },
    {
       "question":"2.   What is the green substance on leaves called?",
       "options":["Chlorophyll","Seed","Watermelon"],
       "correct":0
    },
    {
        "question":"3.  Which part of the plant is responsible for absorbing water from the soil?",
        "options":["Root","Seed","Leaf"],
        "correct":0
    },
    {
        "question":"4.  Which of thses is an edible underground stem?",
        "options":["Potato","Sweet Potato","Groundnut"],
        "correct":0
    },
    {
        "question":"5. Veins of the leaves are useful for",
        "options":["Transport of water and minerals","Transport of organic nutrients","All of the above"],
        "correct":2
    },
    {
        "question":"6. One seeded winged fruit is",
        "options":["Nut","Samara","Cypsela"],
        "correct":1
    },
    {
        "question":"7. The plant that traps and feeds on insects is ",
        "options":["Rose","Pitcher Plant","Timber"],
        "correct":1
    },
    {
        "question":"8. A spore producing plant is",
        "options":["rose","bread mould","ginger"],
        "correct":1
    },
    {
        "question":"9. In plants, water is transported through",
        "options":["Phloem","Xylem","Stomata"],
        "correct":1
    },
    {
        "question":"10. Amrabel is an example of",
        "options":["Autotroph","Parasite","Host"],
        "correct":0
    }
]

gkQuestions = [
    {"question":"1.  Epsom(England) is the place associated with:",
     "options":["Snooker","Horse racing","Polo"],
     "correct":1
    },
    {"question":"2.  Fastest Shorthand Writer was:",
     "options":["Dr. G. D. Bist","J.R.D. Tata","J.M. Tagore"],
     "correct":0
    },
    {"question":"3.  Golf player Vijay Singh belongs to which country?",
     "options":["USA","Fiji","India"],
     "correct":1
    },
    {"question":"4.  “One People, One State, One leader” was the policy of:",
     "options":["Mussolin","Lenin","Hitler"],
     "correct":2
    },
    {"question":"5.  DRDL stands for:",
     "options":["Defence Research and Development Laboratory","Department of Research and Development Laboratory","Differential Research and Documentation Laboratory"],
     "correct":0
    },
    {"question":"6.  Exposure to sunlight helps a person improve his health because:",
     "options":["the infrared light kills bacteria in the body","resistance power increases","the ultraviolet rays convert skin oil into Vitamin D"],
     "correct":2
    },
    {"question":"7.  The biggest public sector undertaking in the country is:",
     "options":["Roadways","Railways","Airways"],
     "correct":1
    },
    {"question":"8.  At which particular place on earth are days and nights of equal length always?",
     "options":["Equator","No where","Poles"],
     "correct":0
    },
    {"question":"9.  G-15 is an economic grouping of:",
     "options":["First World Nations","Second World Nations","Third World Nations"],
     "correct":2
    },
    {"question":"10.  An astronaut in outer space will observe sky as:",
     "options":["Blue","Purple","Black"],
     "correct":2
    }
]


def main():
    questions = None
    ch = int(input("Please select your topic\n1-GK\n2-Tech\n3-Animals\n4-Plants\n"))
    if ch == 1:
        questions = gkQuestions
    elif ch == 2:
        questions = techQuestions
    elif ch == 3:
        questions = animalQuestions
    elif ch == 4:
        questions = plantQuestions
    else:
        print("Incorrect option")
        return
    streak = 0
    wrong = 0
    points = 0
    for question in questions:
        print(question["question"])
        for i,k in enumerate(question["options"]):
            print(f"\t{i+1}.{k}")

        ch = input()
        if int(ch)-1 == question["correct"]:
            print("Correct!!\n\n")
            streak += 1
            points+=1
            if streak == 5:
                points+=50
                print("You hit a streak!!! +50")
        else:
            print("Incorrect Option :(")
            wrong+=1
            if wrong == 3:
                print("Better luck next time!")
                return
            
    print(f"Your score is {points}")
    
    
main()