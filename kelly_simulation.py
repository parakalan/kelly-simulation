import random
import numpy as np


def get_kelly_bet_amount(principal, fractional_odds, win_probability):
	# Bets based on Kelly criterion
	return principal * ((win_probability * (fractional_odds + 1)) - 1) / fractional_odds

def get_optimist_bet_amount(principal, fractional_odds, win_probability):
	# Bets all the amount
	return principal

def get_probabilist_bet_amount(principal, fractional_odds, win_probability):
	# Bets based on probability
	return principal * win_probability

def get_pragmatist_bet_amount_optimist(principal, fractional_odds, win_probability):
	# Bets based on probability and fractional_odds (Not kelly though), risk taker
	return max(principal * win_probability, principal * fractional_odds)

def get_pragmatist_bet_amount_pessimist(principal, fractional_odds, win_probability):
	# Bets based on probability and fractional_odds (Not kelly though), risk averse
	return min(principal * win_probability, principal * fractional_odds)

def get_extreme_pessimist_bet_amount(principal, fractional_odds, win_probability):
	return 0.2 * principal




def run_simulation(principal, fractional_odds, iterations):
	kelly_principal = optimist_principal = probabilist_principal = pragmatist_optimist_principal = pragmatist_pessimist_principal = extreme_pessimist_principal = principal
	for i in range(0, iterations):
		win_probability = float(np.round(np.random.random(), 3))
		kelly_bet_amount = get_kelly_bet_amount(kelly_principal, fractional_odds, win_probability)
		optimist_bet_amount = get_optimist_bet_amount(optimist_principal, fractional_odds, win_probability)
		probabilist_bet_amount = get_probabilist_bet_amount(probabilist_principal, fractional_odds, win_probability)
		pragmatist_bet_amount_optimist = get_pragmatist_bet_amount_optimist(pragmatist_optimist_principal, fractional_odds, win_probability)
		pragmatist_bet_amount_pessimist = get_pragmatist_bet_amount_pessimist(pragmatist_pessimist_principal, fractional_odds, win_probability)
		extreme_pessimist_bet_amount = get_extreme_pessimist_bet_amount(extreme_pessimist_principal, fractional_odds, win_probability)

		kelly_principal -= kelly_bet_amount
		optimist_principal -= optimist_bet_amount
		probabilist_principal -= probabilist_bet_amount
		pragmatist_optimist_principal -= pragmatist_bet_amount_optimist
		pragmatist_pessimist_principal -= pragmatist_bet_amount_pessimist
		pragmatist_pessimist_principal -= pragmatist_bet_amount_pessimist
		extreme_pessimist_principal -= extreme_pessimist_bet_amount

		sample_space = ['W'] * int(win_probability * 1000)
		sample_space += ['L'] * int((1 - win_probability) * 1000)

		random.shuffle(sample_space)

		result = random.choice(sample_space)

		if result == 'W':
			kelly_principal += kelly_bet_amount * (1 + fractional_odds)
			optimist_principal += optimist_bet_amount * (1 + fractional_odds)
			probabilist_principal += probabilist_bet_amount  * (1 + fractional_odds)
			pragmatist_optimist_principal += pragmatist_bet_amount_optimist  * (1 + fractional_odds)
			pragmatist_pessimist_principal += pragmatist_bet_amount_pessimist  * (1 + fractional_odds)
			extreme_pessimist_principal += extreme_pessimist_bet_amount  * (1 + fractional_odds)

		print(f"Round {i+1} results")
		print(f"Win probability = {win_probability}")
		print(f"Result = {result}")
		print(f"kelly_principal = {kelly_principal}")
		print(f"optimist_principal = {optimist_principal}")
		print(f"probabilist_principal = {probabilist_principal}")
		print(f"pragmatist_optimist_principal = {pragmatist_optimist_principal}")
		print(f"pragmatist_pessimist_principal = {pragmatist_pessimist_principal}")
		print(f"extreme_pessimist_principal = {extreme_pessimist_principal}")

	print(f"Round {i} results")
	print(f"Win probability = {win_probability}")
	print(f"Result = {result}")
	print(f"kelly_principal = {kelly_principal}")
	print(f"optimist_principal = {optimist_principal}")
	print(f"probabilist_principal = {probabilist_principal}")
	print(f"pragmatist_optimist_principal = {pragmatist_optimist_principal}")
	print(f"pragmatist_pessimist_principal = {pragmatist_pessimist_principal}")
	print(f"extreme_pessimist_principal = {extreme_pessimist_principal}")
	print("=========")
	print("Returns")
	print(f"kelly_returns = {100 * (kelly_principal - principal)/principal} ")
	print(f"optimist_returns = {100 * (optimist_principal - principal)/principal} ")
	print(f"probabilist_principal = {100 * (probabilist_principal - principal)/principal} ")
	print(f"pragmatist_optimist_returns = {100 * (pragmatist_optimist_principal - principal)/principal} ")
	print(f"pragmatist_pessimist_returns = {100 * (pragmatist_pessimist_principal - principal)/principal} ")
	print(f"extreme_pessimist_returns = {100 * (extreme_pessimist_principal - principal)/principal} ")


if __name__ == '__main__':
	run_simulation(10000, 1, 20)
