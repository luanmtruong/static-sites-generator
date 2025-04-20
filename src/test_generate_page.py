import os
import shutil
import tempfile
import unittest
from generate_page import generate_pages_recursive


class TestGeneratePagesRecursive(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.temp_dir, "content")
        self.public_dir = os.path.join(self.temp_dir, "public")
        self.template_path = os.path.join(self.temp_dir, "template.html")

        os.makedirs(self.content_dir)
        os.makedirs(os.path.join(self.content_dir, "blog"))

        # Create template
        with open(self.template_path, "w") as f:
            f.write("<!doctype html><html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>")

        # Create markdown files
        with open(os.path.join(self.content_dir, "index.md"), "w") as f:
            f.write("# Home\n\nWelcome")
        with open(os.path.join(self.content_dir, "blog", "post.md"), "w") as f:
            f.write("# Post\n\nContent")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_generate_pages_recursive(self):
        generate_pages_recursive(self.content_dir, self.template_path, self.public_dir)

        # Check generated files
        index_html = os.path.join(self.public_dir, "index.html")
        post_html = os.path.join(self.public_dir, "blog", "post.html")

        self.assertTrue(os.path.exists(index_html))
        self.assertTrue(os.path.exists(post_html))

        with open(index_html, "r") as f:
            content = f.read()
            self.assertIn("<title>Home</title>", content)
            self.assertIn("<h1>Home</h1>", content)

        with open(post_html, "r") as f:
            content = f.read()
            self.assertIn("<title>Post</title>", content)
            self.assertIn("<h1>Post</h1>", content)


if __name__ == "__main__":
    unittest.main()
