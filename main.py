import pygame

WIDTH, HEIGHT = 1200, 1000
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

BUTTON_WIDTH, BUTTON_HEIGHT = 40, 40
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elevator")
canvas = pygame.Surface((WIDTH, HEIGHT))


class Person:
    def __init__(self, start_floor, end_floor):
        self.start = start_floor
        self.end = end_floor
        self.weight = 70
        self.status_list = ["WAIT", "IN", "OUT"]
        self.status = self.status_list[0]
        self.position_y = 950 - start_floor*200 - 120
        self.position_x = 200 + (end_floor-1)*80
        self.text_position = (self.position_x+20, self.position_y-50)

    def change_status(self):
        if self.status == "WAIT":
            self.status = "IN"
        elif self.status == "IN":
            self.status = "OUT"
            

class Level:
    def __init__(self, number, y):
        self.number = number
        self.y = y


def draw_building():
    pygame.draw.line(WIN, BLACK, (500, 100), (500, 150), 4)
    pygame.draw.line(WIN, BLACK, (500, 290), (500, 350), 4)
    pygame.draw.line(WIN, BLACK, (500, 490), (500, 550), 4)
    pygame.draw.line(WIN, BLACK, (500, 690), (500, 750), 4)
    pygame.draw.line(WIN, BLACK, (500, 890), (500, 950), 4)

    pygame.draw.line(WIN, BLACK, (750, 100), (750, 950), 4)

    pygame.draw.line(WIN, BLACK, (500, 100), (750, 100), 4)
    pygame.draw.line(WIN, BLACK, (500, 950), (750, 950), 4)

    pygame.draw.line(WIN, BLUE, (500, 290), (50, 290), 2)
    pygame.draw.line(WIN, BLUE, (500, 490), (50, 490), 2)
    pygame.draw.line(WIN, BLUE, (500, 690), (50, 690), 2)
    pygame.draw.line(WIN, BLUE, (500, 890), (50, 890), 2)


def draw_elevator(elevator_y_position, weight, ticks):
    pygame.draw.rect(WIN, RED, (502, elevator_y_position, 246, 140), 2)

    comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    text = comic_sans.render(f'{weight}kg', False, (0, 0, 0))
    WIN.blit(text, (800, 100))

    text_time = comic_sans.render('{:.2f}'.format((300 - ticks)/60) + 's', False, (0, 0, 0))
    WIN.blit(text_time, (800, 200))
    pygame.display.update()


def draw_buttons():
    comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    level_one_text = comic_sans.render('1', False, (0, 0, 0))
    level_two_text = comic_sans.render('2', False, (0, 0, 0))
    level_three_text = comic_sans.render('3', False, (0, 0, 0))
    level_four_text = comic_sans.render('4', False, (0, 0, 0))
    plus_button = comic_sans.render('+', False, (0, 0, 0))
    minus_button = comic_sans.render('-', False, (0, 0, 0))

    pygame.draw.rect(WIN, BLACK, (50, 130, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 130))
    WIN.blit(plus_button, (140, 130))

    pygame.draw.rect(WIN, BLACK, (50, 175, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 175))
    WIN.blit(plus_button, (140, 175))

    pygame.draw.rect(WIN, BLACK, (50, 220, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 220))
    WIN.blit(plus_button, (140, 220))

    WIN.blit(level_one_text, (65, 130))
    WIN.blit(level_two_text, (65, 175))
    WIN.blit(level_three_text, (65, 220))

    pygame.draw.rect(WIN, BLACK, (50, 330, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 330))
    WIN.blit(plus_button, (140, 330))

    pygame.draw.rect(WIN, BLACK, (50, 375, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 375))
    WIN.blit(plus_button, (140, 375))

    pygame.draw.rect(WIN, BLACK, (50, 420, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 420))
    WIN.blit(plus_button, (140, 420))

    WIN.blit(level_one_text, (65, 330))
    WIN.blit(level_two_text, (65, 375))
    WIN.blit(level_four_text, (65, 420))

    pygame.draw.rect(WIN, BLACK, (50, 530, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 530))
    WIN.blit(plus_button, (140, 530))

    pygame.draw.rect(WIN, BLACK, (50, 575, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 575))
    WIN.blit(plus_button, (140, 575))

    pygame.draw.rect(WIN, BLACK, (50, 620, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 620))
    WIN.blit(plus_button, (140, 620))

    WIN.blit(level_one_text, (65, 530))
    WIN.blit(level_three_text, (65, 575))
    WIN.blit(level_four_text, (65, 620))

    pygame.draw.rect(WIN, BLACK, (50, 730, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 730))
    WIN.blit(plus_button, (140, 730))

    pygame.draw.rect(WIN, BLACK, (50, 775, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 775))
    WIN.blit(plus_button, (140, 775))

    pygame.draw.rect(WIN, BLACK, (50, 820, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    WIN.blit(minus_button, (100, 820))
    WIN.blit(plus_button, (140, 820))

    WIN.blit(level_two_text, (65, 730))
    WIN.blit(level_three_text, (65, 775))
    WIN.blit(level_four_text, (65, 820))


def draw_window():
    WIN.fill(WHITE)
    draw_building()
    draw_buttons()
    pygame.display.update()


def draw_amount_of_people_waiting(dict_of_people):
    comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    WIN.blit(comic_sans.render(str(dict_of_people["level4"]["to1"]), False, (0, 0, 0)), (120, 130))
    WIN.blit(comic_sans.render(str(dict_of_people["level4"]["to2"]), False, (0, 0, 0)), (120, 175))
    WIN.blit(comic_sans.render(str(dict_of_people["level4"]["to3"]), False, (0, 0, 0)), (120, 220))
    WIN.blit(comic_sans.render(str(dict_of_people["level3"]["to1"]), False, (0, 0, 0)), (120, 330))
    WIN.blit(comic_sans.render(str(dict_of_people["level3"]["to2"]), False, (0, 0, 0)), (120, 375))
    WIN.blit(comic_sans.render(str(dict_of_people["level3"]["to4"]), False, (0, 0, 0)), (120, 420))
    WIN.blit(comic_sans.render(str(dict_of_people["level2"]["to1"]), False, (0, 0, 0)), (120, 530))
    WIN.blit(comic_sans.render(str(dict_of_people["level2"]["to3"]), False, (0, 0, 0)), (120, 575))
    WIN.blit(comic_sans.render(str(dict_of_people["level2"]["to4"]), False, (0, 0, 0)), (120, 620))
    WIN.blit(comic_sans.render(str(dict_of_people["level1"]["to2"]), False, (0, 0, 0)), (120, 730))
    WIN.blit(comic_sans.render(str(dict_of_people["level1"]["to3"]), False, (0, 0, 0)), (120, 775))
    WIN.blit(comic_sans.render(str(dict_of_people["level1"]["to4"]), False, (0, 0, 0)), (120, 820))


def draw_people():
    pass


def add_to_queue(start_level, end_level, upward, downward, current_level, current_direction):
    if start_level >= current_level and start_level not in upward:
        upward.append(start_level)
    elif start_level < current_level and start_level not in downward:
        downward.append(start_level)
    if end_level >= current_level and end_level > start_level and end_level not in upward:
        upward.append(end_level)
    if end_level < current_level and end_level not in downward:
        downward.append(end_level)
    if current_direction == "NONE" and start_level >= current_level:
        return "UP"
    elif current_direction == "NONE" and start_level < current_level:
        return "DOWN"
    else:
        return current_direction


def main():
    amount_of_people = {
        "level1": {"to2": 1, "to3": 1, "to4": 1},
        "level2": {"to1": 1, "to3": 1, "to4": 1},
        "level3": {"to1": 1, "to2": 1, "to4": 1},
        "level4": {"to1": 1, "to2": 1, "to3": 1}
    }

    list_of_persons = []
    current_weight = 0
    counter = 0
    run = True
    clock = pygame.time.Clock()
    elevator_y = 750
    current_level = 1
    level_1 = Level(1, 750)
    level_2 = Level(2, 550)
    level_3 = Level(3, 350)
    level_4 = Level(4, 150)
    queue_of_upward_stops = list()
    queue_of_downward_stops = list()
    current_direction = "NONE"

    while run:
        clock.tick(FPS)
        draw_window()
        if current_direction == "NONE" and current_level != 1:
            counter += 1
        else:
            counter = 0

        if elevator_y == level_4.y:
            current_level = 4
        elif elevator_y == level_3.y:
            current_level = 3
        elif elevator_y == level_2.y:
            current_level = 2
        elif elevator_y == level_1.y:
            current_level = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= pygame.mouse.get_pos()[0] <= 90:
                    if 130 <= pygame.mouse.get_pos()[1] <= 170:
                        print("Take me from Level 4 to level 1")
                        current_direction = add_to_queue(4, 1, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level4"]["to1"]):
                            list_of_persons.append(Person(4, 1))

                    elif 175 <= pygame.mouse.get_pos()[1] <= 215:
                        print("Take me from Level 4 to level 2")
                        current_direction = add_to_queue(4, 2, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level4"]["to2"]):
                            list_of_persons.append(Person(4, 2))

                    elif 220 <= pygame.mouse.get_pos()[1] <= 260:
                        print("Take me from Level 4 to level 3")
                        current_direction = add_to_queue(4, 3, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level4"]["to3"]):
                            list_of_persons.append(Person(4, 3))

                    elif 330 <= pygame.mouse.get_pos()[1] <= 370:
                        print("Take me from Level 3 to level 1")
                        current_direction = add_to_queue(3, 1, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level3"]["to1"]):
                            list_of_persons.append(Person(3, 1))

                    elif 375 <= pygame.mouse.get_pos()[1] <= 415:
                        print("Take me from Level 3 to level 2")
                        current_direction = add_to_queue(3, 2, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level3"]["to2"]):
                            list_of_persons.append(Person(3, 2))

                    elif 420 <= pygame.mouse.get_pos()[1] <= 460:
                        print("Take me from Level 3 to level 4")
                        current_direction = add_to_queue(3, 4, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level3"]["to4"]):
                            list_of_persons.append(Person(3, 4))

                    elif 530 <= pygame.mouse.get_pos()[1] <= 570:
                        print("Take me from Level 2 to level 1")
                        current_direction = add_to_queue(2, 1, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level2"]["to1"]):
                            list_of_persons.append(Person(2, 1))

                    elif 575 <= pygame.mouse.get_pos()[1] <= 615:
                        print("Take me from Level 2 to level 3")
                        current_direction = add_to_queue(2, 3, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level2"]["to3"]):
                            list_of_persons.append(Person(2, 3))

                    elif 620 <= pygame.mouse.get_pos()[1] <= 660:
                        print("Take me from Level 2 to level 4")
                        current_direction = add_to_queue(2, 4, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level2"]["to4"]):
                            list_of_persons.append(Person(2, 4))

                    elif 730 <= pygame.mouse.get_pos()[1] <= 770:
                        print("Take me from Level 1 to level 2")
                        current_direction = add_to_queue(1, 2, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level1"]["to2"]):
                            list_of_persons.append(Person(1, 2))

                    elif 775 <= pygame.mouse.get_pos()[1] <= 815:
                        print("Take me from Level 1 to level 3")
                        current_direction = add_to_queue(1, 3, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level1"]["to3"]):
                            list_of_persons.append(Person(1, 3))

                    elif 820 <= pygame.mouse.get_pos()[1] <= 860:
                        print("Take me from Level 1 to level 4")
                        current_direction = add_to_queue(1, 4, queue_of_upward_stops, queue_of_downward_stops, current_level, current_direction)
                        queue_of_upward_stops.sort()
                        queue_of_downward_stops.sort(reverse=True)
                        for number in range(amount_of_people["level1"]["to4"]):
                            list_of_persons.append(Person(1, 4))

                elif 100 <= pygame.mouse.get_pos()[0] <= 120:
                    if 130 <= pygame.mouse.get_pos()[1] <= 170:
                        if amount_of_people["level4"]["to1"] >= 2:
                            amount_of_people["level4"]["to1"] -= 1
                    elif 175 <= pygame.mouse.get_pos()[1] <= 215:
                        if amount_of_people["level4"]["to2"] >= 2:
                            amount_of_people["level4"]["to2"] -= 1
                    elif 220 <= pygame.mouse.get_pos()[1] <= 260:
                        if amount_of_people["level4"]["to3"] >= 2:
                            amount_of_people["level4"]["to3"] -= 1
                    elif 330 <= pygame.mouse.get_pos()[1] <= 370:
                        if amount_of_people["level3"]["to1"] >= 2:
                            amount_of_people["level3"]["to1"] -= 1
                    elif 375 <= pygame.mouse.get_pos()[1] <= 415:
                        if amount_of_people["level3"]["to2"] >= 2:
                            amount_of_people["level3"]["to2"] -= 1
                    elif 420 <= pygame.mouse.get_pos()[1] <= 460:
                        if amount_of_people["level3"]["to4"] >= 2:
                            amount_of_people["level3"]["to4"] -= 1
                    elif 530 <= pygame.mouse.get_pos()[1] <= 570:
                        if amount_of_people["level2"]["to1"] >= 2:
                            amount_of_people["level2"]["to1"] -= 1
                    elif 575 <= pygame.mouse.get_pos()[1] <= 615:
                        if amount_of_people["level2"]["to3"] >= 2:
                            amount_of_people["level2"]["to3"] -= 1
                    elif 620 <= pygame.mouse.get_pos()[1] <= 660:
                        if amount_of_people["level2"]["to4"] >= 2:
                            amount_of_people["level2"]["to4"] -= 1
                    elif 730 <= pygame.mouse.get_pos()[1] <= 770:
                        if amount_of_people["level1"]["to2"] >= 2:
                            amount_of_people["level1"]["to2"] -= 1
                    elif 775 <= pygame.mouse.get_pos()[1] <= 815:
                        if amount_of_people["level1"]["to3"] >= 2:
                            amount_of_people["level1"]["to3"] -= 1
                    elif 820 <= pygame.mouse.get_pos()[1] <= 860:
                        if amount_of_people["level1"]["to4"] >= 2:
                            amount_of_people["level1"]["to4"] -= 1
                elif 140 <= pygame.mouse.get_pos()[0] <= 160:
                    if 130 <= pygame.mouse.get_pos()[1] <= 170:
                        if amount_of_people["level4"]["to1"] <= 7:
                            amount_of_people["level4"]["to1"] += 1
                    elif 175 <= pygame.mouse.get_pos()[1] <= 215:
                        if amount_of_people["level4"]["to2"] <= 7:
                            amount_of_people["level4"]["to2"] += 1
                    elif 220 <= pygame.mouse.get_pos()[1] <= 260:
                        if amount_of_people["level4"]["to3"] <= 7:
                            amount_of_people["level4"]["to3"] += 1
                    elif 330 <= pygame.mouse.get_pos()[1] <= 370:
                        if amount_of_people["level3"]["to1"] <= 7:
                            amount_of_people["level3"]["to1"] += 1
                    elif 375 <= pygame.mouse.get_pos()[1] <= 415:
                        if amount_of_people["level3"]["to2"] <= 7:
                            amount_of_people["level3"]["to2"] += 1
                    elif 420 <= pygame.mouse.get_pos()[1] <= 460:
                        if amount_of_people["level3"]["to4"] <= 7:
                            amount_of_people["level3"]["to4"] += 1
                    elif 530 <= pygame.mouse.get_pos()[1] <= 570:
                        if amount_of_people["level2"]["to1"] <= 7:
                            amount_of_people["level2"]["to1"] += 1
                    elif 575 <= pygame.mouse.get_pos()[1] <= 615:
                        if amount_of_people["level2"]["to3"] <= 7:
                            amount_of_people["level2"]["to3"] += 1
                    elif 620 <= pygame.mouse.get_pos()[1] <= 660:
                        if amount_of_people["level2"]["to4"] <= 7:
                            amount_of_people["level2"]["to4"] += 1
                    elif 730 <= pygame.mouse.get_pos()[1] <= 770:
                        if amount_of_people["level1"]["to2"] <= 7:
                            amount_of_people["level1"]["to2"] += 1
                    elif 775 <= pygame.mouse.get_pos()[1] <= 815:
                        if amount_of_people["level1"]["to3"] <= 7:
                            amount_of_people["level1"]["to3"] += 1
                    elif 820 <= pygame.mouse.get_pos()[1] <= 860:
                        if amount_of_people["level1"]["to4"] <= 7:
                            amount_of_people["level1"]["to4"] += 1
        if counter == 300 and current_direction == "NONE":
            counter = 0
            queue_of_downward_stops.append(1)
            current_direction = "DOWN"
        if len(queue_of_upward_stops) == 0 and current_direction == "UP" and len(queue_of_downward_stops) != 0:
            current_direction = "DOWN"
        elif len(queue_of_upward_stops) != 0 and current_direction == "DOWN" and len(queue_of_downward_stops) == 0:
            current_direction = "UP"
        elif len(queue_of_upward_stops) == 0 and len(queue_of_downward_stops) == 0:
            current_direction = "NONE"

        if len(queue_of_upward_stops) != 0 or len(queue_of_downward_stops) != 0:
            if current_direction == "UP":
                if queue_of_upward_stops[0] == current_level:
                    for person_id in range(len(list_of_persons)):
                        if list_of_persons[person_id].start == current_level:
                            list_of_persons[person_id].change_status()
                        elif list_of_persons[person_id].end == current_level:
                            list_of_persons[person_id].change_status()
                            list_of_persons[person_id] = 0

                    while 0 in list_of_persons:
                        list_of_persons.remove(0)

                    queue_of_upward_stops.pop(0)
                    draw_elevator(elevator_y, current_weight, counter)
                    pygame.time.wait(1000)
                else:
                    elevator_y -= 1
            elif current_direction == "DOWN":
                if queue_of_downward_stops[0] == current_level:
                    for person_id in range(len(list_of_persons)):
                        if list_of_persons[person_id].start == current_level:
                            list_of_persons[person_id].change_status()
                        elif list_of_persons[person_id].end == current_level:
                            list_of_persons[person_id].change_status()
                            list_of_persons[person_id] = 0

                    while 0 in list_of_persons:
                        list_of_persons.remove(0)

                    queue_of_downward_stops.pop(0)
                    draw_elevator(elevator_y, current_weight, counter)
                    pygame.time.wait(1000)
                else:
                    elevator_y += 1
        current_weight = len(list_of_persons)*70

        print("Downward", queue_of_downward_stops)
        print("Upward = ", queue_of_upward_stops)
        print(list_of_persons)
        draw_amount_of_people_waiting(amount_of_people)
        draw_elevator(elevator_y, current_weight, counter)
    pygame.quit()


if __name__ == "__main__":
    main()
