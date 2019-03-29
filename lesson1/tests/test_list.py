""" List tests """
import statistics


def test_triple():
    """Create list of 3, triple each. ensure that length of each is three"""
    my_list = [c * 3 for c in 'list']
    for each_element in my_list:
        assert len(each_element) == 3
    print('Length of each element equals 3')


def test_sum_length():
    """Sum two lists, check length """
    my_list1 = 'list'
    my_list2 = 'list'
    result_list = my_list1 + my_list2
    assert len(result_list) == 8
    print('Length of result list equals 8')


def test_join():
    """Join test"""
    list1 = ['g', 'e', 'e', 'k', 's']
    result_string = "".join(list1)
    assert len(result_string) == 5
    print('Length of result list string 5')


def test_avg_temp(get_temp):
    """List of temp, check avg temperature is higher than some, max temp from fix"""
    temperatures = [32.2, 5, 20, 15, 25, 23, 22.4, 10, 13]
    avg_temp = statistics.mean(temperatures)
    print(avg_temp)
    max_temp = get_temp
    assert avg_temp < max_temp
