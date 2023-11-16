import os

# # path = os.getcwd()
# # print('мое место работы', path)
#
# if not os.path.isdir('folder'):
#     os.mkdir('folder')
# else:
#     print('Такая папка уже есть')
#
# os.chdir('fol')

# for dirpath, dirnames, filenames in os.walk('.'):
#     for dirname in dirnames:
#         print('Каталог', os.path.join(dirpath, dirname))
#     for filename in filenames:
#         print('File', os.path.join(dirpath, filename))
#
# os.remove('folder1/gif.txt')
# os.rmdir('folder')
# os.removedirs('f1/f2/f3/f4/f5')

# open('text.txt', 'w').write('fdfdfdfdf')
# print(os.stat('text.txt').st_mtime)

print(os.name)

with open('text.txt', 'w+') as f:
    f.write('dfdfdfdf')
    
