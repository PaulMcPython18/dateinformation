from flask import Flask, render_template, make_response, request
import flask
app = Flask(__name__)
count = 1
@app.route('/')
def index():
    task1 = request.cookies.get('task1')
    time1 = request.cookies.get('time1')
    task2 = request.cookies.get('task2')
    time2 = request.cookies.get('time2')
    task3 = request.cookies.get('task3')
    time3 = request.cookies.get('time3')
    task4 = request.cookies.get('task4')
    time4 = request.cookies.get('time4')
    return render_template('index.html', task1=task1, time1=time1, task2=task2, time2=time2, task3=task3, time3=time3, task4=task4, time4=time4)
@app.route('/view')
def view():
    task1 = request.cookies.get('task1')
    time1 = request.cookies.get('time1')
    task2 = request.cookies.get('task2')
    time2 = request.cookies.get('time2')
    task3 = request.cookies.get('task3')
    time3 = request.cookies.get('time3')
    task4 = request.cookies.get('task4')
    time4 = request.cookies.get('time4')
    return render_template('view.html', task1=task1, time1=time1, task2=task2, time2=time2, task3=task3,
                               time3=time3, task4=task4, time4=time4)
@app.route('/', methods= ['POST'] )
def add_cookie():
    global count
    if len(request.form['namequery1']) <= 13 or len(request.form['namequery2']) < 24:
        return render_template('index.html', message='* Please input a task with a longer word length *')
    if len(request.form['namequery1']) >= 300 or len(request.form['namequery2']) > 80:
        return render_template('index.html', message='* Please input a task with a shorter word length *')
    if count == 1:
        print(count)
        resp = make_response(render_template('view.html', notification='* Your task has been added to the list, click the "Delete all Tasks" button on the homepage to remove it *'))
        print(request.form['namequery1'])
        resp.set_cookie('task1', request.form['namequery1'])
        framework = request.cookies.get('task1')
        print(framework)
        #
        framework = request.cookies.get('task1')
        print(framework)
        print(request.form['namequery2'])
        resp.set_cookie('time1', request.form['namequery2'])
        print(request.cookies.get('task1'))
        print(request.cookies.get('time1'))
        count += 1
        return resp
    if count == 2:
        print(count)
        resp = make_response(render_template('view.html', notification='* Your task has been added to the list, click the "Delete all Tasks" button on the homepage to remove it *'))
        print(request.form['namequery1'])
        resp.set_cookie('task2', request.form['namequery1'])
        framework = request.cookies.get('task2')
        print(framework)
        #
        framework = request.cookies.get('task2')
        print(framework)
        resp.set_cookie('time2', request.form['namequery2'])
        count += 1
        return resp
    if count == 3:
        count = 3
        print(count)
        resp = make_response(render_template('view.html', notification='* Your task has been added to the list, click the "Delete all Tasks" button on the homepage to remove it *'))
        print(request.form['namequery1'])
        resp.set_cookie('task3', request.form['namequery1'])
        framework = request.cookies.get('task3')
        print(framework)
        #
        framework = request.cookies.get('task3')
        print(framework)

        resp.set_cookie('time3', request.form['namequery2'])
        return resp
@app.route('/todo-list', methods= ['POST'])
def todo_list():
    global count
    task1 = request.cookies.get('task1')
    time1 = request.cookies.get('time1')
    task2 = request.cookies.get('task2')
    time2 = request.cookies.get('time2')
    task3 = request.cookies.get('task3')
    time3 = request.cookies.get('time3')
    task4 = request.cookies.get('task4')
    time4 = request.cookies.get('time4')
    resp = make_response(render_template('index.html', task1=task1, time1=time1, task2=task2, time2=time2, task3=task3,
                           time3=time3, task4=task4, time4=time4))
    if 'task1' not in request.cookies:
        resp.set_cookie('task1', 'N/A')
    if 'time1' not in request.cookies:
        resp.set_cookie('time1', 'N/A')
    if 'task2' not in request.cookies:
        resp.set_cookie('task2', 'N/A')
    if 'time2' not in request.cookies:
        resp.set_cookie('time2', 'N/A')
    if 'task3' not in request.cookies:
        resp.set_cookie('task3', 'N/A')
    if 'time3' not in request.cookies:
        resp.set_cookie('time3', 'N/A')
    # /\ Checks if cookies are already existant, if not create them
    if request.cookies.get('task1') == 'N/A':
        print('Count 1')
        count = 1
        print(count)
    elif request.cookies.get('task2') == 'N/A':
        print('Count 2')
        count = 2
        print(count)
    elif request.cookies.get('task3') == 'N/A':
        print('Count 3')
        count = 3
    else:
        pass
    return resp
    # return render_template('index.html', task1=task1, time1=time1, task2=task2, time2=time2, task3=task3,
    #                        time3=time3, task4=task4, time4=time4)
@app.route('/todo-list')
def todo_list2():
    global count
    task1 = request.cookies.get('task1')
    time1 = request.cookies.get('time1')
    task2 = request.cookies.get('task2')
    time2 = request.cookies.get('time2')
    task3 = request.cookies.get('task3')
    time3 = request.cookies.get('time3')
    task4 = request.cookies.get('task4')
    time4 = request.cookies.get('time4')
    resp = make_response(render_template('index.html', task1=task1, time1=time1, task2=task2, time2=time2, task3=task3,
                                         time3=time3, task4=task4, time4=time4))
    if 'task1' not in request.cookies:
        resp.set_cookie('task1', 'N/A')
    if 'time1' not in request.cookies:
        resp.set_cookie('time1', 'N/A')
    if 'task2' not in request.cookies:
        resp.set_cookie('task2', 'N/A')
    if 'time2' not in request.cookies:
        resp.set_cookie('time2', 'N/A')
    if 'task3' not in request.cookies:
        resp.set_cookie('task3', 'N/A')
    if 'time3' not in request.cookies:
        resp.set_cookie('time3', 'N/A')
    # /\ Checks if cookies are already existant, if not create them
    if request.cookies.get('task1') == 'N/A':
        print('Count 1')
        count = 1
        print(count)
    elif request.cookies.get('task2') == 'N/A':
        print('Count 2')
        count = 2
        print(count)
    elif request.cookies.get('task3') == 'N/A':
        print('Count 3')
        count = 3
    else:
        pass
    return resp
@app.route('/clear')
def clear():
    global count
    resp = make_response(render_template('view.html', message='* Tasks Deleted *'))
    resp.set_cookie('task1', 'N/A')
    resp.set_cookie('time1', 'N/A')
    resp.set_cookie('task2', 'N/A')
    resp.set_cookie('time2', 'N/A')
    resp.set_cookie('task3', 'N/A')
    resp.set_cookie('time3', 'N/A')
    resp.set_cookie('task4', 'N/A')
    resp.set_cookie('time4', 'N/A')
    count = 1
    return resp
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/remove_task1')
def remove_task1():
    resp = make_response(render_template('view.html', message='* Task One Has Been Deleted/Checked Off *'))
    resp.set_cookie('task1', 'N/A')
    resp.set_cookie('time1', 'N/A')
    if 'c_count' in request.cookies:
        value = int(request.cookies.get('c_count'))
        nv = value + 1
        resp.set_cookie('c_count', str(nv))
    else:
        nv = 1
        resp.set_cookie('c_count', '1')
    value1 = request.cookies.get('c_count')
    if str(value1) == "4":
        resp.set_cookie('c_count', '1')

    # ---- #

    resp.set_cookie('task1', request.cookies.get('task2'))
    resp.set_cookie('time1', request.cookies.get('time2'))
    resp.set_cookie('task2', request.cookies.get('task3'))
    resp.set_cookie('time2', request.cookies.get('time3'))
    resp.set_cookie('task3', 'N/A')
    resp.set_cookie('time3', 'N/A')
    global count

    return resp
@app.route('/remove_task2')
def remove_task2():
    global count
    resp = make_response(render_template('view.html', message='* Task Two Has Been Deleted *'))
    resp.set_cookie('task2', 'N/A')
    resp.set_cookie('time2', 'N/A')
    resp.set_cookie('task2', request.cookies.get('task3'))
    resp.set_cookie('time2', request.cookies.get('time3'))
    resp.set_cookie('task3', 'N/A')
    resp.set_cookie('time3', 'N/A')

    return resp
@app.route('/remove_task3')
def remove_task3():
    resp = make_response(render_template('view.html', message='* Task Three Has Been Deleted *'))
    resp.set_cookie('task3', 'N/A')
    resp.set_cookie('time3', 'N/A')
    return resp
@app.route('/checked-off')
def checked_off():
    return render_template('checked_off.html')
if __name__ == "__main__":
    app.run(debug=True)