
import os,time
import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS


path_dir_input    =   "d:/!!!!!Фото/"
path_dir_output   =   "d:/foto_sort_Danilin/"


path_dir_input    =   "d:/Герман фото/"
path_dir_output   =   "d:/Герман фото сортировка24-11-19/"



inc         =   0
countErr    =   0

# trueExt =   ['.JPG', '.jpg', '.MOV', '.mov', '.gif']
trueExt     =   ['.MPG', '.3gp', '.png', '.bmp', '.jpg', '.JPG', '.MOV', '.AVI', '.mov',  '.mp4', '.psd']

# оставить только уникальные значения
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def month_name(month_number):
    curr_name_month =   ""
    if month_number ==  1:
        curr_name_month =   "январь"
    elif month_number ==  2:
        curr_name_month =   "февраль"
    elif month_number ==  3:
        curr_name_month =   "март"
    elif month_number ==  4:
        curr_name_month =   "апрель"
    elif month_number ==  5:
        curr_name_month =   "май"
    elif month_number ==  6:
        curr_name_month =   "июнь"
    elif month_number ==  7:
        curr_name_month =   "июль"
    elif month_number ==  8:
        curr_name_month =   "август"
    elif month_number ==  9:
        curr_name_month =   "сентябрь"
    elif month_number ==  10:
        curr_name_month =   "октябрь"
    elif month_number ==  11:
        curr_name_month =   "ноябрь"
    elif month_number ==  12:
        curr_name_month =   "декабрь"
    return curr_name_month


def mk_Directory(path):
    try:
        os.makedirs(path)
        print ("Успешно создана директория %s" % path)
    except OSError:
        print ("Создать директорию %s не удалось" % path)
    # else:


# начало замера времени
date_start  = datetime.datetime.now()
mass_ext    =   []
arr_files   =   []
arr_dir     =   []

class DateTime_img():
    def __init__(self, parameter):        
        self.tm_year   =   int(parameter[0:4])    
        self.tm_mon    =   int(parameter[5:7])  
        self.tm_mday   =   int(parameter[8:10])  
          
    

# Использование библиотеки Pilow
def get_exif_made_date(fn):    
    ext_ok  =   [".jpg",".jpeg",".tiff"]
    m_date  =   time.gmtime(os.path.getmtime(fullName))
    cur_ext =   os.path.splitext(fullName)[1]
    if cur_ext in ext_ok:   
        i = Image.open(fn)
        info = i._getexif()
        if info==None:
            return m_date
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded  ==   "DateTimeDigitized":   
                m_date  =   DateTime_img(value) 
                break

    return m_date



# Сканирование каталогов и файлов
for dirpath, dirnames, filenames in os.walk(path_dir_input):
    for filename in filenames:                       
        fullName        =   dirpath+'/'+filename       
        
        structur_date   =   get_exif_made_date(fullName)
        # structur_date   =   time.gmtime(os.path.getmtime(fullName))        
        cur_ext         =   os.path.splitext(fullName)[1]

        mass_ext.append(cur_ext)          
        if cur_ext in trueExt:        
            inc+=1     
            old_fullName    =   fullName
            new_path        =   path_dir_output+""+str(structur_date.tm_year)+"/"+month_name(structur_date.tm_mon)
            arr_dir.append(new_path)  
            
            # получаем имя тек папки
            sp          =   fullName.split(os.path.sep)
            part_name   =   sp[len(sp)-1]
            part_name   =   part_name.replace("/","")
            part_name   =   part_name.replace("""\"""","")
            part_name   =   part_name.replace(filename,"")

            new_file_name   =   str(structur_date.tm_mday)+"_"+month_name(structur_date.tm_mon)+"_"+str(structur_date.tm_year)+"_"+part_name+str(cur_ext)            
            arr_files.append([old_fullName,new_path+"/"+new_file_name])        


# # Создание папок для переноса
# arr_dir =   uniq(arr_dir)
# for carr_dur in arr_dir:
#     mk_Directory(carr_dur)

# # оставим только уникальные расширения
# mass_ext    =   uniq(mass_ext)


# print("Обработка файлов:")


# for target_list in arr_files:            
#     try:
#         shutil.copy(target_list[0], target_list[1])
#         # move(target_list[0], target_list[1])
#     except :
#         print(" не удалось скоприровать : ",target_list[0])
#         countErr    +=   1
        


# вывод инф. статистики
print()
print(mass_ext)
print('Продолжительность:{0} для {1} файлов'.format(datetime.datetime.now() - date_start,inc))
print("Не перемещено:",countErr)

 