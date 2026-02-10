
import time


class NotesPage:
    def __init__(self, page):
        self.page = page
        self.new_note_button = page.locator("//button[text()='+ Add Note']")
        self.title_input = page.locator("//input[@data-testid='note-title']")
        self.description_input = page.locator("//textarea[@data-testid='note-description']")
        self.complted_checkbox = page.locator("//input[@data-testid='note-completed']")
        self.category_dropdown = page.locator("//select[@data-testid='note-category']")
        self.submit_button = page.locator("//button[@data-testid='note-submit']")
        self.note_titles = page.locator("//div[@data-testid='note-card-title']")
        self.edit_button = page.locator("//button[@data-testid='note-edit']")
        self.delete_button = page.locator("//button[@data-testid='note-delete']")
        self.note_delete_confirmation = page.locator("//button[@data-testid='note-delete-confirm']")
        self.note_view_button = page.locator("//a[@data-testid='note-view']")
        
        # navigate category
        self.all_category_button = page.locator("//button[@data-testid='category-all']")
        self.home_category_button = page.locator("//button[@data-testid='category-home']")
        self.work_category_button = page.locator("//button[@data-testid='category-work']")
        self.study_category_button = page.locator("//button[@data-testid='category-personal']")

    def create_note_as_home_category(self, title, description):
        self.home_category_button.click()
        self.new_note_button.click()
        self.title_input.fill(title)
        self.description_input.fill(description)
        self.category_dropdown.select_option("Home")
        self.submit_button.click()
        
        time.sleep(3)  # Wait for the note to be created and appear in the list
        assert self.page.locator(f"//div[@data-testid='note-card-title' and text()='{title}']").is_visible(), "Note creation failed"
        return f"Note created successfully as: {title}"
        

    def update_home_note(self, old_title, new_title, new_description):
        note_update_button = self.page.locator(f"//div[text()='{old_title}']/parent::div//button[@data-testid='note-edit']")
        note_update_button.click()
        self.title_input.fill(new_title)
        self.description_input.fill(new_description)
        self.submit_button.click()
        
        time.sleep(5)  # Wait for the note to be updated and appear in the list
        assert self.page.locator(f"//div[@data-testid='note-card-title' and text()='{new_title}']").is_visible(), "Note update failed"
        return f"Note updated successfully to: {new_title}"

    def delete_home_note(self, new_title):
        note_delete_button = self.page.locator(f"//div[text()='{new_title}']/parent::div//button[@data-testid='note-delete']")
        note_delete_button.click()
        self.note_delete_confirmation.click()
        time.sleep(3)  # Wait for the note to be deleted and removed from the list
        if note_delete_button.is_visible():
            return f"Failed to delete note: {new_title}"
        else:
            return f"Note deleted successfully: {new_title}"

    def note_exists(self, title):
        time.sleep(3)  # Wait for the note to be created and appear in the list
        return self.page.locator(f"//div[@data-testid='note-card-title' and text()='{title}']").is_visible()
