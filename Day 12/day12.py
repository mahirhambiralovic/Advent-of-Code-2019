import copy

def iterate_rotation(positions, velocities):
    positions_c = copy.deepcopy(positions)
    for i in range(4):
        for j in range(4):
            if positions_c[i]["x"] < positions_c[j]["x"]:
                velocities[i]["x"] += 1
            elif positions_c[i]["x"] > positions_c[j]["x"]:
                velocities[i]["x"] -= 1

            if positions_c[i]["y"] < positions_c[j]["y"]:
                velocities[i]["y"] += 1
            elif positions_c[i]["y"] > positions_c[j]["y"]:
                velocities[i]["y"] -= 1

            if positions_c[i]["z"] < positions_c[j]["z"]:
                velocities[i]["z"] += 1
            elif positions_c[i]["z"] > positions_c[j]["z"]:
                velocities[i]["z"] -= 1
        # Update position
        positions[i]["x"] += velocities[i]["x"]
        positions[i]["y"] += velocities[i]["y"]
        positions[i]["z"] += velocities[i]["z"]

moon1_pos = {"x":-7, "y":-1, "z":6}
moon1_vel = {"x":0, "y":0, "z":0}
moon2_pos = {"x":6, "y":-9, "z":-9}
moon2_vel = {"x":0, "y":0, "z":0}
moon3_pos = {"x":-12, "y":2, "z":-7}
moon3_vel = {"x":0, "y":0, "z":0}
moon4_pos = {"x":4, "y":-17, "z":-12}
moon4_vel = {"x":0, "y":0, "z":0}

# Part 1
positions = [moon1_pos, moon2_pos, moon3_pos, moon4_pos]
velocities = [moon1_vel, moon2_vel, moon3_vel, moon4_vel]

positions_p1 = copy.deepcopy(positions)
velocities_p1 = copy.deepcopy(velocities)

for iteration in range(1,1001):
    iterate_rotation(positions_p1, velocities_p1)

energy = 0
for i in range(4):
    potential_energy = abs(positions_p1[i]["x"]) + abs(positions_p1[i]["y"]) + abs(positions_p1[i]["z"])
    kinetic_energy = abs(velocities_p1[i]["x"]) + abs(velocities_p1[i]["y"]) + abs(velocities_p1[i]["z"])
    energy += potential_energy * kinetic_energy
print(energy)


# Part 2
# X, Y and Z are independent. Find when X, Y and Z return to original, and find least common multiple.
# The code is messy, but it works...
positions_p2 = copy.deepcopy(positions)
velocities_p2 = copy.deepcopy(velocities)
xs = []
ys = []
zs = []
for moon in positions_p2:
    xs.append(moon["x"])
    ys.append(moon["y"])
    zs.append(moon["z"])

iteration = 1
x_iteration = 0
y_iteration = 0
z_iteration = 0
while True:
    iterate_rotation(positions_p2, velocities_p2)
    if positions_p2[0]["x"] == xs[0] and positions_p2[1]["x"] == xs[1] and positions_p2[2]["x"] == xs[2] and positions_p2[3]["x"] == xs[3]:
        if velocities_p2[0]["x"] == 0 and velocities_p2[1]["x"] == 0 and velocities_p2[2]["x"] == 0 and velocities_p2[3]["x"] == 0:
            if x_iteration == 0:
                x_iteration = iteration

    if positions_p2[0]["y"] == ys[0] and positions_p2[1]["y"] == ys[1] and positions_p2[2]["y"] == ys[2] and positions_p2[3]["y"] == ys[3]:
        if velocities_p2[0]["y"] == 0 and velocities_p2[1]["y"] == 0 and velocities_p2[2]["y"] == 0 and velocities_p2[3]["y"] == 0:
            if y_iteration == 0:
                y_iteration = iteration

    if positions_p2[0]["z"] == zs[0] and positions_p2[1]["z"] == zs[1] and positions_p2[2]["z"] == zs[2] and positions_p2[3]["z"] == zs[3]:
        if velocities_p2[0]["z"] == 0 and velocities_p2[1]["z"] == 0 and velocities_p2[2]["z"] == 0 and velocities_p2[3]["z"] == 0:
            if z_iteration == 0:
                z_iteration = iteration

    if x_iteration != 0 and y_iteration != 0 and z_iteration != 0:
         break
    iteration += 1

    if iteration % 20000 == 0:
        print("At iteration {} Found X:{}, Y:{}, Z:{}".format(iteration, bool(x_iteration), bool(y_iteration), bool(z_iteration)))

print("X period is: {}".format(x_iteration))
print("Y period is: {}".format(y_iteration))
print("Z period is: {}".format(z_iteration))
print("Enter numbers here to find LCM: https://www.calculatorsoup.com/calculators/math/lcm.php")
