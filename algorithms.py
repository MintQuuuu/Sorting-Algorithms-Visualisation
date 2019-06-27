import random
import time


def quick(list_to_sort, start, stop, plot, step_time):
    time.sleep(step_time)
    if stop - start > 0:
        pivot, left, right = list_to_sort[start], start, stop
        while left <= right:
            while list_to_sort[left] < pivot:
                left += 1
            while list_to_sort[right] > pivot:
                right -= 1
            if left <= right:
                list_to_sort[left], list_to_sort[right] = list_to_sort[right], list_to_sort[left]
                plot.points = [(i, list_to_sort[i]) for i in range(len(list_to_sort))]
                left += 1
                right -= 1
        quick(list_to_sort, start, right, plot, step_time)
        quick(list_to_sort, left, stop, plot, step_time)


def selection(list_to_sort, plot, step_time):
    for i in range(len(list_to_sort)):
        index_of_min = i + list_to_sort[i:].index(min(list_to_sort[i:]))
        list_to_sort[i], list_to_sort[index_of_min] = list_to_sort[index_of_min], list_to_sort[i]
        plot.points = [(i, list_to_sort[i]) for i in range(len(list_to_sort))]
        time.sleep(step_time)


def bubble(list_to_sort, plot, step_time):
    i = 0
    while i < (len(list_to_sort) - 1):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            plot.points = [(i, list_to_sort[i]) for i in range(len(list_to_sort))]
            time.sleep(step_time)
            i = 0
        else:
            i += 1


def generate_random_list(size):
    return [random.randint(0, 100) for i in range(1, size)]
