import unittest
from unittest.mock import patch
from io import StringIO
import cards # Assuming that the above functions are saved in a file named 'cards.py'


class TestPrintCard(unittest.TestCase):
    def test_print_card(self):
        """Tests the print_card function by checking the output against expected ASCII art of the card."""
        expected_output = [
            "┌─────────┐",
            "│ A       │",
            "│         │",
            "│    ♠    │",
            "│         │",
            "│       A │",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            cards.print_card("A", "♠")
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output))

        # Test with a two-digit number, which is a special case in the original function
        expected_output_10 = [
            "┌─────────┐",
            "│10       │",
            "│         │",
            "│    ♥    │",
            "│         │",
            "│       10│",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            cards.print_card("10", "♥")
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_10))

        # Test with a "red" Joker card, which is a special case in the original function
        expected_output_rjk = [
            "┌─────────┐",
            "│JK       │",
            "│         │",
            "│    ☆    │",
            "│         │",
            "│       JK│",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            cards.print_card("JK", "☆")
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_rjk))

        
        # Test with a "black" Joker card, which is a special case in the original function
        expected_output_bjk = [
            "┌─────────┐",
            "│JK       │",
            "│         │",
            "│    ★    │",
            "│         │",
            "│       JK│",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            cards.print_card("JK", "★")
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_bjk))


        # Test with a face down card, which is a special case of the original function
        expected_output_fd = [
            "┌─────────┐",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            cards.print_card("4", "♣", False)
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_fd))


        # Test for the get_card() function
        expected_output_get_card = [        
            "┌─────────┐",
            "│ 2       │",
            "│         │",
            "│    ♥    │",
            "│         │",
            "│       2 │",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(cards.get_card("2", "♥"))
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_get_card))


        # Test with a face down card, which is a special case of the get_card() function
        expected_output_gcfd = [
            "┌─────────┐",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "│ ░░░░░░░ │",
            "└─────────┘",
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(cards.get_card("4", "♣", False))
            self.assertEqual(fake_out.getvalue().strip(), "\n".join(expected_output_gcfd))


if __name__ == "__main__":
    unittest.main()
