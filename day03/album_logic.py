"""
Business logic for Taylor Swift Album Finder
Handles month-to-album mapping and album-to-image mapping
"""

# Dictionary mapping month names to Taylor Swift albums
MONTH_TO_ALBUM = {
    "January": "Taylor Swift",
    "February": "Fearless",
    "March": "Speak Now",
    "April": "Red",
    "May": "1989",
    "June": "Reputation",
    "July": "Lover",
    "August": "Folklore",
    "September": "Evermore",
    "October": "Midnights",
    "November": "The Tortured Poets Department",
    "December": "The Life of a Showgirl"
}

# Dictionary mapping album names to image filenames
ALBUM_TO_IMAGE = {
    "Taylor Swift": "taylor_swift.jpg",
    "Fearless": "fearless.jpg",
    "Speak Now": "speak_now.jpg",
    "Red": "red.jpg",
    "1989": "1989.jpg",
    "Reputation": "reputation.jpg",
    "Lover": "lover.jpg",
    "Folklore": "folklore.jpg",
    "Evermore": "evermore.jpg",
    "Midnights": "midnights.jpg",
    "The Tortured Poets Department": "ttpd.jpg",
    "The Life of a Showgirl": "showgirl.jpg"
}


def get_album_for_month(month_name):
    """
    Get the Taylor Swift album for a given birth month.
    
    Args:
        month_name (str): Name of the month (e.g., "January", "February")
        
    Returns:
        str or None: Album name if month is valid, None otherwise
    """
    # Normalize the input by capitalizing first letter
    month_name = month_name.strip().capitalize()
    return MONTH_TO_ALBUM.get(month_name)


def get_image_filename_for_album(album_name):
    """
    Get the image filename for a given album.
    
    Args:
        album_name (str): Name of the Taylor Swift album
        
    Returns:
        str or None: Image filename if album exists, None otherwise
    """
    return ALBUM_TO_IMAGE.get(album_name)


def is_valid_month(month_name):
    """
    Check if a month name is valid.
    
    Args:
        month_name (str): Name of the month to validate
        
    Returns:
        bool: True if valid month, False otherwise
    """
    month_name = month_name.strip().capitalize()
    return month_name in MONTH_TO_ALBUM
