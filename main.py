from dp_on_weights import solve as solve_dp_on_weights
from two_approx import solve as solve_two_approx
from ptas import solve as solve_ptas
from branch_and_bound import solve as solve_branch_and_cut
from tests.tests import get_tests, timing

PTAS_POLYNOMIAL_CONST = 4  # 80 percents from OPT
TIMING_COUNT = 5


def main():
    for test_name, (capacity, profits, weights, choice, optimal_profit) in get_tests().items():
        print(f"Test {test_name}:")
        print(f"Capacity: {capacity}")
        print(f"Optimal profit: {optimal_profit}")
        print(f"Optimal choice: {choice}")

        dp_on_weights_time, (
            dp_on_weights_profit, dp_on_weights_weight, dp_on_weights_choice,
            dp_num_of_intermediate_solutions) = timing(
            TIMING_COUNT,
            solve_dp_on_weights,
            weights,
            profits,
            capacity)
        print(f"DP on weights profit: {dp_on_weights_profit}")
        print(f"DP on weights weight: {dp_on_weights_weight}")
        print(f"DP on weights choice: {dp_on_weights_choice}")
        print(f"DP number of intermediate solutions: {dp_num_of_intermediate_solutions}")
        print(f"DP time: {dp_on_weights_time:.{2}}")

        two_approx_time, (
            two_approx_profit, two_approx_weight, two_approx_choice, two_approx_num_of_intermediate_solutions) = timing(
            TIMING_COUNT,
            solve_two_approx, weights,
            profits,
            capacity)
        print(f"2-approx profit: {two_approx_profit}")
        print(f"2-approx weight: {two_approx_weight}")
        print(f"2-approx choice: {two_approx_choice}")
        print(f"2-approx number of intermediate solutions: {two_approx_num_of_intermediate_solutions}")
        print(f"2-approx time: {two_approx_time:.{2}}")

        ptas_time, (
            ptas_approx_profit, ptas_approx_weight, ptas_approx_choice, ptas_num_of_intermediate_solutions) = timing(
            TIMING_COUNT, solve_ptas,
            weights, profits,
            capacity,
            k=PTAS_POLYNOMIAL_CONST)
        print(f"PTAS with {PTAS_POLYNOMIAL_CONST=} profit: {ptas_approx_profit}")
        print(f"PTAS with {PTAS_POLYNOMIAL_CONST=} weight: {ptas_approx_weight}")
        print(f"PTAS with {PTAS_POLYNOMIAL_CONST=} choice: {ptas_approx_choice}")
        print(
            f"PTAS with {PTAS_POLYNOMIAL_CONST=} number of intermediate solutions: {ptas_num_of_intermediate_solutions}")
        print(f"PTAS with {PTAS_POLYNOMIAL_CONST=} time: {ptas_time:.{2}}")

        branch_and_cut_time, (
            branch_and_cut_profit, branch_and_cut_weight, branch_and_cut_choice,
            branch_and_cut_num_of_intermediate_solutions) = timing(
            TIMING_COUNT,
            solve_branch_and_cut, weights,
            profits,
            capacity)
        print(f"branch_and_cut profit: {branch_and_cut_profit}")
        print(f"branch_and_cut weight: {branch_and_cut_weight}")
        print(f"branch_and_cut choice: {branch_and_cut_choice}")
        print(f"branch_and_cut number of intermediate solutions: {branch_and_cut_num_of_intermediate_solutions}")
        print(f"branch_and_cut time: {branch_and_cut_time:.{2}}")
        print()


if __name__ == "__main__":
    main()
