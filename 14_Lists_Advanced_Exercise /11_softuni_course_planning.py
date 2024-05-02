# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of
# the next course, separated by a comma and a space ", ". Until you receive the "course start" command, you will
# be given some commands to modify the course schedule.
# The possible commands are:
#     • "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
#     • "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
#     • "Remove:{lessonTitle}" - remove the lesson, if it exists.
#     • "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
#     • "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson
#     exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson
#     doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises,
# if there are any following the lessons.
# Input / Constraints
#     • On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
#     • Until "course start" you will receive commands in the format described above.
# Output
#     • Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".

course_objects = input().split(", ")

command = input()

while not command == "course start":
    info = command.split(":")
    actoin = info[0]
    lesson = info[1]
    if actoin == "Add":
        course_objects.append(lesson)
    elif actoin == "Insert":
        index = int(info[2])
        if lesson not in course_objects:
            course_objects = course_objects[:index] + [lesson] + course_objects[index:]
    elif actoin == "Remove":
        if lesson in course_objects:
            course_objects.remove(lesson)
        for word in course_objects:
            if lesson in word:
                course_objects.remove(word)
    elif actoin == "Swap":
        lesson2 = info[2]
        lesson_ex = f"{lesson}-Exercise"
        lesson2_ex = f"{lesson2}-Exercise"
        if lesson in course_objects and lesson2 in course_objects:
            index1 = course_objects.index(lesson)
            index2 = course_objects.index(lesson2)
            course_objects[index1], course_objects[index2] = course_objects[index2], course_objects[index1]
        if lesson_ex in course_objects:
            course_objects.remove(lesson_ex)
            index_ex = course_objects.index(lesson) + 1
            course_objects = course_objects[:index_ex] + [lesson_ex] + course_objects[index_ex:]
        if lesson2_ex in course_objects:
            course_objects.remove(lesson2_ex)
            index_ex2 = course_objects.index(lesson2) + 1
            course_objects = course_objects[:index_ex2] + [lesson2_ex] + course_objects[index_ex2:]
    elif actoin == "Exercise":
        lesson_exercise = f'{lesson}-Exercise'
        if lesson in course_objects and lesson_exercise not in course_objects:
            index_exercise = course_objects.index(lesson) + 1
            course_objects = course_objects[:index_exercise] + [lesson_exercise] + course_objects[index_exercise:]
        if lesson not in course_objects:
            course_objects.append(lesson)
            course_objects.append(lesson_exercise)
    command = input()

for i in range(len(course_objects)):
    print(f'{i + 1}.{course_objects[i]}')

