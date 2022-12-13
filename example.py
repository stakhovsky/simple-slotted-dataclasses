import dataclasses

import simple_slotted_dataclasses


@simple_slotted_dataclasses.dataclass
class Parent:
    a: int
    b: int


@simple_slotted_dataclasses.dataclass
class Child(Parent):
    c: int = dataclasses.field(default=0)


def main():
    parent = Parent(a=1, b=2)
    child = Child(a=2, b=3)
    print("Is Parent a dataclass?", dataclasses.is_dataclass(Parent))
    print("Is Parent' instance a dataclass?", dataclasses.is_dataclass(parent))
    print("Is Child a dataclass?", dataclasses.is_dataclass(Child))
    print("Is Child' instance a dataclass?", dataclasses.is_dataclass(child))
    print("Is parent an instance of Parent?", isinstance(parent, Parent))
    print("Is child an instance of Child?", isinstance(child, Child))
    print("Is child and instance of Parent?", isinstance(child, Parent))
    print("Does parent have a __dict__?", hasattr(parent, "__dict__"))
    print("Does child have a __dict__?", hasattr(child, "__dict__"))


if __name__ == "__main__":
    main()
