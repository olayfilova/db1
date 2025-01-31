# import pandas as pd
# import sqlite3
# import matplotlib.pyplot as plt
# import seaborn as sns
# mysql> SOURCE C:/temp/sakila-db/sakila-schema.sql;
# mysql> SOURCE C:/temp/sakila-db/sakila-data.sql;


# data = pd.read_csv('./menu.csv')
# conn = sqlite3.connect ('McDonalds.db')
# data.to_sql('MCDONALDS_NUTRITION', conn)
#
# df= pd.read_sql("select * from MCDONALDS_NUTRITION", conn)
# print(df)

# sqlite3 sakila.db
# .read/path/to/sakila-schema.sql
# .read/path/to/sakila-data.sql
# .exit


# conn =sqlite3.connect('../db1/sakila-db/sakila-schema.sql')
# data = pd.read_sql('../db1/sakila-db/sakila-data.sql', conn)
# # conn =sqlite3.connect('/Users/olgafilova/Downloads/sakila-db')
# data.to_sql('/pythonProject2/db1/sakila-db', conn)

# plot = sns.joinplot(x = 'Protein', y = 'total Fat', data = df)
# plot.show()
#
# df1.head()
# df.describe( include = 'all')
# %matplotlib inline
#
# plot= sns.swarmplot(x = 'Category', y = 'Sodium', data =df)
# plot.setp(plot.get_xticklabels, rotation = 70)
# plt.title('Sodium Content')
# plt.show()
#
#
# df['Sodium'].describe()
# df['Sodium'].idxmax()
# df.at[82, 'Item']
#
#
# plot2= sns.setstyle("whitegrid")
# ax=sns.boxplot (x = df ["Sugar"])
# plot2.show()


# def count_in_list(numbers: list, first_num: float, second_num: float, mode: 'normal'):
#     assert isinstance(numbers, list), "Numbers has to be a list"
#     assert all(isinstance(i, (int, float)) for i in numbers), "Only numbers are accepted"
#     assert isinstance(first_num, (int, float)) and isinstance(second_num, (int, float)), "Only numbers are accepted"
#
#     numbers = [float(j)for j in numbers]
#     first_num = float(first_num)
#     second_num = float(second_num)
#
#     if first_num != second_num and mode == 'normal':
#         count = 0
#         for i in numbers:
#             if i >= first_num and i <= second_num:
#                 count += 1
#         return count
#
#     elif first_num == second_num and mode=='first_to_next_same':
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = numbers.index(second_num, start_indx + 1)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError (f'Second occurrence of {second_num} not found')
#
#     elif first_num == second_num and mode =='first_to_last':
#         start_indx =  numbers.index(first_num)
#         end_indx = (len(numbers)-1) - (numbers[::-1].index(second_num))
#         return len(numbers[start_indx:end_indx +1])
#
#     else:
#         return (f"you choose first_num as: {first_num}, and second_num as: {second_num} => Please choose another mode")
#         #raise ValueError()
#
#
#
#
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1]
# print(count_in_list(nmbrs, 9,30, 'normal'))

#
# def count_and_sum_within_range(numbers, bound1, bound2):
#     assert isinstance(numbers, list), "Input numbers must be a list."
#     assert all(isinstance(x, int) for x in numbers), "All elements in numbers must be integers."
#     assert isinstance(bound1, int) and isinstance(bound2, int), "Bounds must be integers."
#
#     lower_bound = min(bound1, bound2)
#     upper_bound = max(bound1, bound2)
#
#     filtered_numbers = [number for number in numbers if lower_bound <= number <= upper_bound]
#     count = len(filtered_numbers)
#     total_sum = sum(filtered_numbers)
#     return count, total_sum
#
#
# numbers = [1, 2, 3, 4, 5, 30, 2, 6, 7, 8]
# bound1 = 2
# bound2 = 2
# print(count_and_sum_within_range(numbers, bound1, bound2))  # (5, 20)


# def count_in_list(numbers: list, first_num: int, second_num: int, mode: str):
#     assert isinstance(numbers, list), "Numbers has to be a list"
#     assert all(isinstance(i, int) for i in numbers), "Only numbers are accepted"
#     assert isinstance(first_num, int) and isinstance(second_num, int), "Only numbers are accepted"
#
#     # Convert all numbers to floats for consistent comparison
#     numbers = [int(j) for j in numbers]
#     first_num = int(first_num)
#     second_num = int(second_num)
#
#     if first_num != second_num and mode == 'normal':
#         # Count numbers in the range [first_num, second_num]
#         count = sum(1 for i in numbers if i >= first_num and i <= second_num)
#         return count
#
#     elif first_num == second_num and mode == 'first_to_next_same':
#         # Count numbers from the first occurrence of first_num to the next occurrence of second_num
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = numbers.index(second_num, start_indx + 1)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError(f'Second occurrence of {second_num} not found')
#
#     elif first_num == second_num and mode == 'first_to_last':
#         # Count numbers from the first occurrence of first_num to the last occurrence of second_num
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = len(numbers) - 1 - numbers[::-1].index(second_num)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError(f'Last occurrence of {second_num} not found')
#
#     else:
#         raise ValueError(f"Invalid mode or parameters: mode='{mode}', first_num={first_num}, second_num={second_num}")
#
# # Example usage
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count_in_list(nmbrs, 9, 30, 'normal'))  # Expected output: 4
# print(count_in_list(nmbrs, 9, 9, 'first_to_next_same'))  # Expected output: 3
# print(count_in_list(nmbrs, 9, 9, 'first_to_last'))  # Expected output: 4


# def count_in_list(numbers: list, first_num: int, second_num: int, mode: str):
#     assert isinstance(numbers, list), "Numbers has to be a list"
#     assert all(isinstance(i, int) for i in numbers), "Only numbers are accepted"
#     assert isinstance(first_num, int) and isinstance(second_num, int), "Only numbers are accepted"
#
#     # Convert all numbers to floats for consistent comparison
#     # numbers = [float(j) for j in numbers]
#     # first_num = float(first_num)
#     # second_num = float(second_num)
#
#     if mode == 'normal':
#         # Ensure that the range is correctly interpreted even if bounds are reversed
#         lower_bound = min(first_num, second_num)
#         upper_bound = max(first_num, second_num)
#         count = sum(lower_bound <= i <= upper_bound for i in numbers)
#         return count
#
#     elif first_num == second_num and mode == 'first_to_next_same':
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = numbers.index(second_num, start_indx + 1)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError(f'Second occurrence of {second_num} not found')
#
#     elif first_num == second_num and mode == 'first_to_last':
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = len(numbers) - 1 - numbers[::-1].index(second_num)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError(f'Last occurrence of {second_num} not found')
#
#     else:
#         raise ValueError(f"Invalid mode or parameters: mode='{mode}', first_num={first_num}, second_num={second_num}")
#
# # Example usage
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1]
# print(count_in_list(nmbrs, 9, 30, 'normal')  # Expected output: 2
# print(count_in_list(nmbrs, 9, 9, 'first_to_next_same'))  # Expected output: 3
# print(count_in_list(nmbrs, 9, 9, 'first_to_last'))  # Expected output: 4


# def count_and_sum_within_range(numbers: list, first_num: int, second_num: int) -> tuple:
#     """
#     Count the number of integers in the list that are within the given range (inclusive) and calculate their sum.
#
#     Parameters:
#     - numbers: List of integers.
#     - first_num: The lower bound of the range (inclusive).
#     - second_num: The upper bound of the range (inclusive).
#
#     Returns:
#     - A tuple (count, total_sum), where count is the number of integers within the range and total_sum is their sum.
#     """
#
#     # Ensure numbers are integers
#     assert isinstance(numbers, list), "Numbers must be provided as a list."
#     assert all(isinstance(i, int) for i in numbers), "All elements in the list must be integers."
#     assert isinstance(first_num, int) and isinstance(second_num, int), "Both bounds must be integers."
#
#     # Normalize bounds to handle cases where first_num > second_num
#     lower_bound = min(first_num, second_num)
#     upper_bound = max(first_num, second_num)
#
#     count = 0
#     total_sum = 0
#
#     for number in numbers:
#         if lower_bound <= number <= upper_bound:
#             count += 1
#             total_sum += number
#
#     return count, total_sum
#
#
# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 7, 7, 7]
# bound1 = 7
# bound2 = 7
# print(count_and_sum_within_range(numbers, bound1, bound2))  # Output should be (5, 20)
#
# # Additional test cases
# print(count_and_sum_within_range([7, 2, 9, 4, 5, 6, 3, 8, 7], 7, 7))  # Output should be (3, 21) where 7 appears 3 times
# print(count_and_sum_within_range([7, 2, 9, 4, 5, 6, 3, 8, 7], 7, 9))  # Output should be (5, 29)
#
#
# def count_in_list(numbers: list, first_num: float, second_num: float, mode='normal'):
#     # Ensure input is a list of numbers (int or float)
#     assert isinstance(numbers, list), "Numbers has to be a list"
#     assert all(isinstance(i, (int, float)) for i in numbers), "Only numbers are accepted"
#     assert isinstance(first_num, (int, float)) and isinstance(second_num, (int, float)), "Only numbers are accepted"
#
#     # Convert all numbers in the list to floats for consistency
#     numbers = [float(num) for num in numbers]
#
#     first_num = float(first_num)
#     second_num = float(second_num)
#
#     if first_num != second_num and mode == 'normal':
#         count = 0
#         for i in numbers:
#             if i >= first_num and i <= second_num:
#                 count += 1
#         return count
#
#     elif first_num == second_num and mode == 'first_to_next_same':
#         start_indx = numbers.index(first_num)
#         try:
#             end_indx = numbers.index(second_num, start_indx + 1)
#             return len(numbers[start_indx:end_indx + 1])
#         except ValueError:
#             raise ValueError(f'Second occurrence of {second_num} not found')
#
#     elif first_num == second_num and mode == 'first_to_last':
#         start_indx = numbers.index(first_num)
#         end_indx = (len(numbers) - 1) - (numbers[::-1].index(second_num))
#         return len(numbers[start_indx:end_indx + 1])
#
#     else:
#         return (f"You chose first_num as: {first_num}, and second_num as: {second_num}. Please choose 'normal' mode")


# d
#
# def count_and(numbers: list, first_num: int, second_num: int, mode='normal'):
#     assert isinstance(numbers, list), "Numbers must be in a list format"
#     assert all(isinstance(i, int) for i in numbers), "Only numbers accepted in the list"
#     assert isinstance(first_num, int) and isinstance(second_num,
#     int), "First and second numbers must be int or float"
#
#     if first_num != second_num and mode == 'normal':
#         count = 0
#         for i in numbers:
#             if first_num <= i <= second_num:
#                 count += 1
#         return count
#
#     if first_num == second_num and mode == 'first_to_first':
#         start_indx = numbers.index(first_num)
#         end_indx = numbers.index(second_num, start_indx + 1)
#         return len(numbers[start_indx:end_indx + 1])
#
#     if first_num == second_num and mode == 'first_to_last':
#         start_indx = numbers.index(first_num)
#         end_indx = (len(numbers) - 1) - numbers[::-1].index(second_num)
#         return len(numbers[start_indx:end_indx + 1])
#
#     raise ValueError(
#         f"In this mode, you chose '{first_num}' as first_num, and '{second_num}' as second_num, which is invalid for mode '{mode}'")
#
#
# # Example usage
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
#
# # Test normal mode
# print(count_and(nmbrs, 1, 9, 'normal'))  # Output: 11 (numbers in range [1, 9])
#
# # Test first_to_first mode
# print(count_and(nmbrs, 9, 9, 'first_to_first'))  # Output: 3 (first 9 to next 9)
#
# # Test first_to_last mode
# print(count_and(nmbrs, 9, 9, 'first_to_last'))

#
# def count_and(numbers: list, first_num: int, second_num: int, mode='normal'):
#     assert isinstance(numbers, list), "Numbers has to be a list format"
#     assert all(isinstance(i, int) for i in numbers), "Only integers are accepted in the list"
#     assert isinstance(first_num, int) and isinstance(second_num, int), "First and second numbers must be integers"
#
#     start = numbers.index(first_num)
#     end = numbers.index(second_num)
#
#     count = []
#     total  = 0
#
#     if first_num != second_num and mode == 'normal':
#         assert isinstance(first_num< second_num)
#         for i in numbers[start:end+1]:
#             if first_num <= i <= second_num:
#                 count.append(i)
#                 total += num
#             print(count)
#         res = sum(count)
#         c_t = len(count)
#         return res, c_t, count,total
#
#     elif first_num == second_num and mode == 'first_to_first':
#         try:
#             end_indx = numbers.index(second_num, start + 1)
#             return len(numbers[start:end_indx + 1])
#         except ValueError:
#             raise ValueError(f"Second occurrence of {second_num} not found in the list")
#
#     elif first_num == second_num and mode == 'first_to_last':
#         end_indx = (len(numbers) - 1) - (numbers[::-1].index(second_num))
#         return len(numbers[start:end_indx + 1])
#
#     else:
#         raise ValueError(
#             f"In this mode, you chose '{first_num}' as first_num, and '{second_num}' as second_num'. Choose 'normal' mode"
#         )
#
#
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
#
# # Example usage:
# print(count_and(nmbrs, 1, 9, 'normal'))  # Output: Count of numbers in the range [1, 9]
# #
# #
# #
# #
# # def count_and(numbers: list, first_num: int, second_num: int, mode='normal'):
# #     assert isinstance(numbers, list), "Numbers has to be a list format"
# #     assert all(isinstance(i, int) for i in numbers), "Only integers are accepted in the list"
# #     assert isinstance(first_num, int) and isinstance(second_num, int), "First and second numbers must be integers"
# #
# #     try:
# #         start = numbers.index(first_num)
# #         end = numbers.index(second_num)
# #     except ValueError as e:
# #         return f"Error: {str(e)} - One of the bounds is not in the list"
# #
# #     count = []
# #     i=0
# #
# #     if first_num != second_num and mode == 'normal':
# #
# #         for i in numbers[start:end + 1]:
# #
# #             if first_num <= i <= second_num:
# #
# #                 count.append(i)
# #             print(f"Checking number {i}, count so far: {count}")  # Діагностичне повідомлення
# #
# #         res = sum(count)
# #         c_t = len(count)
# #         return res, c_t, count
# #
# #     elif first_num == second_num and mode == 'first_to_first':
# #         try:
# #             end_indx = numbers.index(second_num, start + 1)
# #             return len(numbers[start:end_indx + 1])
# #         except ValueError:
# #             raise ValueError(f"Second occurrence of {second_num} not found in the list")
# #
# #     elif first_num == second_num and mode == 'first_to_last':
# #         end_indx = (len(numbers) - 1) - (numbers[::-1].index(second_num))
# #         return len(numbers[start:end_indx + 1])
# #
# #     else:
# #         raise ValueError(
# #             f"In this mode, you chose '{first_num}' as first_num, and '{second_num}' as second_num'. Choose 'normal' mode"
# #         )
# #
# #
# # nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
# #
# # # Example usage:
# # print(count_and(nmbrs, 1, 9, 'normal'))  # Output: Count of numbers in the range [1, 9]
# #
# #
# #
# #
# # def count_and(numbers: list, first_num: int, second_num: int, mode='normal'):
# #     assert isinstance(numbers, list), "Numbers has to be a list format"
# #     assert all(isinstance(i, int) for i in numbers), "Only integers are accepted in the list"
# #     assert isinstance(first_num, int) and isinstance(second_num, int), "First and second numbers must be integers"
# #
# #     try:
# #         start = numbers.index(first_num)
# #         end = numbers.index(second_num)
# #     except ValueError as e:
# #         return f"Error: {str(e)} - One of the bounds is not in the list"
# #
# #     count = []
# #
# #     if first_num != second_num and mode == 'normal':
# #         for i in numbers[start:end + 1]:
# #             if first_num <= i <= second_num:
# #                 count.append(i)
# #                 print(f"Checking number {i}, count so far: {count}")  # Діагностичне повідомлення
# #
# #         res = sum(count)
# #         c_t = len(count)
# #         return res, c_t, count
# #
# #     elif first_num == second_num and mode == 'first_to_first':
# #         try:
# #             end_indx = numbers.index(second_num, start + 1)
# #             return len(numbers[start:end_indx + 1])
# #         except ValueError:
# #             raise ValueError(f"Second occurrence of {second_num} not found in the list")
# #
# #     elif first_num == second_num and mode == 'first_to_last':
# #         end_indx = (len(numbers) - 1) - (numbers[::-1].index(second_num))
# #         return len(numbers[start:end_indx + 1])
# #
# #     else:
# #         raise ValueError(
# #             f"In this mode, you chose '{first_num}' as first_num, and '{second_num}' as second_num'. Choose 'normal' mode"
# #         )
# #
# # nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
# #
# # # Example usage:
# # print(count_and(nmbrs, 1, 9, 'normal'))  # Output: Count of numbers in the range [1, 9]
#
#
# def count_and(numbers: list, first_num: int, second_num: int, mode='normal'):
#     assert isinstance(numbers, list), "Numbers has to be a list format"
#     assert all(isinstance(i, int) for i in numbers), "Only integers are accepted in the list"
#     assert isinstance(first_num, int) and isinstance(second_num, int), "First and second numbers must be integers"
#
#     try:
#         start = numbers.index(first_num)
#         if mode == 'normal':
#             end = numbers.index(second_num)
#         elif mode == 'first_to_last':
#             end = len(numbers) - 1 - numbers[::-1].index(second_num)
#         else:
#             end = numbers.index(second_num, start + 1)
#
#
#         # Ініціалізація змінних для підрахунку
#         count = 0
#         total_sum = 0
#
#         # Перебір чисел у списку та підрахунок тих, що потрапляють у діапазон
#         for num in numbers:
#             if first_num <= num <= second_num:
#                 count += 1
#                 total_sum += num
#
#         return count, total_sum
#
#     # count = []
#     #
#     # if first_num != second_num and mode == 'normal':
#     #     for i in numbers[start:end + 1]:
#     #         if first_num <= i <= second_num:
#     #             count.append(i)
#     #
#     #     res = sum(count)
#     #     c_t = len(count)
#     #     return res, c_t, count
#
#         if first_num == second_num:
#             if mode == 'first_to_first':
#                 if start != end:
#                     return 1, 1, [numbers[start]]
#                 else:
#                     return 0, 0, []
#
#             elif mode == 'first_to_last':
#                 return sum(numbers[start:end + 1]), len(numbers[start:end + 1]), numbers[start:end + 1]
#     except ValueError as e:
#                 return f"Error: {str(e)} - One of the bounds is not in the list"
#                 raise ValueError(f"Invalid mode or input values: {first_num} and {second_num}")
#
#
# nmbrs = [9, 30, 9, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
#
# # Example usage:
# print(count_and(nmbrs, 1, 9, 'normal'))  # Рахує кількість і суму в нормальному режимі
# print(count_and(nmbrs, 9, 9, 'first_to_first'))  # Від першого до наступного співпадіння
# print(count_and(nmbrs, 9, 9, 'first_to_last'))  # Від першого до останнього співпадіння
# print(count_and(nmbrs, 1, 9, 'normal'))  # Рахує кількість і суму в нормальному режимі для діапазону 1 до 9
#
# def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int) -> tuple[int, int]:
#     """
#     Підрахувати кількість чисел у списку, що потрапляють у заданий діапазон (включаючи обидві межі)
#     і їх суму.
#
#     :param numbers: список цілих чисел
#     :param lower_bound: нижня межа діапазону
#     :param upper_bound: верхня межа діапазону
#     :return: кортеж, що містить кількість чисел у діапазоні та їх суму
#     """
#     # Перевірка на валідність вхідних даних
#     assert isinstance(numbers, list), "Numbers must be a list of integers."
#     assert all(isinstance(i, int) for i in numbers), "All elements in the list must be integers."
#     assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers."
#
#     # Ініціалізація змінних для підрахунку
#     count = 0
#     total_sum = 0
#
#     # Перебір чисел у списку та підрахунок тих, що потрапляють у діапазон
#     for num in numbers:
#         if lower_bound <= num <= upper_bound:
#             count += 1
#             total_sum += num
#
#     return count, total_sum
#
# # Приклад використання функції
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# lower_bound = 1
# upper_bound = 8
# result = count_and_sum_in_range(numbers, lower_bound, upper_bound)
# print(result)  # Output: (5, 20)

#
# def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int, mode: str = 'normal') -> tuple[
#     int, int]:
#     """
#     Count the number of integers in the list that are within the specified range (inclusive of both bounds)
#     and calculate their sum based on the specified mode.
#
#     :param numbers: List of integers
#     :param lower_bound: The lower bound of the range (inclusive)
#     :param upper_bound: The upper bound of the range (inclusive)
#     :param mode: The mode of operation ('normal', 'first_to_first', 'first_to_last')
#     :return: A tuple containing the count of numbers and their sum
#     """
#     # Validate input types
#     assert isinstance(numbers, list), "Numbers should be a list"
#     assert all(isinstance(num, int) for num in numbers), "All items in the list should be integers"
#     assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers"
#
#     # Validate that the lower bound is less than or equal to the upper bound
#     assert lower_bound <= upper_bound, "Lower bound must be less than or equal to upper bound"
#
#     # Handle 'normal' mode
#     if mode == 'normal':
#         count = 0
#         total_sum = 0
#         for num in numbers:
#             if lower_bound <= num <= upper_bound:
#                 count += 1
#                 total_sum += num
#         return count, total_sum
#
#     # Handle 'first_to_first' mode
#     elif mode == 'first_to_first':
#         if lower_bound != upper_bound:
#             raise ValueError("In 'first_to_first' mode, lower_bound and upper_bound must be the same")
#
#         try:
#             start_indx = numbers.index(lower_bound)
#             end_indx = numbers.index(upper_bound, start_indx + 1)
#             count = end_indx - start_indx
#             total_sum = sum(numbers[start_indx:end_indx + 1])
#             return count, total_sum
#         except ValueError:
#             raise ValueError(f"Second occurrence of {upper_bound} not found in the list")
#
#     # Handle 'first_to_last' mode
#     elif mode == 'first_to_last':
#         if lower_bound != upper_bound:
#             raise ValueError("In 'first_to_last' mode, lower_bound and upper_bound must be the same")
#
#         try:
#             start_indx = numbers.index(lower_bound)
#             end_indx = (len(numbers) - 1) - numbers[::-1].index(upper_bound)
#             count = end_indx - start_indx + 1
#             total_sum = sum(numbers[start_indx:end_indx + 1])
#             return count, total_sum
#         except ValueError:
#             raise ValueError(f"Either occurrence of {lower_bound} or {upper_bound} not found in the list")
#
#     else:
#         raise ValueError(f"Invalid mode '{mode}' specified. Choose 'normal', 'first_to_first', or 'first_to_last'.")
#
#
# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# lower_bound = 0
# upper_bound = 6
# result = count_and_sum_in_range(numbers, lower_bound, upper_bound)
# print(result)  # Output: (5, 20)


# def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int, mode: str = 'normal') -> tuple[
#     int, int]:
#     """
#     Count the number of integers in the list that are within the specified range (inclusive of both bounds)
#     and calculate their sum based on the specified mode.
#
#     :param numbers: List of integers
#     :param lower_bound: The lower bound of the range (inclusive)
#     :param upper_bound: The upper bound of the range (inclusive)
#     :param mode: The mode of operation ('normal', 'first_to_first', 'first_to_last')
#     :return: A tuple containing the count of numbers and their sum
#     """
#     # Validate input types
#     assert isinstance(numbers, list), "Numbers should be a list"
#     assert all(isinstance(num, int) for num in numbers), "All items in the list should be integers"
#     assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers"
#
#     # Validate that the lower bound is less than or equal to the upper bound
#     assert lower_bound <= upper_bound, "Lower bound must be less than or equal to upper bound"
#
#     # Check if bounds are within the range of numbers
#     if lower_bound not in numbers:
#         raise ValueError(f"Lower bound {lower_bound} is not present in the list")
#     if upper_bound not in numbers:
#         raise ValueError(f"Upper bound {upper_bound} is not present in the list")
#
#     # Handle 'normal' mode
#     if mode == 'normal':
#         count = 0
#         total_sum = 0
#         for num in numbers:
#             if lower_bound <= num <= upper_bound:
#                 count += 1
#                 total_sum += num
#         return count, total_sum
#
#     # Handle 'first_to_first' mode
#     elif mode == 'first_to_first':
#         if lower_bound != upper_bound:
#             raise ValueError("In 'first_to_first' mode, lower_bound and upper_bound must be the same")
#
#         try:
#             start_indx = numbers.index(lower_bound)
#             end_indx = numbers.index(upper_bound, start_indx + 1)
#             count = end_indx - start_indx
#             total_sum = sum(numbers[start_indx:end_indx + 1])
#             return count, total_sum
#         except ValueError:
#             raise ValueError(f"Second occurrence of {upper_bound} not found in the list")
#
#     # Handle 'first_to_last' mode
#     elif mode == 'first_to_last':
#         if lower_bound != upper_bound:
#             raise ValueError("In 'first_to_last' mode, lower_bound and upper_bound must be the same")
#
#         try:
#             start_indx = numbers.index(lower_bound)
#             end_indx = (len(numbers) - 1) - numbers[::-1].index(upper_bound)
#             count = end_indx - start_indx + 1
#             total_sum = sum(numbers[start_indx:end_indx + 1])
#             return count, total_sum
#         except ValueError:
#             raise ValueError(f"Either occurrence of {lower_bound} or {upper_bound} not found in the list")
#
#     else:
#         raise ValueError(f"Invalid mode '{mode}' specified. Choose 'normal', 'first_to_first', or 'first_to_last'.")
#
#
# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# lower_bound = 0
# upper_bound = 6
# result = count_and_sum_in_range(numbers, lower_bound, upper_bound)
# print(result)  # Output: (5, 20)
#
#
def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int, mode: str = 'normal') -> tuple[
    int, int]:
    assert isinstance(numbers, list) and all(isinstance(num, int) for num in numbers), "List must contain only integers"
    assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers"
    # assert lower_bound <= upper_bound, "Lower bound must be less than or equal to upper bound"

    if lower_bound not in numbers or upper_bound not in numbers:
        # raise (ValueError("Bounds must exist within the list"))
        print("Bounds must exist within the list")

    if mode == 'normal':
        count = sum(lower_bound <= num <= upper_bound for num in numbers)
        total_sum = sum(num for num in numbers if lower_bound <= num <= upper_bound)

    elif mode in ['first_to_first', 'first_to_last']:
        start_idx = numbers.index(lower_bound)
        end_idx = (numbers.index(upper_bound, start_idx + 1) if mode == 'first_to_first'
                   else len(numbers) - 1 - numbers[::-1].index(upper_bound))

        count = end_idx - start_idx + 1
        total_sum = sum(numbers[start_idx:end_idx + 1])

    else:
        # raise (ValueError("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'."))
        print("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'.")

    return count, total_sum



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lower_bound = 2
upper_bound = 6

result = count_and_sum_in_range(numbers, lower_bound, upper_bound, mode='normal')
print(result)

#
# def count_and_sum_in_range(numbers: list[int], lower_num: int, upper_num: int, mode='normal'):
#     assert isinstance(numbers, list) and all(isinstance(num, int) for num in numbers), "List within integers only"
#     assert isinstance(lower_num, int) and isinstance(upperr_num, int), "Integers only - Unsupported format"
#     # assert lower_num<=upper_num, "Lowwer number has to be less than or equal to upper number."
#
#     if lower_num not in numbers or upper_num not in numbers:
#         print('Bounds must be in the list')
#         # raise ValueError('Bounds must be in the list')
#
#     if mode == 'normal':
#         count_n = sum(lower_num <= num <= upper_num for num in numbers)
#         total = sum(num for num in numbers if lower_num <= num <= upper_num)
#
#     elif mode in ['first_to_first', 'first_to_last']:
#         start = numbers.inder(lower.num)
#         end = (numbers.index(upper_num), start + 1) if mode == 'first_to_first'
#                 else len(numbers) - 1 - numbers[::-1].index(upper_num)
#
#     count_n = end - start + 1
#     total = sum(numbers[start:end + 1])
#
# else:
# print("Invalid mode. Chose 'normal', 'first_to_first', or 'first_to_last'")
# # raise (Value Error(Invalid mode. Chose 'normal', 'first_to_first', or 'first_to_last'"))
# return count_n, total
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# lower_num = 2
# upper_num = 6
#
# res = count_and_sum_in_range(numbers, lower_num, upper_num, mode='normal')
# print(res)



def count_and_sum_in_range(numbers: list[int], lower_bound: int, upper_bound: int, mode: str = 'normal') -> tuple[
    int, int]:
    assert isinstance(numbers, list) and all(isinstance(num, int) for num in numbers), "List must contain only integers"
    assert isinstance(lower_bound, int) and isinstance(upper_bound, int), "Bounds must be integers"
    # assert lower_bound <= upper_bound, "Lower bound must be less than or equal to upper bound"

    if lower_bound not in numbers or upper_bound not in numbers:
        print("Bounds must exist within the list")
        # raise (ValueError("Bounds must exist within the list"))

    if mode == 'normal':
        count = sum(lower_bound <= num <= upper_bound for num in numbers)
        total_sum = sum(num for num in numbers if lower_bound <= num <= upper_bound)

    elif mode in ['first_to_first', 'first_to_last']:
        start_idx = numbers.index(lower_bound)
        end_idx = (numbers.index(upper_bound, start_idx + 1) if mode == 'first_to_first'
                   else len(numbers) - 1 - numbers[::-1].index(upper_bound))

        count = end_idx - start_idx + 1
        total_sum = sum(numbers[start_idx:end_idx + 1])

    else:
        print("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'.")
        # raise (ValueError("Invalid mode. Choose 'normal', 'first_to_first', or 'first_to_last'."))
    return count, total_sum




numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lower_bound = 2
upper_bound = 6

result = count_and_sum_in_range(numbers, lower_bound, upper_bound, mode='normal')
print(result)