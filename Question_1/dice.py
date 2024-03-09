import random


def simulate_die_tosses(tosses, values):
    odd_count = 0
    for _ in range(tosses):
        die_toss = random.choice(values)
        if die_toss % 2 == 1:
            odd_count += 1
    return odd_count / tosses


if __name__ == "__main__":
    tosses_list = [50, 100, 1000, 2000, 3000, 10000, 100000]

    for tosses in tosses_list:
        probability = simulate_die_tosses(tosses, range(1, 13))
        weighted_probability = simulate_die_tosses(tosses, [1, 4, 6, 8, 9, 10, 12] + 2 * [2, 3, 5, 7, 11])

        print(f"{tosses} Tosses ->  Estimated probability of obtaining an odd number: {probability}")
        print(f"{tosses} Weighted Tosses ->  Estimated probability of obtaining an odd number with a weighted die: {weighted_probability} \n\n")