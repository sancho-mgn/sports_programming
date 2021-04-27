def Unmanned(L, N, track):
    total_dist = L
    red_add_time = 0
    for i in range(N):
        travel_time, time_red, time_green = [item for item in track[i]]
        total_wait_time = travel_time + red_add_time # общее время в пути вместе с простоем на красном свете
        total_traf_light = time_red + time_green # общее время работы светофора

        if total_traf_light and L > travel_time: # проверяем что время работы светофора не ноль, и что до светофора мы доедем
             cur_time_lights = total_wait_time % total_traf_light # проверяем попадаем ли мы под светофор, с учётом пройденных ранее светофоров
             if cur_time_lights < time_red:
                 red_add_time += time_red - cur_time_lights # вычисляем общее время простоя на красном свете светофоров
    total_dist += red_add_time
    return total_dist

#L = 10
#N = 2
#track = [[3, 5, 5], [5, 2, 2]]
#track = [[3, 6, 2], [6, 2, 2]]
#print(Unmanned(L, N, track))