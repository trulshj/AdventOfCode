using System.Globalization;
using System.Text.RegularExpressions;

namespace AdventOfCode.Puzzles;

public partial class Day04 : BaseDay
{
    private List<Card> Cards { get; set; } = new();

    public override string SolvePart1Async()
    {
        Cards = InputFileAsLines
            .Select(x => CardRegex().Match(x).Groups)
            .Select(x => new Card(int.Parse(x[1].Value), x[2].Captures.Select(c => int.Parse(c.Value)).ToArray(),
                x[3].Captures.Select(c => int.Parse(c.Value)).ToArray())).ToList();

        return Cards.Select(x => x.ScratchedNumbers.Count(s => x.WinningNumber.Contains(s))).Where(x => x > 0)
            .Select(c => Math.Pow(2, c - 1)).Sum().ToString(CultureInfo.InvariantCulture);
    }

    public override string SolvePart2Async()
    {
        var copies = Cards.ToDictionary(card => card.CardId, _ => 1);

        var wins = Cards.Select(card =>
                (cardId: card.CardId, card.ScratchedNumbers.Count(s => card.WinningNumber.Contains(s))))
            .Where(x => x.Item2 > 0).ToArray();

        foreach (var (cardId, count) in wins)
        {
            var cardCount = copies[cardId];
            for (var i = 1; i <= count; i++) copies[cardId + i] += cardCount;
        }

        return copies.Select(x => x.Value).Sum().ToString();
    }

    [GeneratedRegex(@"Card +(\d+): +(\d+ +)+\|( *\d+)+")]
    private static partial Regex CardRegex();

    private sealed record Card(int CardId, int[] WinningNumber, int[] ScratchedNumbers);
}