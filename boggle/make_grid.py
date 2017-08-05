def test_can_create_an_empty_grid(self):
    grid = boggle.make_grid(0, 0)
    self.assertEqual(len(grid), 0)

    def make_grid(height, width):
        return {(row, col): ' ' for row in range(height)
                for col in range(width)}

def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
                for row in range(height)
                for col in range(width)}