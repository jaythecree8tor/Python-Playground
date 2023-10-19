class_members = {
    "pelumi": {
        "bio": "Pelumi is a computer science major who loves programming and solving complex problems.",
        "introduction": "Hi, I'm Pelumi! I'm passionate about coding and always up for a new challenge.",
        "height": "5'7\"",
        "favorite_food": "Pizza",
        "favorite_color": "Blue",
        "complexion": "Fair",
        "ethnicity": "Caucasian",
        "favorite_coding_stack": "Python and JavaScript",
    },
    "Bob": {
        "bio": "Bob is an avid sports enthusiast and enjoys playing basketball and soccer in his free time.",
        "introduction": "Hey there! I'm Bob, and I'm all about sports and staying active.",
        "height": "6'0\"",
        "favorite_food": "Tacos",
        "favorite_color": "Red",
        "complexion": "Medium",
        "ethnicity": "African American",
        "favorite_coding_stack": "Java and C++",
    },
    "Charlie": {
        "bio": "Charlie is a bookworm who can often be found with their nose in a novel.",
        "introduction": "Hello, I'm Charlie, and I'm a dedicated book lover. Let's talk about our favorite reads!",
        "height": "5'5\"",
        "favorite_food": "Sushi",
        "favorite_color": "Green",
        "complexion": "Olive",
        "ethnicity": "Asian",
        "favorite_coding_stack": "Ruby and Ruby on Rails",
    },
    "David": {
        "bio": "David is a music lover and plays the guitar in a local band on weekends.",
        "introduction": "Hey, I'm David. I'm passionate about music, and I play the guitar in a band. Rock on!",
        "height": "6'2\"",
        "favorite_food": "Burgers",
        "favorite_color": "Black",
        "complexion": "Dark",
        "ethnicity": "Hispanic",
        "favorite_coding_stack": "Swift and iOS development",
    },
}

# Get a person's name from user input
person_name = input("Enter a person's name: ")

# Check if the entered name exists in the dictionary
if person_name in class_members:
    person_info = class_members[person_name]
    print(f"Name: {person_name}")
    print(f"Bio: {person_info['bio']}")
    # print(f"Introduction: {person_info['introduction']}")
    # print(f"Height: {person_info['height']}")
    # print(f"Favorite Food: {person_info['favorite_food']}")
    # print(f"Favorite Color: {person_info['favorite_color']}")
    # print(f"Complexion: {person_info['complexion']}")
    # print(f"Ethnicity: {person_info['ethnicity']}")
    # print(f"Favorite Coding Stack: {person_info['favorite_coding_stack']}")
else:
    print(f"No information found for {person_name}.")