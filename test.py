import os, shutil

print("Виберіть мову || Choose language")
lang = input("Українська || English: ")

#Ukraine
if lang == "Українська":
    print("Програма створена для веб-розробників")
    print("Створити проект ---- Видалити проект ---- Перейменувати Проект")
    Answer_1 = input("Вибір: ")

    if Answer_1 == "Створити проект":
        Answer_2 = input("Як ви бажаєте її назвати: ")
        Answer_html = input("Як ви хочете назвати .html файл: ")
        Answer_css = input("Як ви хочете назвати .css файл: ")
        Answer_js = input("Як ви хочете назвати .js файл: ")
        Answer_3 = input("Вам потрібний Jquery: ")
        Answer_4 = input("Вам потрібний Bootstrap: ")
        print("Ваш проект створено цим шляхом: ", os.getcwd())

        os.mkdir(Answer_2)
        os.makedirs(f"{Answer_2}/css")
        os.makedirs(f"{Answer_2}/img")
        os.makedirs(f"{Answer_2}/js")

        index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
        index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        if Answer_3 == "Так":
            index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
            index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        if Answer_4 == "Так":
            index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
            index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        if Answer_3 and Answer_4 == "Так":
            index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
            index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        index_css = open(f"{Answer_2}/css/{Answer_css}.css", "w")
        index_js = open(f"{Answer_2}/js/{Answer_js}.js", "w")

    elif Answer_1 == "Перейменувати Проект":
        Answer_2 = input("Яким шляхом перебуває: ")
        Answer_3 = input("Нове ім'я для проекту: ")
        os.rename(f"{Answer_2}", f"{Answer_3}")

    elif Answer_1 == "Видалити проект":
        Answer_2 = input("Яким шляхом знаходиться ваш проект: ")
        shutil.rmtree(f"{Answer_2}")
        print("Ваш проект був успішно видалений")

#English
elif lang == "English":
    print("The program was created for web projects")
    print("Create Project ---- Delete Project ---- Rename Project")
    Answer_1 = input("Choice: ")

    if Answer_1 == "Create Project":
        Answer_2 = input("What do you want to call her: ")
        Answer_html = input("What do you want to name the .html file: ")
        Answer_css = input("What do you want to name the .css file: ")
        Answer_js = input("What do you want to name the .js file: ")
        Answer_3 = input("You need Jquery: ")
        Answer_4 = input("You need Bootstrap: ")
        print("Your project is created in this path: ", os.getcwd())

        os.mkdir(Answer_2)
        os.makedirs(f"{Answer_2}/css")
        os.makedirs(f"{Answer_2}/img")
        os.makedirs(f"{Answer_2}/js")

        index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
        index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        if Answer_3 == "Yes":
            index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
            index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
            """)

            if Answer_4 == "Yes":
                index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
                index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

            if Answer_3 and Answer_4 == "Yes":
                index_html = open(f"{Answer_2}/{Answer_html}.html", "w")
                index_html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/{Answer_css}.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <script src="js/{Answer_js}.js"></script>
</body>
</html>
        """)

        index_css = open(f"{Answer_2}/css/{Answer_css}.css", "w")
        index_js = open(f"{Answer_2}/js/{Answer_js}.js", "w")

    elif Answer_1 == "Rename Project":
        Answer_2 = input("Which path is: ")
        Answer_3 = input("New name for the project: ")
        os.rename(f"{Answer_2}", f"{Answer_3}")

    elif Answer_1 == "Delete Project":
        Answer_2 = input("What path is your project on: ")
        shutil.rmtree(f"{Answer_2}")
        print("Your project has been successfully deleted")

input()
