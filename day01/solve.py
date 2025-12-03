from aocd import get_data, submit

YEAR = 2025

def part1(data):
    lines = data.strip().split("\n")
    x = 50
    count = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            x = (x + amount) % 100
        elif direction == "L":
            x = (x - amount) % 100

        if x == 0:
            count += 1

    return count


def part2(data):
    lines = data.strip().split("\n")
    x = 50
    count = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            for i in range(amount):
                x +=1
                y = x % 100
                if y == 0:
                    count += 1


        elif direction == "L":
            for i in range(amount):
                x-= 1
                y = x % 100
                if y == 0:
                    count += 1

    return count


def main():
    day = int(__file__.split("/")[-2][-2:])
    data = get_data(day=day, year=YEAR)

    p1 = part1(data)
    submit(p1, part="a", day=day, year=YEAR)

    p2 = part2(data)
    if p2 is not None:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
