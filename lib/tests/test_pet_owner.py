import pytest
from lib.owner import Owner
from lib.pet import Pet

def test_pet_creation():
    pet = Pet(name="Buddy", pet_type="dog")
    assert pet.name == "Buddy"
    assert pet.pet_type == "dog"

def test_invalid_pet_type():
    with pytest.raises(Exception):
        Pet(name="Unknown", pet_type="unicorn")

def test_owner_and_pets():
    owner = Owner(name="Alice")
    pet1 = Pet(name="Buddy", pet_type="dog")
    pet2 = Pet(name="Whiskers", pet_type="cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    assert owner.pets() == [pet1, pet2]
    assert owner.get_sorted_pets() == [pet2, pet1]
