import random

FIRST_NAMES = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

SKILLS = {
    "Kotlin", "Java", "Python", "JavaScript", "TypeScript",
    "React", "Angular", "Spring Boot", "AWS", "Docker",
    "Kubernetes", "SQL", "MongoDB", "Git", "CI/CD",
    "Machine Learning", "DevOps", "Node.js", "REST API", "GraphQL"
}

EMPLOYEES = list({emp["name"]: emp for emp in [
    {
        "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
        # Randomly assign 2 to 5 skills to each employee
        "skills": random.sample(list(SKILLS), random.randint(2, 5))
    }
    for i in range(30)
]}.values())


# also can be written as a list comprehension with a set to ensure unique names
# Generate 100 unique names up front
'''
names = random.sample([f"{first} {last}" for first in FIRST_NAMES for last in LAST_NAMES], 100)

# Build the employee list directly
EMPLOYEES = [
    {
        "name": name,
        "skills": random.sample(list(SKILLS), random.randint(2, 5))
    }
    for name in names
]

'''