# Общее описание решение 
geometric_lib содержит себе .py файлы с вычислением площадей круга, квадрата, прямоугольника, треугольника. 

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# func "calc.py"
функция заключается в применении функции к запрошенной формуле для запрошенной формулы для фигуры с введенными данными


#фукнция "area" для квадрата
вычисляет площадь квадрата

#пример
>>> area(2)
<<< 2 * 2 = 4

#функция "area" для треугольника
вычисляет площадь квадрата

#пример
>>> area(3, 4, 5)
<<< sqrt(6(6 - 3)(6 - 4)(6 - 5)) = 6

#функция "area" для круга
вычисляет площадь круга

#пример
>>>  area(1)
<<< 3.141592653589793


#функция "perimetr" для треугольника
считает периметр треугольника

#пример
>>> perimetr(3, 4, 5)
<<< 3 + 4 + 5 = 12

#функция "perimetr" для круга
вычисляет периметр круга

#пример
>>>perimetr(1)
<<< 6,28318530718

#история изменений 
| | * b5b0fae727ca72c317c383b39c0af73d6adcd81c (HEAD -> new_features_451249, origin/develop, develop) L-04: Update docs for calculate.py
| | * d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
| | * 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
| | * d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
| |/
| * d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added
|/
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
