def Unmanned(L, N, track):
    total_dist = L
    red_add_time = 0
    for i in range(N):
        travel_time, time_red, time_green = track[i][0], track[i][1], track[i][2]
        total_wait_time = travel_time + red_add_time
        total_traf_light = time_red + time_green

        if total_traf_light > travel_time and L > travel_time:
             cur_time_lights = total_wait_time % total_traf_light
             if cur_time_lights < time_red:
                 red_add_time += time_red - cur_time_lights
    total_dist += red_add_time
    return total_dist

#L = 10
#N = 2
#track = [[2, 5, 5], [5, 2, 2]]
#print(Unmanned(L, N, track))