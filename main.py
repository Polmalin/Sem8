# Создать телефонный справочник
# с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

#
def edit ():#принимает данные о человеке, список данных
  with open('spravochnik.txt','a', encoding= 'utf-8') as file:
      print("Welcome")
      string=input("Введите данные в формате 'Фамилия Имя Отчество номер телефона':")
      if string:
          file.write('\n' + string)



def search():
  with open('spravochnik.txt','r', encoding= 'utf-8') as file:
      info=input("Введите что-то для поиска: ")
      found = False
      while True:
          line=file.readline().split()
          if not line:
              break
          for part in line:
              if part.lower()==info.lower():
                  print("found:" + str.join(" ", line))
                  found=True
      if not found:
        print ("not found")

def interface():#функция взаимодействия с пользователем
    print("Welcome")
    mode=input('Введите режим работы со справочником, напишите edit или search: ')
    if mode=="search":
        search()
    if mode=="edit":
        edit()

while True:
    interface()


