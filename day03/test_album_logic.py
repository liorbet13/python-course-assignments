"""
Unit tests for album_logic module
Tests the business logic for Taylor Swift Album Finder
"""

import unittest
import album_logic


class TestAlbumLogic(unittest.TestCase):
    """Test cases for album logic functions"""
    
    def test_valid_month_returns_correct_album(self):
        """Test that valid months return the correct album"""
        self.assertEqual(album_logic.get_album_for_month("January"), "Taylor Swift")
        self.assertEqual(album_logic.get_album_for_month("August"), "Folklore")
        self.assertEqual(album_logic.get_album_for_month("December"), "The Life of a Showgirl")
        self.assertEqual(album_logic.get_album_for_month("May"), "1989")
    
    def test_case_insensitive_input(self):
        """Test that month names work regardless of case"""
        self.assertEqual(album_logic.get_album_for_month("january"), "Taylor Swift")
        self.assertEqual(album_logic.get_album_for_month("AUGUST"), "Folklore")
        self.assertEqual(album_logic.get_album_for_month("DeCeMbEr"), "The Life of a Showgirl")
        self.assertEqual(album_logic.get_album_for_month("mAy"), "1989")
    
    def test_invalid_month_returns_none(self):
        """Test that invalid months return None"""
        self.assertIsNone(album_logic.get_album_for_month("NotAMonth"))
        self.assertIsNone(album_logic.get_album_for_month(""))
        self.assertIsNone(album_logic.get_album_for_month("13"))
        self.assertIsNone(album_logic.get_album_for_month("InvalidMonth"))
    
    def test_whitespace_handling(self):
        """Test that leading/trailing whitespace is handled"""
        self.assertEqual(album_logic.get_album_for_month("  January  "), "Taylor Swift")
        self.assertEqual(album_logic.get_album_for_month("\tMay\n"), "1989")
        self.assertEqual(album_logic.get_album_for_month("  march  "), "Speak Now")
    
    def test_all_months_have_albums(self):
        """Test that all 12 months have corresponding albums"""
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        for month in months:
            album = album_logic.get_album_for_month(month)
            self.assertIsNotNone(album, f"{month} should have an album")
            self.assertIsInstance(album, str, f"{month}'s album should be a string")
    
    def test_image_filename_for_valid_album(self):
        """Test that valid albums return correct image filenames"""
        self.assertEqual(album_logic.get_image_filename_for_album("Folklore"), "folklore.jpg")
        self.assertEqual(album_logic.get_image_filename_for_album("1989"), "1989.jpg")
        self.assertEqual(album_logic.get_image_filename_for_album("Taylor Swift"), "taylor_swift.jpg")
        self.assertEqual(album_logic.get_image_filename_for_album("The Life of a Showgirl"), "showgirl.jpg")
    
    def test_image_filename_for_invalid_album(self):
        """Test that invalid albums return None"""
        self.assertIsNone(album_logic.get_image_filename_for_album("Fake Album"))
        self.assertIsNone(album_logic.get_image_filename_for_album(""))
        self.assertIsNone(album_logic.get_image_filename_for_album("Not An Album"))
    
    def test_is_valid_month_true(self):
        """Test that valid months are recognized"""
        self.assertTrue(album_logic.is_valid_month("January"))
        self.assertTrue(album_logic.is_valid_month("december"))
        self.assertTrue(album_logic.is_valid_month("MARCH"))
        self.assertTrue(album_logic.is_valid_month("  April  "))
    
    def test_is_valid_month_false(self):
        """Test that invalid months are rejected"""
        self.assertFalse(album_logic.is_valid_month("NotAMonth"))
        self.assertFalse(album_logic.is_valid_month(""))
        self.assertFalse(album_logic.is_valid_month("13"))
        self.assertFalse(album_logic.is_valid_month("Jan"))
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Empty string
        self.assertIsNone(album_logic.get_album_for_month(""))
        
        # Numbers
        self.assertIsNone(album_logic.get_album_for_month("1"))
        
        # Special characters
        self.assertIsNone(album_logic.get_album_for_month("@#$%"))
        
        # Partial month names
        self.assertIsNone(album_logic.get_album_for_month("Jan"))
        
        # Misspellings
        self.assertIsNone(album_logic.get_album_for_month("Januray"))
    
    def test_data_integrity(self):
        """Ensure all albums have corresponding images"""
        for album in album_logic.MONTH_TO_ALBUM.values():
            self.assertIn(album, album_logic.ALBUM_TO_IMAGE, 
                         f"Album '{album}' should have an image")
            image_file = album_logic.get_image_filename_for_album(album)
            self.assertTrue(image_file.endswith('.jpg'), 
                          f"Image for '{album}' should be a .jpg file")
    
    def test_integration_scenario(self):
        """Test a complete workflow like the GUI would use"""
        # Simulate user typing "august" in lowercase
        album = album_logic.get_album_for_month("august")
        image = album_logic.get_image_filename_for_album(album)
        
        self.assertEqual(album, "Folklore")
        self.assertEqual(image, "folklore.jpg")
        
        # Simulate dropdown selection
        album2 = album_logic.get_album_for_month("November")
        image2 = album_logic.get_image_filename_for_album(album2)
        
        self.assertEqual(album2, "The Tortured Poets Department")
        self.assertEqual(image2, "ttpd.jpg")


class TestMonthToAlbumMapping(unittest.TestCase):
    """Test the complete month-to-album mapping"""
    
    def test_january_to_taylor_swift(self):
        self.assertEqual(album_logic.get_album_for_month("January"), "Taylor Swift")
    
    def test_february_to_fearless(self):
        self.assertEqual(album_logic.get_album_for_month("February"), "Fearless")
    
    def test_march_to_speak_now(self):
        self.assertEqual(album_logic.get_album_for_month("March"), "Speak Now")
    
    def test_april_to_red(self):
        self.assertEqual(album_logic.get_album_for_month("April"), "Red")
    
    def test_may_to_1989(self):
        self.assertEqual(album_logic.get_album_for_month("May"), "1989")
    
    def test_june_to_reputation(self):
        self.assertEqual(album_logic.get_album_for_month("June"), "Reputation")
    
    def test_july_to_lover(self):
        self.assertEqual(album_logic.get_album_for_month("July"), "Lover")
    
    def test_august_to_folklore(self):
        self.assertEqual(album_logic.get_album_for_month("August"), "Folklore")
    
    def test_september_to_evermore(self):
        self.assertEqual(album_logic.get_album_for_month("September"), "Evermore")
    
    def test_october_to_midnights(self):
        self.assertEqual(album_logic.get_album_for_month("October"), "Midnights")
    
    def test_november_to_ttpd(self):
        self.assertEqual(album_logic.get_album_for_month("November"), "The Tortured Poets Department")
    
    def test_december_to_showgirl(self):
        self.assertEqual(album_logic.get_album_for_month("December"), "The Life of a Showgirl")


if __name__ == '__main__':
    unittest.main()
