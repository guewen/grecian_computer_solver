#!/usr/bin/env python3
from itertools import permutations


class GrecianComputer:

    def __init__(self, layers):
        self.layers = layers
        self.layer_positions = [0, 0, 0, 0, 0]

    def rotate(self, layer, position):
        self.layer_positions[layer] = position

    def value_at(self, row, col):
        for layer_index, layer in enumerate(self.layers):
            if len(layer) <= row:
                continue
            value = layer[row][(col + self.layer_positions[layer_index]) % 12]
            if value:
                return value

    def solve(self):
        result = Result()
        for row in range(4):
            for col in range(12):
                result.set_value(row, col, self.value_at(row, col))
        result.set_layer_position(self.layer_positions)
        return result



class Result:
    def __init__(self):
        self.reset()
        self.layer_positions = [0, 0, 0, 0, 0]

    def reset(self):
        self.numbers = [[None] * 12 for x in range(4)]

    def set_value(self, row, col, value):
        self.numbers[row][col] = value

    def set_layer_position(self, layer_positions):
        self.layer_positions = layer_positions

    def verify(self):
        return all(total == 42 for total in self.totals())

    def totals(self):
        totals = [0] * 12
        for col in range(12):
            for layer in range(4):
                totals[col] += self.numbers[layer][col]
        return totals

    def __str__(self):
        return (
            'Positions: ' + str(self.layer_positions) + '\n' +
            '\n'.join([' '.join([str(x).rjust(2) for x in row]) for row in self.numbers]) +
            '\n' + '-' * 35 + '\n' +
            ' '.join([str(x).rjust(2) for x in self.totals()])
        )

if __name__ == '__main__':
    layers = [
        [
            [3, None, 6, None, 10, None, 7, None, 15, None, 8, None],
        ],
        [
            [7, 3, None, 6, None, 11, 11, 6, 11, None, 6, 17],
            [4, None, 7, 15, None, None, 14, None, 9, None, 12, None],
        ],
        [
            [9, 13, 9, 7, 13, 21, 17, 4, 5, None, 7, 8],
            [21, 6, 15, 4, 9, 18, 11, 26, 14, 1, 12, None],
            [5, None, 10, None, 8, None, 22, None, 16, None, 9, None],
        ],
        [
            [7, None, 9, None, 7, 14, 11, None, 8, None, 16, 2],
            [9, 20, 12, 3, 6, None, 14, 12, 3, 8, 9, None],
            [3, 26, 6, None, 2, 13, 9, None, 17, 19, 3, 12],
            [1, None, 9, None, 12, None, 6, None, 10, None, 10, None],
        ],
        [
            [14, 11, 14, 14, 11, 14, 11, 14, 11, 11, 14, 11],
            [8, 9, 10, 11, 12, 13, 14, 15, 4, 5, 6, 7],
            [3, 3, 14, 14, 21, 21, 9, 9, 4, 4, 6, 6],
            [2, 5, 10, 7, 16, 8, 7, 8, 8, 3, 4, 12],
        ],
    ]

    solver = GrecianComputer(layers)

    for layer1_pos in range(12):
        solver.rotate(0, layer1_pos)
        for layer2_pos in range(12):
            solver.rotate(1, layer2_pos)
            for layer3_pos in range(12):
                solver.rotate(2, layer3_pos)
                for layer4_pos in range(12):
                    solver.rotate(3, layer4_pos)
                    result = solver.solve()
                    print(result)
                    valid = result.verify()
                    print('✅' if valid else '❌')
                    if valid:
                        print('Solved!')
                        exit(0)
                    print()
