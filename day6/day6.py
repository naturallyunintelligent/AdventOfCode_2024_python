from tabulate import tabulate

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

class Guard:
    motion = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}

    def __init__(self, position, initial_dirn):
        self.position = position
        self.direction = initial_dirn
        self.target = position[0] + self.motion[self.direction][0], self.position[1] + self.motion[self.direction][1]

    def update_direction(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction =  "left"
        elif self.direction == "left":
            self.direction = "up"



def day(input_data):

    # build a map and locate the guard
    map=[]
    for y, line in enumerate(input_data):
        map_length = len(input_data)
        map_width = len(line)
        map.append([])
        for x, char in enumerate(line):
            map[y].append(char)
            if char == ("^" or "v" or "<"  or ">"):
                # find the guards initial position
                match char:
                    case "^":
                        guard = Guard(position=(y,x), initial_dirn="up")
                    case "v":
                        guard = Guard(position=(y,x), initial_dirn="down")
                    case "<":
                        guard = Guard(position=(y,x), initial_dirn="left")
                    case ">":
                        guard = Guard(position=(y,x), initial_dirn="right")
                    case _:
                        "oopsie"
                map[y][x] = "."


    #include the first position
    step_count = 0

    ##find the next obstacle
    # target_posn = (
    # guard.position[0] + guard.motion[guard.direction][0], guard.position[1] + guard.motion[guard.direction][1])

    while guard.position[0] >= 0 and guard.position[0] <= map_length-1 and guard.position[1] >= 0 and guard.position[1] <= map_width-1:
        # tabulated_map = tabulate(map)
        # print(tabulated_map)
        # print(step_count)
        try:
            if map[guard.target[0]][guard.target[1]] == ".":
                ##take a step
                map[guard.position[0]][guard.position[1]] = "X"
                step_count += 1
                #update position and target
                guard.position = (
                    guard.position[0] + guard.motion[guard.direction][0],
                    guard.position[1] + guard.motion[guard.direction][1])
                guard.target = (
                    guard.target[0] + guard.motion[guard.direction][0],
                    guard.target[1] + guard.motion[guard.direction][1])
                continue
            if map[guard.target[0]][guard.target[1]] == "X":
                ##take a step
                map[guard.position[0]][guard.position[1]] = "X"
                #this dot has already been covered!
                #update position and target
                guard.position = (
                    guard.position[0] + guard.motion[guard.direction][0],
                    guard.position[1] + guard.motion[guard.direction][1])
                guard.target = (
                    guard.target[0] + guard.motion[guard.direction][0],
                    guard.target[1] + guard.motion[guard.direction][1])
                continue
            ##find the next obstacle
            if map[guard.target[0]][guard.target[1]] == "#":
                guard.update_direction()
                guard.target = (
                    guard.position[0] + guard.motion[guard.direction][0],
                    guard.position[1] + guard.motion[guard.direction][1])
                continue
            else:
                print("oopsie")
                break
        except IndexError: break

    map[guard.position[0]][guard.position[1]] = "X"
    step_count += 1

    # tabulated_map = tabulate(map)
    # print(tabulated_map)

    answer = step_count
    if input_text_file == "sample.txt":
        assert answer == 41
    return answer


if __name__ == '__main__':

    #input_text_file = "sample.txt"
    input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer = day(data)
    print(f"day: {answer=}")


    #store answer as a comment
    #a:
    #b: