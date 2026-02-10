import pytest
from pages.notes_page import NotesPage
import random
import string

@pytest.mark.smoke_logged_in
def test_notes_crud_flow(logged_in_page):
     page = logged_in_page
     notes = NotesPage(page)

     # Create note
     title = "Test Note " + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
     description = "This is a test note " + ''.join(random.choices(string.ascii_letters + string.digits, k=10))

     notes.create_note_as_home_category(title, description)

     # Update note
     new_title = "Updated Note " + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
     new_description = "This is an updated test note " + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
     notes.update_home_note(old_title = title, new_title = new_title, new_description = new_description)

     # re-verify note exists with updated title
     assert notes.note_exists(new_title), "Updated note not found in the list"
     
     # Delete note
     notes.delete_home_note(new_title)
     
