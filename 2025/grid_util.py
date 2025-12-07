import callee


def input_grid():
    path = callee.get_input_path()
    with open(path) as f:
        return Grid([list(x.rstrip()) for x in f.readlines()])


class Grid:
    DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]
    ORTHO_DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, grid: list[list[str | int]]):
        self._grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __getitem__(self, y):
        return self._grid[y]

    def __setitem__(self, y, data):
        self._grid[y] = data

    def __iter__(self):
        yield from self._grid

    def in_bounds(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width

    def filter_cells(self, filter):
        for y, row in enumerate(self._grid):
            for x, cell in enumerate(row):
                if filter(y, x, cell):
                    yield (y, x)

    def neighbour_coords(self, y, x, ortho=False):
        for dy, dx in (self.DELTAS if not ortho else self.ORTHO_DELTAS):
            if self.in_bounds(ny := dy + y, nx := dx + x):
                yield (ny, nx)

    def neighbours(self, y: int, x: int, ortho=False, filter=None):
        for ny, nx in self.neighbour_coords(y, x, ortho):
            cell = self._grid[ny][nx]
            if filter is None or filter(cell):
                yield (ny, nx), cell

    def count_neighbours(self, y: int, x: int, ortho=False, filter=None):
        return sum(1 for _ in self.neighbours(y, x, ortho, filter))

    def copy(self):
        return Grid([row[:] for row in self._grid])

    def bulk_set(self, coordinates, data):
        for y, x in coordinates:
            self._grid[y][x] = data
