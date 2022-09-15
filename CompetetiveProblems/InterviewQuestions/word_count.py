l = ["this is a sample", "of words in english", "these sample words are all in english",
    "this is a sample", "of words in english", "these sample words are all in english"]
import concurrent.futures

def threaded_execution(l):
    tpool = concurrent.futures.ThreadPoolExecutor()

    cores = 3
    n = len(l)
    chunk = n // 3
    futures = []
    for i in range(chunk):
        inp_chunk = l[i*cores:(i+1) * cores]
        futures.append(tpool.submit(count_of_words, inp_chunk))
    for i in range(len(futures)):
        if futures[i].done():
            print("Thread", i, "Result:", futures[i].result())


def count_of_words(l):
    word_count = []
    for each in l:
        w_count = each.count(" ")+1
        word_count.append(w_count)
    return sum(word_count)


print(threaded_execution(l))