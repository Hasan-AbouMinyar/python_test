import asyncio
import csv
from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict

@dataclass(frozen=True, order=True)
class Person:
    """
    An immutable dataclass representing a person.
    'frozen=True' makes instances of this class unchangeable after creation.
    'order=True' automatically implements comparison methods (__lt__, __gt__, etc.).
    """
    name: str
    birth_year: int
    # 'field' is used to compute a value after the object is created.
    age: int = field(init=False)

    def __post_init__(self):
        """
        This method is called by the dataclass after the object is initialized.
        We use it here to calculate the age.
        """
        current_year = date.today().year
        # Since the class is frozen, we can't assign to self.age directly.
        # We must use a special (but standard) way to set the attribute.
        object.__setattr__(self, 'age', current_year - self.birth_year)

    @property
    def age_category(self) -> str:
        """Determines the age category based on the person's age."""
        if self.age >= 65:
            return "Senior Citizen"
        elif self.age >= 18:
            return "Adult"
        elif self.age >= 13:
            return "Teenager"
        elif self.age >= 3:
            return "Child"
        else:
            return "Baby"

    def years_until_100(self) -> int:
        """Calculates the years remaining until the person turns 100."""
        return 100 - self.age

    def to_dict(self) -> Dict[str, any]:
        """Converts the person object to a dictionary for CSV writing."""
        return {
            "Name": self.name,
            "Birth Year": self.birth_year,
            "Age": self.age,
            "Category": self.age_category,
            "Years to 100": self.years_until_100()
        }

async def process_person_data(name: str, birth_year: int) -> Person:
    """
    An asynchronous function to simulate fetching and processing data for a person.
    `async` defines the function as a coroutine.
    `await` pauses the function to wait for a (simulated) slow operation.
    """
    print(f"⏳ Fetching data for {name}...")
    # Simulate a network request or slow database query (0.5 to 1.5 seconds)
    await asyncio.sleep(0.5 + (hash(name) % 10) / 10.0)
    print(f"✅ Data received for {name}.")
    return Person(name=name, birth_year=birth_year)

def export_to_csv(people: List[Person], filename: str = "people_report.csv"):
    """Exports a list of Person objects to a CSV file."""
    if not people:
        return
    
    print(f"\n📄 Exporting report to '{filename}'...")
    # Get the headers from the first person's dictionary keys
    headers = people[0].to_dict().keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=headers)
        dict_writer.writeheader()
        dict_writer.writerows([p.to_dict() for p in people])
    print("✨ Export complete!")


async def main():
    """The main asynchronous entry point for the script."""
    people_data_source = {
        "Hasan": 2003,
        "Sarah": 2010,
        "Ali": 1960,
        "Mona": 2023,
        "Khalid": 1988,
        "Fatima": 1955,
        "Omar": 2018
    }

    # Create a list of asynchronous tasks
    tasks = [process_person_data(name, year) for name, year in people_data_source.items()]
    
    # Run all tasks concurrently and wait for them all to complete
    print("🚀 Starting concurrent data processing...")
    processed_people: List[Person] = await asyncio.gather(*tasks)
    
    # Sort the final list by age
    processed_people.sort()

    print("\n--- Processing Results ---")
    for person in processed_people:
        print(f"👤 {person.name} (Age: {person.age}) is a(n) {person.age_category}.")
    
    # Export the final data to a file
    export_to_csv(processed_people)


if __name__ == "__main__":
    # This is how you run the main asynchronous function
    asyncio.run(main())
