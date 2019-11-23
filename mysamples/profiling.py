'''to get profiling details for any function'''
import cProfile
import pstats


def decorator_profile(inputfn):
    cProfile.run(inputfn.__name__ + '()')
    return inputfn


# def decorator_profile(inputfn):
#     # cProfile.run(inputfn.__name__ + '()')
#     def inner():
#         cProfile.run(inputfn.__name__ + '()')
#         return inputfn()
#     return inner


# from concurrent_futures import processfn, threadfn
# if __name__ == "__main__":
#     cProfile.run('processfn()', 'proessStats')
#     cProfile.run('threadfn()', 'threadStats')
#     p = pstats.Stats('proessStats')
#     print(p.sort_stats('time').print_stats(10))

