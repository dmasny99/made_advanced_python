# Запуск профилировщиков:  
* Самый наивный, который просто считает время создания, удаления, изменения аттрибута и тд (пункт 1 дз):  
```
python3 time_profile.py --num_iter 1000000 
```
* Профилировние вызовов с использованием декоратора из пункта 3 дз (декоратор cProfile):  
```
python3 call_profile.py --class_type human --num_iter 1000000 
```
>>Где ```--class_type``` один из вариантов: ```human, human slots, human wref ```
* Профилирование памяти:  
```
python3 mem_profile.py --num_iter 1000000
```

