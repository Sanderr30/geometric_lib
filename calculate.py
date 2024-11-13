import circle
import square
import triangle

# Список фигур и функций
figs = {
    'circle': {'module': circle, 'params': 1},
    'square': {'module': square, 'params': 1},
    'triangle': {'module': triangle, 'params': 3}
}

funcs = ['perimeter', 'area']

def calc(fig, func, size):
    # Проверка корректности фигуры и функции
    if fig not in figs:
        raise ValueError(f"Figure'{fig}' is not available. Available figures: {list(figs.keys())}")
    if func not in funcs:
        raise ValueError(f"Function '{func}' is not available. Available functions: ['area', 'perimeter']")

    # Получение модуля и функции для вычислений
    module = figs[fig]['module']
    func_to_call = getattr(module, func)

    # Проверка количества параметров
    expected_params = figs[fig]['params']
    if len(size) != expected_params:
        raise ValueError(f"For the figure '{fig}' {expected_params}  parameters are required , but was provided {len(size)}")

    # Выполнение функции и вывод результата
    result = func_to_call(*size)
    print(f'{func.capitalize()} of {fig} with size(s) {size} is {result}')
    return result