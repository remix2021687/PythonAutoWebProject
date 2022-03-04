import os, shutil

print("Выберите язык || Choose language")
lang = input("Русский || English: ")

if lang == "Русский":
    print("Программа создана для web проектов")
    print("Создать проект ---- Удалить проект ---- Переименовать Проект")
    Answer_1 = input("Выбор: ")

    if Answer_1 == "Создать проект":
        Answer_2 = input("Как вы хочите ее назвать: ")
        Answer_html = input("Как вы хочите назвать .html файл: ")
        Answer_css = input("Как вы хочите назвать .css файл: ")
        Answer_js = input("Как вы хочите назвать .js файл: ")
        Answer_3 = input("Вам нужен Jquery: ")
        Answer_4 = input("Вам нужен Bootstrap: ")
        print("Ваш проект создан по этом пути: ", os.getcwd())

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

        if Answer_3 == "Да":
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

        if Answer_4 == "Да":
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

        if Answer_3 and Answer_4 == "Да":
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

    elif Answer_1 == "Переиминовать Проект":
        Answer_2 = input("По какому пути находится: ")
        Answer_3 = input("Новое имя для проекта: ")
        os.rename(f"{Answer_2}", f"{Answer_3}")

    elif Answer_1 == "Удалить проект":
        Answer_2 = input("По какому пути нахожится ваш проект: ")
        shutil.rmtree(f"{Answer_2}")
        print("Ваш проект был успешно удален")


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
