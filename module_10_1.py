from datetime import datetime
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f"Какое-то слово № {i} \n")
            sleep(0.1)
            file.close()
            print(f"Завершилась запись в файл {file_name}")

time_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

time_start2 = datetime.now()
f1 = Thread(target=write_words, args=(10, 'example5.txt'))
f2 = Thread(target=write_words, args=(30, 'example6.txt'))
f3 = Thread(target=write_words, args=(200, 'example7.txt'))
f4 = Thread(target=write_words, args=(100, 'example8.txt'))

f1.start()
f2.start()
f3.start()
f4.start()

f1.join()
f2.join()
f3.join()
f4.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)






