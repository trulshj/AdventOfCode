#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

struct Instruction
{
    char direction;
    int distance;
};

struct Position
{
    int x;
    int y;
    bool operator<(const Position &other) const
    {
        return x < other.x || (x == other.x && y < other.y);
    }
};

std::vector<Instruction> parse(std::string &input)
{
    std::vector<Instruction> result;
    std::string token;
    Instruction instruction;
    size_t pos = 0;

    while ((pos = input.find_first_of(", ")) != std::string::npos)
    {
        token = input.substr(0, pos);

        instruction.direction = token[0];
        instruction.distance = std::stoi(token.substr(1, token.length() - 1));

        result.push_back(instruction);
        input.erase(0, pos + 2);
    }
    token = input.substr(0, pos);
    instruction.direction = token[0];
    instruction.distance = std::stoi(token.substr(1, token.length() - 1));
    result.push_back(instruction);
    return result;
}

int main()
{
    std::ifstream file("/Users/trulsjakobsen/dev/aoc/2016/inputs/01.txt");
    std::string input;
    std::getline(file, input);
    auto instructions = parse(input);

    Position position = {0, 0};
    Position direction = {0, 1};

    std::set<Position> visited;
    bool found = false;
    Position firstDouble;
    visited.insert(position);

    for (auto &instruction : instructions)
    {
        if (instruction.direction == 'R')
        {
            direction = {direction.y, -direction.x};
        }
        else
        {
            direction = {-direction.y, direction.x};
        }

        position.x += direction.x * instruction.distance;
        position.y += direction.y * instruction.distance;

        if (!found && visited.find(position) != visited.end())
        {
            firstDouble = position;
            found = true;
        }
        if (!found)
            visited.insert(position);
    }

    std::cout << "Part 1: " << abs(position.x) + abs(position.y) << std::endl;
    std::cout << "Part 2: " << abs(firstDouble.x) + abs(firstDouble.y) << std::endl;
}
