"""
Script or sorting packages in Thoughtful’s warehouse. Complete with unit tests

Rules:
- A package is BULKY if its volume hits 1,000,000 cm³ or any one side is 150 cm or more.
- A package is HEAVY if it tips the scale at 20 kg or more.

Stacks:
  STANDARD  → neither bulky nor heavy
  SPECIAL   → either bulky or heavy (but not both)
  REJECTED  → both bulky and heavy
"""

def is_bulky(w, h, l):
    # Bulky if any side is huge, or if the whole thing’s volume breaks a million.
    return (
        w >= 150 or h >= 150 or l >= 150 or
        w * h * l >= 1_000_000
    )


def is_heavy(mass):
    # Heavy just means 20 kg or more.
    return mass >= 20


def sort(width, height, length, mass):
    """Tell the robot which stack this box belongs on."""
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"


# Quick self‑test when you run the file directly.
if __name__ == "__main__":
    import unittest

    class SortTests(unittest.TestCase):
        def test_standard(self):
            self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

        def test_special_bulky_only(self):
            self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")

        def test_special_heavy_only(self):
            self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

        def test_rejected_bulky_and_heavy(self):
            self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

        def test_volume_bulkiness_and_light(self):
            self.assertEqual(sort(100, 100, 100, 0.1), "SPECIAL")

        def test_borderline_volume_just_under(self):
            self.assertEqual(sort(99.999, 100, 100, 19.999), "STANDARD")

    unittest.main(verbosity=2)
