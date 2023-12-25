using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day17 : BaseDay
{
    private Matrix<int> Grid { get; set; } = null!;

    protected override void ParseInput()
    {
        Grid = new Matrix<int>(InputFileAsLines.Select(x => x.Select(c => int.Parse(c.ToString())).ToList()).ToList());
    }

    protected override object SolvePartOne()
    {
        var visited = new HashSet<(Coordinate position, Coordinate delta, int steps)>();
        var queue = new PriorityQueue<(Coordinate position, Coordinate delta, int steps), int>();

        queue.Enqueue((Coordinate.Zero, Coordinate.Zero, 0), 0);

        while (queue.TryDequeue(out var currentNode, out var currentHeat))
        {
            if (currentNode.position == Grid.BottomRight) return currentHeat;

            if (!visited.Add(currentNode)) continue;

            // try moving forward
            // we can only move forward if we have moved less than 3 steps and we are not standing still
            if (currentNode.steps < 3 && !currentNode.delta.IsZero())
            {
                var newPosition = currentNode.position + currentNode.delta;
                if (Grid.WithinBounds(newPosition))
                    queue.Enqueue((newPosition, currentNode.delta, currentNode.steps + 1),
                        currentHeat + Grid[newPosition]);
            }

            // try turning both left and right
            foreach (var delta in Coordinate.OrthogonalDeltas)
            {
                // we don't want to go back or forward
                if (delta == currentNode.delta || delta == currentNode.delta.Reverse())
                    continue;

                var newPosition = currentNode.position + delta;
                if (Grid.WithinBounds(newPosition))
                    queue.Enqueue((newPosition, delta, 1), currentHeat + Grid[newPosition]);
            }
        }

        throw new InvalidOperationException("No path found");
    }

    protected override object SolvePartTwo()
    {
        var visited = new HashSet<(Coordinate position, Coordinate delta, int steps)>();
        var queue = new PriorityQueue<(Coordinate position, Coordinate delta, int steps), int>();

        queue.Enqueue((Coordinate.Zero, Coordinate.Zero, 0), 0);

        while (queue.TryDequeue(out var currentNode, out var currentHeat))
        {
            if (currentNode.position == Grid.BottomRight && currentNode.steps >= 4) return currentHeat;

            if (!visited.Add(currentNode)) continue;

            // try moving forward
            // we can only move forward if we have moved less than 10 steps and we are not standing still
            if (currentNode.steps < 10 && !currentNode.delta.IsZero())
            {
                var newPosition = currentNode.position + currentNode.delta;
                if (Grid.WithinBounds(newPosition))
                    queue.Enqueue((newPosition, currentNode.delta, currentNode.steps + 1),
                        currentHeat + Grid[newPosition]);
            }

            // try turning both left and right
            // we need to move at least 4 steps before we can turn
            // at the start we also need to pick a direction
            if (currentNode.steps >= 4 || currentNode.delta.IsZero())
                foreach (var delta in Coordinate.OrthogonalDeltas)
                {
                    // we don't want to go back or forward
                    if (delta == currentNode.delta || delta == currentNode.delta.Reverse())
                        continue;

                    var newPosition = currentNode.position + delta;
                    if (Grid.WithinBounds(newPosition))
                        queue.Enqueue((newPosition, delta, 1), currentHeat + Grid[newPosition]);
                }
        }

        throw new InvalidOperationException("No path found");
    }
}