print("Name: Yinghao Meng")
print("Status: First-year Ph.D. student")
print("Location: The University of Tennessee, Knoxville")

hobbies = ["hiking", "video games", "cycling"]

print("My hobbies are:", ", ".join(hobbies))

print("\n--- Interactive Q&A ---")
print("You can ask: 'Where are you from?' or 'What is your research focus?'")
print("Type 'exit' or 'No' to quit.\n")

while True:
    question = input("Your question: ")

    if question.strip().lower() in ["exit", "no"]:
        print("Exiting Q&A session. Goodbye!")
        break
    elif question.strip().lower() == "where are you from?":
        print("Answer: Mainland China")
    elif question.strip().lower() == "what is your research focus?":
        print("Answer: Traffic safety estimation")
    else:
        print("Sorry, I don't have an answer for that question.")