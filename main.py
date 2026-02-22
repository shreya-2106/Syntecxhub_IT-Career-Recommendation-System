from infer import forward_chaining

print("===== IT Career Expert System =====")
print("\nAvailable Domains:")
print("""
math, logic, physics, coding, statistics,
biology, helping, patience, communication,
creativity, design, drawing,
law, debate, confidence,
business, finance, teaching,
analysis
""")

user_input = input("Enter your interests (comma separated): ")  
facts = [x.strip().lower() for x in user_input.split(",")]
final_facts, explanation = forward_chaining(facts)

print("\n--- Inference Steps ---")
for step in explanation:
    print(step)

print("\n--- Final Facts ---")
print(final_facts)
career_keywords = [
    "software_engineer", "doctor", "graphic_designer",
    "lawyer", "entrepreneur", "teacher",
    "data_scientist", "civil_servant", "artist",
    "marketing_manager", "psychologist",
    "cyber_security_specialist", "researcher", "banker"
]

careers = [fact for fact in final_facts if fact in career_keywords]

if careers:
    print("\n✅ Recommended Career(s):")
    for c in careers:
        print("→", c)
else:
    print("\n❌ No strong recommendation found.")